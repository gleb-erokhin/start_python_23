# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = [2, 3, 5, 9, 3, 4, 6]
summ = 0
for i in range(len(my_list)):
    if not i % 2 == 0:
        summ = summ + my_list[i]
print(summ)