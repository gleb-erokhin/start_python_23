# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

my_str = "aaabbcccaaa"
# my_list = list(my_str)
# my_set = set(my_str)
my_str = my_str.split('')

new_list = []
count = 0
print(my_str)
for i in range(len(my_list) - 1):
    if my_list[i] == my_list[i + 1]:
        new_list.append(my_list[i])
    count += 1
print(new_list, count)
