def menu():
    print("Открыли меню")


def add_data(my_list):
    pass


def change_data(my_list):
    pass


def write_data():
    pass


def read_data():
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        # my_list = list(file.readlines())
        my_list = list(file.readlines())
        return my_list


def print_data(data):
    for el in data:
        # разделяем по ; и распаковывем список для визуала
        print(*el.strip().split(';'))


def main():
    print("Прочитаем данные")
    my_list = read_data()
    print("Напечататем данные")
    print_data(my_list)
    print("Запустили меню")
    menu()
    print(my_list)


if __name__ == '__main__':
    main()
