# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

my_str = "Это абворожительный код, не абвобременен формулами математики абв абвтест абвтест"
find = 'абв'

print("Исходный текст = ", my_str)
my_list = my_str.split(' ')
out_list = my_list.copy()
for elem in my_list:
    if find in elem:
        out_list.remove(elem)
print("Измененный текст = ", out_list)
