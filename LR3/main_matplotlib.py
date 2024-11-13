import numpy as np
import matplotlib.pyplot as plt


# Функция для вычисления ряда Тейлора для экспоненты
def taylor_exp(x, epsilon):
    term = 1  # начальный член ряда
    sum_ = term
    n = 1
    while abs(term) > epsilon:
        term *= x / n
        sum_ += term
        n += 1
    return sum_


# Основная функция
def plot_functions(x_start, x_end, dx, epsilon, b):
    x_values = np.arange(x_start, x_end, dx)

    # Вычисление значений функций
    y_taylor = np.array([taylor_exp(x, epsilon) for x in x_values])
    y_shifted = y_taylor + b

    # Построение графиков
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_taylor, label='Taylor Series', color='blue')
    plt.plot(x_values, y_shifted, label=f'Taylor Series + {b}', color='red')

    # Настройка графиков
    plt.title('Графики функций')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Ввод данных
x_start = float(input("Введите Xнач: "))
x_end = float(input("Введите Xкон: "))
dx = float(input("Введите шаг dx: "))
epsilon = float(input("Введите точность ε: "))
b = float(input("Введите смещение b: "))

# Вызов функции для построения графиков
plot_functions(x_start, x_end, dx, epsilon, b)
