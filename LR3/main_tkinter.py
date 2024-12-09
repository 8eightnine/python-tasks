import tkinter as tk
import numpy as np


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


# Функция для отрисовки графиков
def draw_graph(canvas, x_start, x_end, dx, epsilon, b):
    canvas.delete("all")  # Очистить Canvas

    # Определение размеров Canvas
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    # Вычисление значений функций
    x_values = np.arange(x_start, x_end, dx)
    y_taylor = np.array([taylor_exp(x, epsilon) for x in x_values])
    y_shifted = y_taylor + b

    # Определение масштаба
    x_min, x_max = x_start, x_end
    y_min = min(min(y_taylor), min(y_shifted))
    y_max = max(max(y_taylor), max(y_shifted))

    x_scale = width / (x_max - x_min)
    y_scale = height / (y_max - y_min)

    # Функция для преобразования координат
    def transform(x, y):
        x_screen = (x - x_min) * x_scale
        y_screen = height - (y - y_min) * y_scale
        return x_screen, y_screen

    # Отрисовка графиков
    for i in range(len(x_values) - 1):
        x1, y1 = transform(x_values[i], y_taylor[i])
        x2, y2 = transform(x_values[i + 1], y_taylor[i + 1])
        canvas.create_line(x1, y1, x2, y2, fill='blue')

    for i in range(len(x_values) - 1):
        x1, y1 = transform(x_values[i], y_shifted[i])
        x2, y2 = transform(x_values[i + 1], y_shifted[i + 1])
        canvas.create_line(x1, y1, x2, y2, fill='red')


# Создание интерфейса
def main():
    root = tk.Tk()
    root.title("Графики функций")

    # Создание Canvas
    canvas = tk.Canvas(root, width=800, height=600, bg='white')
    canvas.pack(fill=tk.BOTH, expand=True)

    # Создание элементов ввода
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, fill=tk.X)

    label_x_start = tk.Label(frame, text="Xнач:")
    label_x_start.pack(side=tk.LEFT)
    entry_x_start = tk.Entry(frame)
    entry_x_start.pack(side=tk.LEFT)

    label_x_end = tk.Label(frame, text="Xкон:")
    label_x_end.pack(side=tk.LEFT)
    entry_x_end = tk.Entry(frame)
    entry_x_end.pack(side=tk.LEFT)

    label_dx = tk.Label(frame, text="dx:")
    label_dx.pack(side=tk.LEFT)
    entry_dx = tk.Entry(frame)
    entry_dx.pack(side=tk.LEFT)

    label_epsilon = tk.Label(frame, text="ε:")
    label_epsilon.pack(side=tk.LEFT)
    entry_epsilon = tk.Entry(frame)
    entry_epsilon.pack(side=tk.LEFT)

    label_b = tk.Label(frame, text="b:")
    label_b.pack(side=tk.LEFT)
    entry_b = tk.Entry(frame)
    entry_b.pack(side=tk.LEFT)

    # Функция для обновления графиков
    def update_graphs():
        x_start = float(entry_x_start.get())
        x_end = float(entry_x_end.get())
        dx = float(entry_dx.get())
        epsilon = float(entry_epsilon.get())
        b = float(entry_b.get())
        draw_graph(canvas, x_start, x_end, dx, epsilon, b)

    # Кнопка для построения графиков
    button_update = tk.Button(frame,
                              text="Построить графики",
                              command=update_graphs)
    button_update.pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    main()
