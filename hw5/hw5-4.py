# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

# функция кодирования строки
def rle_code(code_str):
    count = 0
    curent = code_str[0]
    outputs = []
    if len(code_str) == 0:  # проверка на пустую строку
        print("Строка пустая")
    else:
        # основной код, за старт берем первый индекс, после чего увеличиваем счетчик,
        # и сравниваем сколько одинаковых значений
        for i in range(len(code_str)):
            if code_str[i] == curent:
                count += 1
            # как только нашли разницу, заносим в список картежем
            # обновляем новое значение подстроки и изменяем значение счетчика
            else:
                outputs.append((count, curent))
                curent = code_str[i]
                count = 1
            # проверка последних элементов на основе индекса, и добавление в список
            if i == (len(code_str) - 1):
                outputs.append((count, curent))
        return outputs


# функция декодирования, получаем список картежей на вход, проходимся по списку в цикле
def rle_decode(decod_list):
    out = ""
    for el in decod_list:
        out = out + (el[0] * el[1])
    # складываем конкатенацией строку и показываем расшифрованную строку
    print("Расшифровано: ", out)


# функция для печати зашифрованной последовательности строки
def print_out(to_print):
    out = ""
    for el in to_print:
        out = out + (str(el[0]) + el[1])
    print("Зашифровано: ", out)


input_str = "aaabbcccaaadcc"

print("Исходный текст: ", input_str)
code = rle_code(input_str)
print_out(code)
rle_decode(code)
