point_to_str = {
    1:'Отрезки',
    3:'Треугольники',
    4:'Четырехугольники',
    5:'Пятиугольники',
    6:'Шестиугольники',
    7:'Семиугольники',
    8:'Восьмиугольники'
}

dct = {}

str = input()
values = str.split(';')

for item in values:
    count = item.count(" ") + 1
    if count in dct:
        dct[count].append(item.split(' '))
    else:
        dct[count] = []
        dct[count].append(item.split(' '))

for item in dct:
    print(point_to_str.get(item), ", Значения:", dct[item])