"""Программа для нахождения минимального значения в списке"""

n = int(input())
if n <= 0:
    print("Ошибка: n не может быть <= 0")
else:
    nums = []

    for i in range(n):
        nums.append(int(input()))

    min = nums[0]
    index = 0
    for i in range(1, n, 1):
        if nums[i] < min:
            min = nums[i]
            index = i

    print("Минимальный элемент", min, "найден, его индекс -", index)
