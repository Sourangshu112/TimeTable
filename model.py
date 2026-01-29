from ortools.sat.python import cp_model
import collections
import csv
import data

# --- 1. SETUP & CONSTANTS ---
print("Started initialising... ")

DAYS = data.DAYS
BTECH_SLOTS = data.BTECHSLOTS
DIPLOMA_SLOTS = data.DIPLOMASLOTS
LUNCH_SLOT_BTECH = data.LUNCH_SLOT_BTECH 
LUNCH_SLOT_DIPLOMA = data.LUNCH_SLOT_DIPLOMA
teachers_db = data.teachers
batches_db = data.batches
rooms_mapped = data.rooms_mapped

# --- 2. PRE-PROCESSING ---

all_theory = {}
all_practical = {}

def process_theory(source, c_type):
    for c_id, details in source.items():
        all_theory[c_id] = {
            'type': c_type,
            'rooms': details[0],
            'subject': details[1],
            'hours': details[2],
            'teachers': list(set(details[3])),
            'raw_teachers': details[3]
        }

process_theory(data.diploma_theroy, 'diploma')
process_theory(data.btech_theory, 'btech')

def process_practical(source, c_type):
    for p_id, details in source.items():
        batch_ids = details[0]
        teacher_groups = details[1]
        lab_id = details[2]
        subject = details[3]
        hours_list = details[4]

        # SPLIT BATCHES LOGIC
        for i, b_id in enumerate(batch_ids):
            unique_task_id = f"{p_id}_{b_id}"
            
            if i < len(teacher_groups):
                assigned_teachers = teacher_groups[i]
            else:
                assigned_teachers = [] 

            all_practical[unique_task_id] = {
                'type': c_type,
                'batches': [b_id],
                'all_teachers': assigned_teachers,
                'lab_id': lab_id,
                'subject': subject,
                'sessions': hours_list,
                'original_id': p_id
            }

process_practical(data.diploma_practical, 'diploma')
process_practical(data.btech_practical, 'btech')

def get_slot_len(c_type):
    return len(BTECH_SLOTS) if c_type == 'btech' else len(DIPLOMA_SLOTS)

def get_lunch_idx(c_type):
    return LUNCH_SLOT_BTECH if c_type == 'btech' else LUNCH_SLOT_DIPLOMA

def main():
    model = cp_model.CpModel()

    # --- 3. VARIABLES ---
    
    # Theory
    t_shifts = {}
    for c_id, info in all_theory.items():
        s_len = get_slot_len(info['type'])
        for d in range(len(DAYS)):
            for s in range(s_len):
                t_shifts[(c_id, d, s)] = model.NewBoolVar(f't{c_id}_d{d}_s{s}')

    # Practical
    p_starts = {}
    for u_id, info in all_practical.items():
        s_len = get_slot_len(info['type'])
        lunch_idx = get_lunch_idx(info['type'])
        sessions = info['sessions']
        
        for sess_idx, duration in enumerate(sessions):
            for d in range(len(DAYS)):
                possible_starts = s_len - duration + 1
                for s in range(possible_starts):
                    # Check Lunch overlap
                    block_indices = [s + k for k in range(duration)]
                    
                    # 1. Overlap Check: Cannot cover Lunch
                    if lunch_idx in block_indices:
                        continue
                    
                    # 2. DIPLOMA SPECIFIC: Cannot cover S1 (Index 0)
                    # Since practicals are continuous, if s=0, it covers index 0.
                    # So practical cannot start at 0.
                    if info['type'] == 'diploma' and 0 in block_indices:
                        continue

                    p_starts[(u_id, sess_idx, d, s)] = model.NewBoolVar(f'p{u_id}_sess{sess_idx}_d{d}_s{s}')


    # --- 4. RESOURCE MAPPING ---
    teacher_busy = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    room_busy = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))
    batch_busy = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))

    # A. Theory Mapping
    for c_id, info in all_theory.items():
        s_len = get_slot_len(info['type'])
        for d in range(len(DAYS)):
            for s in range(s_len):
                var = t_shifts[(c_id, d, s)]
                
                for t_id in info['teachers']:
                    teacher_busy[t_id][d][s].append(var)
                
                for r_name in info['rooms']:
                    room_busy[r_name][d][s].append(var)
                    if r_name in rooms_mapped:
                        for b_id in rooms_mapped[r_name]:
                            batch_busy[b_id][d][s].append(var)

    # B. Practical Mapping
    for u_id, info in all_practical.items():
        sessions = info['sessions']
        for sess_idx, duration in enumerate(sessions):
            s_len = get_slot_len(info['type'])
            for d in range(len(DAYS)):
                for s_start in range(s_len):
                    if (u_id, sess_idx, d, s_start) not in p_starts: continue
                    
                    start_var = p_starts[(u_id, sess_idx, d, s_start)]
                    
                    for k in range(duration):
                        current_s = s_start + k
                        
                        # Teachers
                        for t_id in info['all_teachers']:
                            teacher_busy[t_id][d][current_s].append(start_var)
                        
                        # Lab Room
                        if info['lab_id'] != 0:
                            room_busy[info['lab_id']][d][current_s].append(start_var)
                        
                        # Batches
                        for b_id in info['batches']:
                            batch_busy[b_id][d][current_s].append(start_var)

    # --- 5. HARD CONSTRAINTS ---

    # A. Theory
    for c_id, info in all_theory.items():
        s_len = get_slot_len(info['type'])
        lunch_idx = get_lunch_idx(info['type'])

        model.Add(sum(t_shifts[(c_id, d, s)] for d in range(len(DAYS)) for s in range(s_len)) == info['hours'])
        
        for d in range(len(DAYS)):
            # 1. Force Lunch to 0
            model.Add(t_shifts[(c_id, d, lunch_idx)] == 0)
            
            # 2. DIPLOMA SPECIFIC: Force S1 (Index 0) to 0
            if info['type'] == 'diploma':
                model.Add(t_shifts[(c_id, d, 0)] == 0)

            # 3. Max 1 class per day
            model.Add(sum(t_shifts[(c_id, d, s)] for s in range(s_len)) <= 1)

    # B. Practical
    for u_id, info in all_practical.items():
        sessions = info['sessions']
        s_len = get_slot_len(info['type'])
        
        # Exact occurrences
        for sess_idx in range(len(sessions)):
            all_vars = [p_starts[(u_id, sess_idx, d, s)] for d in range(len(DAYS)) for s in range(s_len) if (u_id, sess_idx, d, s) in p_starts]
            model.Add(sum(all_vars) == 1)

        # Different days
        if len(sessions) > 1:
            for d in range(len(DAYS)):
                daily_starts = []
                for sess_idx in range(len(sessions)):
                    for s in range(s_len):
                        if (u_id, sess_idx, d, s) in p_starts:
                            daily_starts.append(p_starts[(u_id, sess_idx, d, s)])
                model.Add(sum(daily_starts) <= 1)

    # C. Global Conflicts (REMOVED LUNCH FILTER)
    # We iterate ALL slots. Constraints on variables (forced to 0 at lunch) handle the safety.
    
    for t_id in teacher_busy:
        for d in teacher_busy[t_id]:
            for s in teacher_busy[t_id][d]:
                # Check conflict for EVERY slot
                model.Add(sum(teacher_busy[t_id][d][s]) <= 1)

    for r_id in room_busy:
        for d in room_busy[r_id]:
            for s in room_busy[r_id][d]:
                model.Add(sum(room_busy[r_id][d][s]) <= 1)

    for b_id in batch_busy:
        for d in batch_busy[b_id]:
            for s in batch_busy[b_id][d]:
                model.Add(sum(batch_busy[b_id][d][s]) <= 1)


    # --- 6. SOFT CONSTRAINTS ---
    objective_terms = []

    # Theory: Morning
    for c_id, info in all_theory.items():
        s_len = get_slot_len(info['type'])
        lunch_idx = get_lunch_idx(info['type'])
        for d in range(len(DAYS)):
            for s in range(s_len):
                if s > lunch_idx:
                    objective_terms.append(t_shifts[(c_id, d, s)] * (s - lunch_idx) * 10)

    # Practical: Early Afternoon
    for u_id, info in all_practical.items():
        sessions = info['sessions']
        lunch_idx = get_lunch_idx(info['type'])
        s_len = get_slot_len(info['type'])
        
        for sess_idx, duration in enumerate(sessions):
            for d in range(len(DAYS)):
                for s_start in range(s_len):
                    if (u_id, sess_idx, d, s_start) not in p_starts: continue
                    var = p_starts[(u_id, sess_idx, d, s_start)]
                    
                    if s_start < lunch_idx:
                        objective_terms.append(var * 1000)
                    else:
                        lateness = s_start - (lunch_idx + 1)
                        objective_terms.append(var * lateness * 20)
    # --- VERTICAL RANDOMNESS ---
    for c_id, info in all_theory.items():
        s_len = get_slot_len(info['type'])
        c_lunch_idx = get_lunch_idx(info['type'])
        
        for s in range(s_len):
            if s == c_lunch_idx: continue # Skip specific lunch
            
            # Compare every day against every other day
            for d1 in range(len(DAYS)):
                for d2 in range(d1 + 1, len(DAYS)):
                    
                    is_duplicate = model.NewBoolVar(f'dup_{c_id}_s{s}_{d1}_{d2}')
                    
                    model.AddBoolAnd([
                        t_shifts[(c_id, d1, s)], 
                        t_shifts[(c_id, d2, s)]
                    ]).OnlyEnforceIf(is_duplicate)
                    
                    model.AddBoolOr([
                        t_shifts[(c_id, d1, s)].Not(), 
                        t_shifts[(c_id, d2, s)].Not()
                    ]).OnlyEnforceIf(is_duplicate.Not())
                    
                    objective_terms.append(is_duplicate * 50)

    model.Minimize(sum(objective_terms))

    # --- 7. SOLVE ---
    print("Solving Model...")
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 300
    status = solver.Solve(model)

    if status in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        print(f"Solution Found! Status: {solver.StatusName(status)}")
        
        filename = "timetable.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            header = ['Batch ID', 'Batch Name', 'Day'] + BTECH_SLOTS
            writer.writerow(header)

            for b_id in sorted(batches_db.keys()):
                b_info = batches_db[b_id]
                b_type = b_info[0] # 'btech' or 'diploma'
                b_lunch_idx = get_lunch_idx(b_type)
                b_name = f"{b_type}-{b_info[2]}-{b_info[1]}-{b_info[3]}"

                for d_idx, day in enumerate(DAYS):
                    row = [b_id, b_name, day]
                    for s_idx in range(len(BTECH_SLOTS)):
                        
                        # Specific Lunch Text
                        if s_idx == b_lunch_idx:
                            row.append("--- LUNCH ---")
                            continue
                        
                        # Diploma S1 Empty
                        if b_type == 'diploma' and s_idx == 0:
                            row.append("--- OFF ---")
                            continue

                        cell_text = ""
                        # Theory
                        for r, batches in rooms_mapped.items():
                            if b_id in batches:
                                for c_id, info in all_theory.items():
                                    if r in info['rooms'] and s_idx < get_slot_len(info['type']):
                                        if solver.Value(t_shifts[(c_id, d_idx, s_idx)]):
                                            try:
                                                r_idx = info['rooms'].index(r)
                                                t_name = teachers_db[info['raw_teachers'][r_idx]][0]
                                            except: t_name = "?"
                                            cell_text = f"[T] {info['subject']} ({t_name})"
                        
                        # Practical
                        if cell_text == "":
                            for u_id, info in all_practical.items():
                                if b_id in info['batches']:
                                    sessions = info['sessions']
                                    for sess_idx, duration in enumerate(sessions):
                                        s_len = get_slot_len(info['type'])
                                        for s_start in range(s_len):
                                            if (u_id, sess_idx, d_idx, s_start) in p_starts:
                                                if solver.Value(p_starts[(u_id, sess_idx, d_idx, s_start)]):
                                                    if s_start <= s_idx < s_start + duration:
                                                        t_str = ",".join([teachers_db[t][0] for t in info['all_teachers']])
                                                        cell_text = f"[L:{info['lab_id']}] {info['subject']} ({t_str})"
                        
                        row.append(cell_text)
                    writer.writerow(row)
                writer.writerow([])
        print(f"Exported to {filename}")
    else:
        print("No solution found.")

if __name__ == '__main__':
    main()