# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая
# ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом"" 29 // sweets

import random

# sweets = 150
# max_sweets_hod = 28
# player1 = 0
# player2 = 0
# player_hod = 0


def chose():  # функция жеребьевки
    print("Выбор первого хода")
    print("Загадайте число от 1 до 10")
    print("Первый ходит у кого число будет больше")
    player_hod = random.randint(0, 1)  # кто ходит
    print(player_hod)
    play()


def play():  # функция для игры
    sweets = 150
    max_sweets_hod = 28
    player1 = 0
    player2 = 0
    player_hod = 0
    bot = True
    while sweets:
        player = int(
            input(f"Ход игрока {player_hod + 1}, Сколько конфет возьмете: "))
        if sweets >= player <= max_sweets_hod:
            sweets = sweets - player
            print("конфет осталось: ", sweets)
            player_hod = 0 if player_hod else 1
        else:
            print("конфет больше 28")

            continue
    print("Выиграл игрок: ", 1 if player_hod else 2)


def main():
    chose()


if __name__ == "__main__":
    main()
