# Напишите программу, которая принимает на вход число
# N и выдает набор произведений чисел от 1 до N.
# Пример:
# N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

x = int(input("Ведите число: "))
count = 1
factorial = 1
my_list = []

while count <= x:
    factorial = factorial * count
    my_list.append(factorial)
    count += 1

print(my_list)
