from ortools.sat.python import cp_model
import collections
import data

# --- 1. DATA INPUT ---
teachers = data.teachers
theory = data.theory

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
SLOTS = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
LUNCH_SLOT_INDEX = 4 # Index 4 corresponds to S5 (0-based index)

def main():
    model = cp_model.CpModel()

    # --- 2. PRE-PROCESS MAPPING ---
    # We need to know which courses belong to which Room and which Teacher
    courses_for_teacher = collections.defaultdict(list)
    courses_for_room = collections.defaultdict(list)
    
    for c_id, details in theory.items():
        room = details[0]
        t_id = details[3]
        
        courses_for_room[room].append(c_id)
        courses_for_teacher[t_id].append(c_id)

    # --- 3. CREATE VARIABLES ---
    # shifts[(course_id, day_index, slot_index)] -> True/False
    shifts = {}
    for c_id in theory.keys():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                shifts[(c_id, d, s)] = model.NewBoolVar(f'c{c_id}_d{d}_s{s}')

    # --- 4. ADD CONSTRAINTS ---

    # A. Hour Constraints & Lunch Constraint
    for c_id, details in theory.items():
        hours_needed = details[2]
        
        # 1. Total hours per week must match
        model.Add(
            sum(shifts[(c_id, d, s)] 
                for d in range(len(DAYS)) 
                for s in range(len(SLOTS))) == hours_needed
        )

        # 2. LUNCH BREAK: No classes allowed in S5 (Index 4)
        for d in range(len(DAYS)):
            model.Add(shifts[(c_id, d, LUNCH_SLOT_INDEX)] == 0)

        # 3. OPTIONAL: Max 1 hour per day per subject (Spread the classes)
        # Uncomment below if you want to force classes to be on different days
        # for d in range(len(DAYS)):
        #     model.Add(sum(shifts[(c_id, d, s)] for s in range(len(SLOTS))) <= 1)

    # B. Teacher Conflict
    # A teacher cannot teach more than 1 class in the same slot
    for t_id, course_ids in courses_for_teacher.items():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                if s == LUNCH_SLOT_INDEX: continue # Skip lunch check (already 0)
                model.Add(
                    sum(shifts[(c_id, d, s)] for c_id in course_ids) <= 1
                )

    # C. Room Conflict
    # A Room (which represents a Batch Group) cannot have more than 1 class in the same slot
    for r_name, course_ids in courses_for_room.items():
        for d in range(len(DAYS)):
            for s in range(len(SLOTS)):
                if s == LUNCH_SLOT_INDEX: continue
                model.Add(
                    sum(shifts[(c_id, d, s)] for c_id in course_ids) <= 1
                )

    # --- 5. SOLVE ---
    solver = cp_model.CpSolver()
    # solver.parameters.max_time_in_seconds = 10 # Optional time limit
    status = solver.Solve(model)

    # ... (rest of your code above) ...

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        print(f"Solution Found! Status: {solver.StatusName(status)}")
        
        import csv
        
        # We will create a CSV file that opens in Excel
        filename = "college_timetable.csv"
        
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # 1. Write the Main Header
            # Columns: Room, Day, S1, S2, ..., S8
            header = ['Room', 'Day'] + SLOTS
            writer.writerow(header)
            
            sorted_rooms = sorted(courses_for_room.keys())
            
            for room in sorted_rooms:
                # We iterate through days to build rows
                for d_idx, day in enumerate(DAYS):
                    row_data = [room, day]
                    
                    for s_idx, slot in enumerate(SLOTS):
                        # Handle Fixed Lunch Slot
                        if s_idx == LUNCH_SLOT_INDEX:
                            row_data.append("--- LUNCH ---")
                            continue

                        # Search for the assigned course in this slot
                        cell_text = ""
                        found = False
                        for c_id in courses_for_room[room]:
                            if solver.Value(shifts[(c_id, d_idx, s_idx)]):
                                # Get details
                                subj_name = theory[c_id][1]
                                t_id = theory[c_id][3]
                                t_name = teachers[t_id][0]
                                
                                # Format: "Subject Name (Prof. Name)"
                                cell_text = f"{subj_name} ({t_name})"
                                found = True
                                break
                        
                        row_data.append(cell_text)
                    
                    # Write the full row to CSV
                    writer.writerow(row_data)
                
                # Add an empty row between rooms for better readability in Excel
                writer.writerow([]) 

        print(f"\nSuccessfully exported timetable to '{filename}'")
        print("You can open this file in Excel or Google Sheets.")

    else:
        print("No solution found. Likely conflicts:")
        print("1. A room might need more hours than available slots (35 teaching slots/week).")
        print("2. A teacher might be overloaded in a specific overlap.")

if __name__ == '__main__':
    main()