# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

my_str = "aaabbcccaaa"
my_list = list(my_str)
new_list = []
count = 0
print(my_list)
for i in range(len(my_list) - 1):
    if my_list[i] == my_list[i + 1]:
        count += 1
        new_list.append(my_list[i])
print(new_list)
