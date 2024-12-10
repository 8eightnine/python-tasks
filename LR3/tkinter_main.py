import tkinter as tk
from tkinter import messagebox
from math import exp, factorial

# Функция для вычисления y(x) с использованием ряда Тейлора
def taylor_series(x, epsilon):
    result = 0
    term = 1  # Первый член ряда
    n = 0
    while abs(term) > epsilon:
        term = ((-1) ** n) * (x ** n) / factorial(n)
        result += term
        n += 1
    return result

# Функция для вычисления z(x)
def z_function(x, b):
    return exp(-x) + b

# Проверка корректности ввода
def validate_input(value, name, allow_negative=False):
    try:
        val = float(value)
        if not allow_negative and val < 0:
            raise ValueError
        return val
    except ValueError:
        messagebox.showerror("Ошибка ввода", f"Некорректное значение для {name}. Введите число.")
        return None

# Функция для построения графиков
def plot_graphs():
    # Получение и проверка параметров
    x_start = validate_input(entry_x_start.get(), "Xнач")
    x_end = validate_input(entry_x_end.get(), "Xкон")
    dx = validate_input(entry_dx.get(), "Шаг dx", allow_negative=False)
    epsilon = validate_input(entry_epsilon.get(), "Точность ε", allow_negative=False)
    b = validate_input(entry_b.get(), "Параметр b")

    if None in (x_start, x_end, dx, epsilon, b):
        return  # Если есть ошибки ввода, прервать выполнение

    if x_start >= x_end:
        messagebox.showerror("Ошибка ввода", "Xнач должен быть меньше Xкон.")
        return

    # Очистка холста
    canvas.delete("all")

    # Размеры холста
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Генерация значений x
    x_values = []
    y_values = []
    z_values = []
    x = x_start
    while x <= x_end:
        x_values.append(x)
        y_values.append(taylor_series(x, epsilon))
        z_values.append(z_function(x, b))
        x += dx

    # Нахождение минимальных и максимальных значений для масштабирования
    all_y_values = y_values + z_values
    y_min = min(all_y_values)
    y_max = max(all_y_values)

    # Функция для преобразования координат в пиксели
    def to_canvas_coords(x, y):
        x_pixel = int((x - x_start) / (x_end - x_start) * canvas_width)
        y_pixel = int(canvas_height - (y - y_min) / (y_max - y_min) * canvas_height)
        return x_pixel, y_pixel

    # Рисование осей
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="black")  # Ось X
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="black")  # Ось Y

    # Рисование графика y(x)
    for i in range(1, len(x_values)):
        x1, y1 = to_canvas_coords(x_values[i - 1], y_values[i - 1])
        x2, y2 = to_canvas_coords(x_values[i], y_values[i])
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=2)

    # Рисование графика z(x)
    for i in range(1, len(x_values)):
        x1, y1 = to_canvas_coords(x_values[i - 1], z_values[i - 1])
        x2, y2 = to_canvas_coords(x_values[i], z_values[i])
        canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

# Создание окна Tkinter
window = tk.Tk()
window.title("Графики функций")

# Поля ввода для параметров
frame = tk.Frame(window)
frame.pack()

tk.Label(frame, text="Xнач:").grid(row=0, column=0)
entry_x_start = tk.Entry(frame)
entry_x_start.grid(row=0, column=1)

tk.Label(frame, text="Xкон:").grid(row=0, column=2)
entry_x_end = tk.Entry(frame)
entry_x_end.grid(row=0, column=3)

tk.Label(frame, text="Шаг dx:").grid(row=1, column=0)
entry_dx = tk.Entry(frame)
entry_dx.grid(row=1, column=1)

tk.Label(frame, text="Точность ε:").grid(row=1, column=2)
entry_epsilon = tk.Entry(frame)
entry_epsilon.grid(row=1, column=3)

tk.Label(frame, text="Параметр b:").grid(row=2, column=0)
entry_b = tk.Entry(frame)
entry_b.grid(row=2, column=1)

# Кнопка для построения графиков
plot_button = tk.Button(frame, text="Построить графики", command=plot_graphs)
plot_button.grid(row=5, column=1, columnspan=2)

# Холст для рисования графиков
canvas = tk.Canvas(window, width=800, height=600, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Запуск приложения
window.mainloop()