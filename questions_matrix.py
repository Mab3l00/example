# Question 1
# list1 = [[1, 2, 3, 4, 5],
#          [6, 7, 8, 9, 10],
#          [11, 12, 13, 14, 15],
#          [16, 17, 18, 19, 20],
#          [21, 22, 23, 24, 25]]
# for row in range(len(list1)):
#     for number in range(len(list1[row])):
#         print(list1[row][number], end= " ")
#     print()

# question 2
# matrix = [[1, 2, 3, 4, 5],
#          [6, 7, 8, 9, 10],
#          [11, 12, 13, 14, 15],
#          [16, 17, 18, 19, 20],
#          [21, 22, 23, 24, 25]]
#
# for row in range(len(matrix)):
#     print(sum(matrix[row]))

# question 3
# matrix = [[1, 2, 3, 4, 5],
#          [6, 7, 8, 9, 10],
#          [11, 12, 13, 14, 15],
#          [16, 17, 18, 19, 20],
#          [21, 22, 23, 24, 25]]
# i = 0
# summary = []
# for row in range(len(matrix)):
#     summary.append(matrix[row][i])
#     print(matrix[row][i])
#     i +=1
# print()
# print(sum(summary))

# question 4
# import numpy
# from numpy import *
#
#
# matrix = random.randint(1,10,(3,3))
# print(matrix)
# print()
# matrix2 = matrix.transpose()
# print(matrix2)

# question 5
# matrix = [[1, 2, 3, 4, 5],
#          [6, 7, 8, 9, 10],
#          [11, 12, 13, 14, 15],
#          [16, 17, 18, 19, 20],
#          [21, 22, 23, 24, 25]]
# new = []
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         new.append(matrix[row])
#     else:
#         new.append(matrix[row][::-1])
# for row in range(len(new)):
#     for collumn in range(len(new[row])):
#         print(new[row][collumn],end= " ")
#     print()

# question 6
# guests = []
# vip = ["Ofir", "Bar", "Neta"]
# family = ["Aviram", "Ohad"]
# friends = ["Moti", "Liron", "Roni"]
# guests.append(vip)
# guests.append(family)
# guests.append(friends)
# for row in range(len(guests)):
#     for name in range(len(guests[row])):
#         print(guests[row][name], end=" ")
#     print()
# removed = str(input("Who is not coming to the party from the VIP's? "))
# vip.remove(removed)
# new_guest = str(input("Who would you like to invite? "))
# friends.append(new_guest)
# print(guests)

#question 7
# matrix  = []
# rows_collums = int(input("Enter a number to create a matrix: "))
# numbers_left = [x for x in range(1,(rows_collums*rows_collums)+1)]
# print(numbers_left)
# for row in range(rows_collums):
#     x = []
#     for colm in range(rows_collums):
#         x.append((row*rows_collums)+colm+1)
#     matrix.append(x[0:rows_collums])
# print(matrix)
#
# for row in range(len(matrix)):
#     for collum in range(len(matrix[row])):
#         print(matrix[row][collum], end=" ")
#     print()
# rotated = list(list(x)[::-1] for x in zip(*matrix))
# print("Reversed")
# for row in range(len(rotated)):
#     for collum in range(len(rotated[row])):
#         print(rotated[row][collum], end=" ")
#     print()

#question 8
# matrix = []
# length = int(input("Length of matrix: "))
# for list1 in range(length):
#     matrix.append([])
# print(matrix)
#
# for list0 in range(len(matrix)):
#     for number in range(length):
#         subsraction = list0 - number
#         if subsraction <= 0:
#             matrix[list0].append(0)
#         else:
#             matrix[list0].append(subsraction)
# for row in range(len(matrix)):
#     for collum in range(len(matrix[row])):
#         print(matrix[row][collum], end=" ")
#     print()

#question 9
# WORKING_SCREEN = "work"
# FAULTY_SCREEN = "problem"
# tv = [
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, FAULTY_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN]
# ]
#
# matrix = []
# for tellevision in range(len(tv)):
#     for broken in range(len(tv[tellevision])):
#         messed_up = []
#         if tv[tellevision][broken] == FAULTY_SCREEN:
#             messed_up.append(tellevision)
#             messed_up.append(broken)
#         else:
#             continue
#         matrix.append(messed_up)
# print(matrix)

#question 10
# restaurant_layout = [
#     [4, 2, 6, 3],
#     [8, 3, 2, 5],
#     [5, 7, 3, 6],
#     [9, 4, 2, 8]
# ]
# reservations = [
#     ["Group A", 3],
#     ["Group B", 6],
#     ["Group C", 2],
#     ["Group D", 7],
#     ["Group E", 5],
#     ["Group F", 4],
#     ["Group G", 8],
#     ["Group H", 3],
#     ["Group I", 9],
#     ["Group J", 6]]
#
# sitting = [["Empty "] * len(restaurant_layout) for i in range(len(restaurant_layout))]
# added = []
# for reservation in range(len(reservations)):
#     for row in range(len(sitting)):
#         for seat in range(len(sitting[row])):
#             if reservations[reservation][1] == restaurant_layout[row][seat]:
#                 if reservations[reservation][0] in added:
#                     continue
#                 else:
#                     sitting[row][seat] = reservations[reservation]
#                     added.append(reservations[reservation][0])
# for row in range(len(sitting)):
#     for colm in range(len(sitting[row])):
#         print(sitting[row][colm], end=" ")
#     print()