"""Программа для нахождения минимального значения в списке"""

n = int(input())

nums = []

for i in range(n):
    nums.append(int(input()))

min = nums[0]
index = 0
for i in range(1, n, 1):
    if nums[i] < min:
        min = nums[i]
        index = i

print("min =", min, "at index", index)
