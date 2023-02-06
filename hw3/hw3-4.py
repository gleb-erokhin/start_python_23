# Напишите программу, которая будет преобразовывать
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

x = 45
my_list = []
while x > 0:
    y = x % 2
    x = x // 2
    my_list.append(y)
my_list.reverse()
print("С помощью списка")
print(my_list)

x = 45
summ = ""
while x > 0:
    y = x % 2
    x = x // 2
    summ = summ + str(y)
print("С помощью строки")
print(summ[::-1])
