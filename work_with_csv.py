import csv
import data

teachers = data.teachers
subjects = data.theory

# with open('Diploma.csv', 'r') as file:
#     reader = csv.reader(file)
#     id = 1
#     for row in reader:
#         if row[5] == "Theory":
#             print(f"{id}: {[row[3],int(row[4])]},")
#             id += 1
#         else:
#             continue


# with open('Diploma.csv','r') as file:
#     reader = csv.reader(file)
#     teacher = []
#     id = 101
#     for row in reader:
#         if row[5] != 'Theory':
#             continue
#         new_teacher = row[6]
#         if new_teacher in teacher:
#             continue
#         print(f"{id} : [{new_teacher},],")
#         id += 1
#         teacher.append(new_teacher)



# with open('Diploma.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if row[5] != 'Theory':
#             continue
#         subject = row[3]
#         teacher = row[6]
#         for id,list in teachers.items():
#             if teacher == list[0]:
#                 for i in subjects.values():
#                     if subject == i[1]:
#                         i.append(id)

# for i in subjects.items():
#     print(f'{i[0]} : {i[1]},')


with open('Diploma.csv', 'r') as file:
    reader = csv.reader(file)
    id = 1
    for row in reader:
        if row[5] == "Practical":
            try:
                print(f"{id}: {[row[3],int(row[4])]},")
            except:
                print(f"{id}: {[row[3],row[4]]},")
            id += 1
        else:
            continue