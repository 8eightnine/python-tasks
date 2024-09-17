from math import sqrt

def distance(x1, y1, x2, y2):
    result = 0
    result = pow(x2 - x1, 2) + pow(y2 - y1, 2)
    result = sqrt(result)
    return result


x = []
y = []

for num in range(5):
    x.append(int(input()))
    y.append(int(input()))

min = distance(x[0], y[0], x[1], y[1])
i = 0
for i in range(4):
    num = distance(x[i], y[i], x[i + 1], y[i + 1])
    if num < min:
        min = num
    i = i + 1

print(min)