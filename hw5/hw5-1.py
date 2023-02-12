# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

my_str = "Это абворожительный код, не абвобременен формулами математики абв"
find = 'абв'

my_list = my_str.split(' ')
for elem in my_list:
    if find in elem:
        my_list.remove(elem)
print(my_list)
