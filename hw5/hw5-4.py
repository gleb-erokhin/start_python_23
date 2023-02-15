# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

my_str = "aaabbcccaaa"
# my_list = list(my_str)
# my_set = set(my_str)
count = 0
# curent = my_str[0]
if len(my_str) == 0:
    print("Строка пустая")
else:
    for i in range(len(my_str) - 1):
        print(my_str[i], end=" ")
        if my_str[i] == my_str[i + 1]:
            count += 1
        print(count)
# new_list = []

# print(my_str)
# for i in range(len(my_list) - 1):
#     if my_list[i] == my_list[i + 1]:
#         new_list.append(my_list[i])
#     count += 1
# print(new_list, count)


def rle(src):
    result = []
    # допишем букву, отличающуюся от последней в строке
    # src += 'b' if src.endswith('a') else 'a'
    # теперь, заметь, она не пуста и проверка на пустоту не нужна
    current = src[0]
    counter = 0  # тут ошибочка, ты пытался дважды посчитать первую букву
    for e in src:
        if e == current:
            counter += 1
        else:
            result.append((current, counter))
            current = e
            counter = 1
    return result


string = 'aaabbbtttggghhhavaaa'

print(rle(string))
