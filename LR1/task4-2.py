"""Программа для разделения списка значений по параметрам: больше нуля, меньше или равно нулю"""

n = int(input())
if n <= 0:
    print("Ошибка: n не может быть <= 0")
else:
    nums = []
    positive = []
    other = []

    for i in range(n):
        nums.append(int(input()))
    print(nums)

    for i in range(n):
        if nums[i] > 0:
            positive.append(nums[i])
    print(positive)

    for i in range(n):
        if nums[i] <= 0:
            other.append(nums[i])

    print(other)
