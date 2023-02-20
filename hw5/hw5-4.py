# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

my_str = "aaabbcccaaa"
my_list = list(my_str)
my_set = set(my_str)
count = 0
curent = my_str[0]
if len(my_str) == 0:
    print("Строка пустая")
else:
    for el in my_str:
        print(my_str[i], end=" ")
        if my_str[i] == my_str[i + 1]:
            count += 1
        print(count)
new_list = []

print(my_str)
for i in range(len(my_list) - 1):
    if my_list[i] == my_list[i + 1]:
        new_list.append(my_list[i])
    count += 1
print(new_list, count)


# def rle(src):
#     result = []
#     current = src[0]
#     counter = 0
#     for e in src:
#         if e == current:
#             counter += 1
#         else:
#             result.append((counter, current))
#             current = e
#             counter = 1
#     return result


# string = 'aaabbbtttggghhhavvv'

# print(rle(string))
