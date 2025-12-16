from ortools.sat.python import cp_model
import collections
import csv
import data

# --- 1. DATA INPUT ---
teachers = data.teachers
theory = data.theory

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
SLOTS = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
LUNCH_SLOT_INDEX = 4  # S5 is lunch

def main():
    model = cp_model.CpModel()

    # --- Pre-processing ---
    courses_for_teacher = collections.defaultdict(list)
    courses_for_room = collections.defaultdict(list)
    
    for c_id, details in theory.items():
        room = details[0]
        t_id = details[3]
        courses_for_room[room].append(c_id)
        courses_for_teacher[t_id].append(c_id)

    # --- Create Variables ---
    shifts = {}
    for c_id in theory.keys():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                shifts[(c_id, d, s)] = model.NewBoolVar(f'c{c_id}_d{d}_s{s}')

    # --- Hard Constraints ---

    # 1. Total Hours
    for c_id, details in theory.items():
        hours_needed = details[2]
        model.Add(sum(shifts[(c_id, d, s)] 
                      for d in range(len(DAYS)) 
                      for s in range(len(SLOTS))) == hours_needed)

    # 2. Lunch Break (Hard Constraint: No classes in S5)
    for c_id in theory.keys():
        for d in range(len(DAYS)):
            model.Add(shifts[(c_id, d, LUNCH_SLOT_INDEX)] == 0)
    
    # 3. Max 1 hour per day per subject (Spread the classes)
    for d in range(len(DAYS)):
        model.Add(sum(shifts[(c_id, d, s)] for s in range(len(SLOTS))) <= 1)

    # 3. Teacher Conflict
    for t_id, course_ids in courses_for_teacher.items():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                if s == LUNCH_SLOT_INDEX: continue
                model.Add(sum(shifts[(c_id, d, s)] for c_id in course_ids) <= 1)
    

    # 4. Room Conflict
    for r_name, course_ids in courses_for_room.items():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                if s == LUNCH_SLOT_INDEX: continue
                model.Add(sum(shifts[(c_id, d, s)] for c_id in course_ids) <= 1)

    # --- 5. NEW: Soft Constraints (Optimization) ---
    # Goal: Penalize afternoon slots to force classes into the morning.
    
    objective_terms = []
    
    for c_id in theory.keys():
        for d in range(len(DAYS)):
            for s_idx, slot in enumerate(SLOTS):
                
                # Check if this slot is after lunch
                if s_idx > LUNCH_SLOT_INDEX:
                    # Weight logic:
                    # S6 (Index 5) -> Cost 1 (Preferred if overflow is needed)
                    # S7 (Index 6) -> Cost 2 (Avoid)
                    # S8 (Index 7) -> Cost 3 (Strongly Avoid)
                    
                    weight = (s_idx - LUNCH_SLOT_INDEX) 
                    
                    # Add to our "penalty score"
                    objective_terms.append(shifts[(c_id, d, s_idx)] * weight)

    # Tell solver to minimize this penalty score
    model.Minimize(sum(objective_terms))

    # --- Solve ---
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 20 # Give it time to find the BEST balance
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Solution Found! Status: {solver.StatusName(status)}")
        
        filename = "college_timetable_optimized.csv"
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
        print("No solution found. Constraints are too tight.")

if __name__ == '__main__':
    main()