def menu():
    print("Открыли меню")


def change_data():
    pass


def write_data():
    pass


def read_data():
    with open('contacts.txt', 'r', encoding='utf-8') as file:
        my_list = list(file.readlines())
        return my_list


def screen():
    pass


def main():
    read_data()
    print("Прочитали данные")
    menu()
    print("Запустили меню")


if __name__ == '__main__':
    main()
