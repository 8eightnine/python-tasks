"""Программа для рассчета стоимости n килограммов конфет"""

n = int(input())
if n <= 0:
    print("Ошибка: n не может быть <= 0")
else:
    for i in range(1, 10, 1):
        summa = i * n
        print("Сумма", i, "килограммов конфет =", summa)
