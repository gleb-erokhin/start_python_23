list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_min = int(input("min"))
list_max = int(input("max"))
for i in range(len(list_1)):
    if list_min <= list_1[i] <= list_max:
        print(i)
