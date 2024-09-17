n = int(input())

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