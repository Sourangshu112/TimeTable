from ortools.sat.python import cp_model
import collections
import csv
import data

# --- 1. DATA INPUT ---
# (Same data as before)
teachers = data.teachers

theory = data.theory

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
SLOTS = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
LUNCH_SLOT_INDEX = 4 # S5

def main():
    print("Started running...")
    model = cp_model.CpModel()

    # --- Pre-process ---
    courses_for_teacher = collections.defaultdict(list)
    courses_for_room = collections.defaultdict(list)
    
    for c_id, details in theory.items():
        room = details[0]
        t_id = details[3]
        courses_for_room[room].append(c_id)
        courses_for_teacher[t_id].append(c_id)

    # --- Variables ---
    shifts = {}
    for c_id in theory.keys():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                shifts[(c_id, d, s)] = model.NewBoolVar(f'c{c_id}_d{d}_s{s}')

    # --- Hard Constraints (The Rules) ---

    # 1. Hours per week
    for c_id, details in theory.items():
        model.Add(sum(shifts[(c_id, d, s)] for d in range(len(DAYS)) for s in range(len(SLOTS))) == details[2])

    # 2. Lunch Break
    for c_id in theory.keys():
        for d in range(len(DAYS)):
            model.Add(shifts[(c_id, d, LUNCH_SLOT_INDEX)] == 0)

    # 3. Conflicts
    for t_id, course_ids in courses_for_teacher.items():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                if s == LUNCH_SLOT_INDEX: continue
                model.Add(sum(shifts[(c_id, d, s)] for c_id in course_ids) <= 1)

    for r_name, course_ids in courses_for_room.items():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                if s == LUNCH_SLOT_INDEX: continue
                model.Add(sum(shifts[(c_id, d, s)] for c_id in course_ids) <= 1)


    # --- Soft Constraints (The Quality Improvements) ---
    # We create a list of penalty terms to Minimize.
    objective_terms = []

    # A. Afternoon Penalty (Keep existing preference for morning)
    for c_id in theory.keys():
        for d in range(len(DAYS)):
            for s_idx, slot in enumerate(SLOTS):
                if s_idx > LUNCH_SLOT_INDEX:
                    weight = (s_idx - LUNCH_SLOT_INDEX) * 2 # Base cost
                    objective_terms.append(shifts[(c_id, d, s_idx)] * weight)

    # B. Vertical Randomness (Course Balance)
    # Penalty: If Course X is in S1 on Mon, try NOT to put it in S1 on Tue
    # for c_id in theory.keys():
    #     for s_idx in range(len(SLOTS)):
    #         # Count how many times this course uses this slot across the week
    #         slot_usage = [shifts[(c_id, d, s_idx)] for d in range(len(DAYS))]
            
    #         # We want to minimize (sum)^2 to punish peaks
    #         # Since CP-SAT handles booleans, we can create an integer sum var
    #         usage_sum = model.NewIntVar(0, 5, f'usage_c{c_id}_s{s_idx}')
    #         model.Add(usage_sum == sum(slot_usage))
            
    #         # Penalize: 1 time = ok, 2 times = bad, 3 times = very bad
    #         # We add usage_sum * scaling_factor to objective
    #         # A simple way is to penalize if usage > 1
    #         model.Add(usage_sum <= 1).OnlyEnforceIf(model.NewBoolVar(f'limit_c{c_id}_s{s_idx}'))
    #         # For objective, let's just add the sum squared essentially
    #         # (In CP-SAT linear objectives, we can approximate by weighting)
    #         # Simpler approach: Add usage_sum * 10. If usage is 2, cost is 20. 
    #         # Ideally we want non-linear, but let's stick to linear weights for speed
    #         # Better trick: Create a variable that is 1 if usage > 1
    #         is_repeated = model.NewBoolVar(f'rep_c{c_id}_s{s_idx}')
    #         model.Add(usage_sum > 1).OnlyEnforceIf(is_repeated)
    #         model.Add(usage_sum <= 1).OnlyEnforceIf(is_repeated.Not())
    #         objective_terms.append(is_repeated * 50) # High penalty for repetition

    # # C. Teacher Slot Spread (Teacher Work Balance)
    # # Penalty: If Teacher X has a class in S1 on Mon, try NOT to give S1 on Tue
    # for t_id, course_ids in courses_for_teacher.items():
    #     for s_idx in range(len(SLOTS)):
    #         if s_idx == LUNCH_SLOT_INDEX: continue
            
    #         # Sum of all classes this teacher has in this slot index across the week
    #         # Note: This checks S1 on Mon, S1 on Tue, etc.
    #         teacher_slot_vars = []
    #         for c_id in course_ids:
    #             for d in range(len(DAYS)):
    #                 teacher_slot_vars.append(shifts[(c_id, d, s_idx)])
            
    #         t_usage_sum = model.NewIntVar(0, 5, f'tus_t{t_id}_s{s_idx}')
    #         model.Add(t_usage_sum == sum(teacher_slot_vars))
            
    #         # Penalize repetition heavily
    #         t_is_repeated = model.NewBoolVar(f'trep_t{t_id}_s{s_idx}')
    #         model.Add(t_usage_sum > 1).OnlyEnforceIf(t_is_repeated)
    #         model.Add(t_usage_sum <= 1).OnlyEnforceIf(t_is_repeated.Not())
    #         objective_terms.append(t_is_repeated * 100) # Very High penalty

    # # D. Clustering & Day Balancing (Minimize Gaps & Empty Days)
    # # 1. Compactness (Gap Penalty): S1 should be filled before S2
    # # We penalize: (Slot S_k is Empty) AND (Slot S_{k+1} is Full)
    # for r_name, course_ids in courses_for_room.items():
    #     for d in range(len(DAYS)):
    #         for s_idx in range(len(SLOTS) - 1):
    #             if s_idx == LUNCH_SLOT_INDEX or s_idx+1 == LUNCH_SLOT_INDEX: continue
                
    #             # Is slot k active?
    #             is_s_active = model.NewBoolVar(f'active_r{r_name}_d{d}_s{s_idx}')
    #             model.Add(sum(shifts[(c, d, s_idx)] for c in course_ids) >= 1).OnlyEnforceIf(is_s_active)
    #             model.Add(sum(shifts[(c, d, s_idx)] for c in course_ids) == 0).OnlyEnforceIf(is_s_active.Not())
                
    #             # Is slot k+1 active?
    #             is_next_active = model.NewBoolVar(f'active_r{r_name}_d{d}_s{s_idx+1}')
    #             model.Add(sum(shifts[(c, d, s_idx+1)] for c in course_ids) >= 1).OnlyEnforceIf(is_next_active)
    #             model.Add(sum(shifts[(c, d, s_idx+1)] for c in course_ids) == 0).OnlyEnforceIf(is_next_active.Not())

    #             # Bad State: Empty followed by Active (Gap or Late Start)
    #             is_gap = model.NewBoolVar(f'gap_r{r_name}_d{d}_s{s_idx}')
    #             # gap is true if s_active is FALSE and next_active is TRUE
    #             model.AddBoolAnd([is_s_active.Not(), is_next_active]).OnlyEnforceIf(is_gap)
    #             model.AddBoolOr([is_s_active, is_next_active.Not()]).OnlyEnforceIf(is_gap.Not())
                
    #             objective_terms.append(is_gap * 20) # Medium penalty for gaps

    # 2. Day Load Balance (Fill Mon/Wed if Fri is full)
    # We calculate the load for each day and punish (Load^2).
    # This mathematically forces an even spread (2,2,2,2,2) vs (0,0,0,5,5).
    # for r_name, course_ids in courses_for_room.items():
    #     for d in range(len(DAYS)):
    #         daily_load = model.NewIntVar(0, 8, f'load_r{r_name}_d{d}')
    #         model.Add(daily_load == sum(shifts[(c, d, s)] for c in course_ids for s in range(len(SLOTS))))
            
            # To minimize Load^2, we can't do direct quadratic in linear solver easily without helpers.
            # But we can approximate by adding "Cost per unit".
            # If load > 2, add penalty. If load > 4, add huge penalty.
            
            # Simple Linear trick: Just weight earlier days slightly less?
            # No, user wants balancing.
            # Let's add a soft constraint: Try to match Average Load (approx 3-4 classes)
            # Absolute difference from 3?
            
            # Actually, simply adding the Gap penalty above usually fixes the "Late Week Clustering"
            # because gaps on Monday (S1, S2 empty) will be penalized.
            # pass

    # --- Solve ---
    model.Minimize(sum(objective_terms))
    
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 30 # Increased time for complex optimization
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Solution Found! Status: {solver.StatusName(status)}")
        
        filename = "timetables/college_timetable_final_4.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            header = ['Room', 'Day'] + SLOTS
            writer.writerow(header)
            
            sorted_rooms = sorted(courses_for_room.keys())
            for room in sorted_rooms:
                for d_idx, day in enumerate(DAYS):
                    row_data = [room, day]
                    for s_idx, slot in enumerate(SLOTS):
                        if s_idx == LUNCH_SLOT_INDEX:
                            row_data.append("--- LUNCH ---")
                            continue

                        cell_text = ""
                        for c_id in courses_for_room[room]:
                            if solver.Value(shifts[(c_id, d_idx, s_idx)]):
                                subj = theory[c_id][1]
                                t_name = teachers[theory[c_id][3]][0]
                                cell_text = f"{subj} ({t_name})"
                                break
                        row_data.append(cell_text)
                    writer.writerow(row_data)
                writer.writerow([]) 

        print(f"Exported to {filename}")
    else:
        print("No solution found. Constraints might be too conflicting.")

if __name__ == '__main__':
    main()