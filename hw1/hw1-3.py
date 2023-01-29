# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

number_of_section = int(input("Enter number of section: "))

if number_of_section == 1:
    print("X from 0 to infinity, Y from 0 to infinity")
elif number_of_section == 2:
    print("X from 0 to minus infinity, Y from 0 to infinity")
elif number_of_section == 3:
    print("X from 0 to minus infinity, Y from 0 to minus infinity")
elif number_of_section == 4:
    print("X from 0 to infinity, Y from 0 to minus infinity")
else:
    print("There is only four sections!, Try again!")
