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
        

teachers = data.teachers
theory = data.theory

courses_for_teacher = collections.defaultdict(list)
courses_for_room = collections.defaultdict(list)
print(courses_for_teacher)
print(courses_for_room)