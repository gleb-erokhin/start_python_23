# Задайте список из n чисел
# #последовательности (1 + 1 / n) ** n и
# #выведите на экран их сумму.

n = int(input("Enter munber: "))
summ = 0
for i in range(1, n + 1):
    summ = summ + ((1 + (1 / i)) ** i)
    print(f"i => {i}, sum => {summ}")  # for testing
print(summ)
