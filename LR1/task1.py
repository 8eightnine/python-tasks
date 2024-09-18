from math import sqrt

x0 = int(input())
y0 = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
x4 = int(input())
y4 = int(input())

min_val = sqrt(pow(x1 - x0, 2) + pow(y1 - y0, 2))

if sqrt(pow(x2 - x0, 2) + pow(y2 - y0, 2)) < min_val:
    min_val = sqrt(pow(x2 - x0, 2) + pow(y2 - y0, 2))

if sqrt(pow(x3 - x0, 2) + pow(y3 - y0, 2)) < min_val:
    min_val = sqrt(pow(x3 - x0, 2) + pow(y3 - y0, 2))

if sqrt(pow(x4 - x0, 2) + pow(y4 - y0, 2)) < min_val:
    min_val = sqrt(pow(x4 - x0, 2) + pow(y4 - y0, 2))

if sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)) < min_val:
    min_val = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

if sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2)) < min_val:
    min_val = sqrt(pow(x3 - x1, 2) + pow(y3 - y1, 2))

if sqrt(pow(x4 - x1, 2) + pow(y4 - y1, 2)) < min_val:
    min_val = sqrt(pow(x4 - x1, 2) + pow(y4 - y1, 2))

if sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2)) < min_val:
    min_val = sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))

if sqrt(pow(x4 - x2, 2) + pow(y4 - y2, 2)) < min_val:
    min_val = sqrt(pow(x4 - x2, 2) + pow(y4 - y2, 2))

if sqrt(pow(x4 - x3, 2) + pow(y4 - y3, 2)) < min_val:
    min_val = sqrt(pow(x4 - x3, 2) + pow(y4 - y3, 2))

print(min_val)
