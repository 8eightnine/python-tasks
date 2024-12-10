import numpy as np
import math
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button, StringVar, OptionMenu


def calculate_taylor_series(x, epsilon):
    """Вычисление y(x) через ряд Тейлора с заданной точностью ε."""
    result = 0
    term = 1  # Начальное значение первого члена ряда
    n = 0
    while abs(term) > epsilon:
        term = ((-1)**n) * (x**n) / math.factorial(n)
        result += term
        n += 1
    return result


def plot_functions():
    """Построение графиков функций y(x) и z(x)."""
    # Получение параметров от пользователя
    x_start = float(entry_x_start.get())
    x_end = float(entry_x_end.get())
    dx = float(entry_dx.get())
    epsilon = float(entry_epsilon.get())
    b = float(entry_b.get())

    # Генерация значений x
    x_values = np.arange(x_start, x_end, dx)

    # Вычисление y(x) через ряд Тейлора
    y_values = [calculate_taylor_series(x, epsilon) for x in x_values]

    # Вычисление z(x)
    z_values = np.exp(-x_values) + b

    # Построение графиков
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label="y(x) = Σ((-1)^n * x^n) / n!", 
             color=color_y.get(), linestyle=style_y.get(), marker=marker_y.get())
    plt.plot(x_values, z_values, label=f"z(x) = e^(-x) + {b}", 
             color=color_z.get(), linestyle=style_z.get(), marker=marker_z.get())

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Графики функций y(x) и z(x)")
    plt.legend(loc=legend_position.get())
    plt.grid()

    # Сохранение изображения
    file_name = entry_file_name.get()
    if file_name:
        plt.savefig(file_name)
    plt.show()


# Создание графического интерфейса
root = Tk()
root.title("Построение графиков функций")

# Поля ввода параметров
Label(root, text="Xнач:").grid(row=0, column=0)
entry_x_start = Entry(root)
entry_x_start.grid(row=0, column=1)

Label(root, text="Xкон:").grid(row=1, column=0)
entry_x_end = Entry(root)
entry_x_end.grid(row=1, column=1)

Label(root, text="dx:").grid(row=2, column=0)
entry_dx = Entry(root)
entry_dx.grid(row=2, column=1)

Label(root, text="ε:").grid(row=3, column=0)
entry_epsilon = Entry(root)
entry_epsilon.grid(row=3, column=1)

Label(root, text="b (для z(x)):").grid(row=4, column=0)
entry_b = Entry(root)
entry_b.grid(row=4, column=1)

# Выбор цвета, стиля линии и маркера для графиков
Label(root, text="Цвет y(x):").grid(row=5, column=0)
color_y = StringVar(value="blue")
OptionMenu(root, color_y, "blue", "green", "red", "black").grid(row=5, column=1)

Label(root, text="Цвет z(x):").grid(row=6, column=0)
color_z = StringVar(value="orange")
OptionMenu(root, color_z, "orange", "purple", "cyan", "magenta").grid(row=6, column=1)

Label(root, text="Стиль y(x):").grid(row=7, column=0)
style_y = StringVar(value="-")
OptionMenu(root, style_y, "-", "--", "-.", ":").grid(row=7, column=1)

Label(root, text="Стиль z(x):").grid(row=8, column=0)
style_z = StringVar(value="--")
OptionMenu(root, style_z, "-", "--", "-.", ":").grid(row=8, column=1)

Label(root, text="Маркер y(x):").grid(row=9, column=0)
marker_y = StringVar(value="o")
OptionMenu(root, marker_y, "o", "s", "d", "^", "None").grid(row=9, column=1)

Label(root, text="Маркер z(x):").grid(row=10, column=0)
marker_z = StringVar(value="s")
OptionMenu(root, marker_z, "o", "s", "d", "^", "None").grid(row=10, column=1)

# Выбор расположения легенды
Label(root, text="Расположение легенды:").grid(row=11, column=0)
legend_position = StringVar(value="upper right")
OptionMenu(root, legend_position, "upper right", "upper left", "lower right", "lower left").grid(row=11, column=1)

# Поле для имени файла сохранения
Label(root, text="Имя файла для сохранения:").grid(row=12, column=0)
entry_file_name = Entry(root)
entry_file_name.grid(row=12, column=1)

# Кнопка для построения графиков
Button(root, text="Построить графики", command=plot_functions).grid(row=13, column=0, columnspan=2)

root.mainloop()
