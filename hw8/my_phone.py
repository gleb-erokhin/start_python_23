import csv


def menu(list):
    print("The main menu")
    print("1 - Print all book")
    print("2 - Add record")
    print("3 - Change record")
    print("4 - Exit")
    while True:
        command = int(input("Choose number \n"))
        if command == 1:
            data = read_data()
            print_data(data)
        elif command == 2:
            add_data(list)
        elif command == 3:
            pass  # для изменения записи
        elif command == 4:
            break


def add_data(my_list):
    print("(F I O +7... must be with space)")
    my_list.append(input("Enter data \n").split())
    write_data(my_list)
    menu(my_list)


def change_data(my_list):
    pass


def write_data(my_list):
    with open('contacts.csv', 'w', newline="", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter=",")
        file_writer.writerows(my_list)


def read_data():
    my_list = []
    with open('contacts.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            my_list.append(line)
        return my_list


def print_data(data):
    for el in data:
        # разделяем по ; и распаковывем список для визуала
        print(*el)


def main():
    print("Прочитаем данные")
    my_list = read_data()
    print("Напечататем данные")
    print_data(my_list)
    print("Запустили меню")
    menu(my_list)
    # print(my_list)
    # add_data(my_list)


if __name__ == '__main__':
    main()
