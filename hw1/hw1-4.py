# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

distance_xa = int(input("Enter coordinate Ax: "))
distance_ya = int(input("Enter coordinate Ay: "))
distance_xb = int(input("Enter coordinate Bx: "))
distance_yb = int(input("Enter coordinate By: "))
distance = ((distance_xb - distance_xa) ** 2 +
            (distance_yb - distance_ya) ** 2) ** 0.5
print(round(distance, 3))
