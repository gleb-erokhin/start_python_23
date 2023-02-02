# Задайте список из n чисел
# #последовательности (1 + 1 / n) ** n и
# #выведите на экран их сумму.

n = int(input("Enter munber: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + ((1 + (1 / i)) ** i)
    print(f"i => {i}, sum => {sum}")  # for testing
print(sum)
