import data
import collections

# def check_for_same_room(data):
#     used_rooms = []
#     for i in data.values():
#         if i[3] in used_rooms:
#             print(f"Same room {i[3]} is used for 2 classes please check")
#             continue
#         else:
#             used_rooms.append(i[3])
#     else:
#         print(used_rooms)

# if __name__ == '__main__':
#     check_for_same_room(data.batches)
        

# teachers = data.teachers
# theory = data.theory
# DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# SLOTS = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']


# shifts = {}
# for c_id in theory.keys():
#     for d in range(len(DAYS)):
#         for s in range(len(SLOTS)):
#             shifts[(c_id, d, s)] = f'c{c_id}_d{d}_s{s}'

# print(len(shifts))

# courses_for_teacher = collections.defaultdict(list)
# courses_for_room = collections.defaultdict(list)

# for c_id, details in theory.items():
#     room = details[0]
#     t_id = details[3]
#     courses_for_room[room].append(c_id)
#     courses_for_teacher[t_id].append(c_id)

# print(courses_for_room)
# print(courses_for_teacher)

# for c_id, details in theory.items():
#         for d in range(len(DAYS)):
#             for s in range(len(SLOTS)):
#                 print(shifts[(c_id, d, s)])



for i,j in data.diploma_theroy.items():
    print(f"{i} : [[{j[0]}], '{j[1]}', {j[2]}, [{j[3]}]],")