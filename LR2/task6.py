def check_for_pyramid(n):
    i = 0
    sum = 0

    while sum < n:
        sum += pow(i, 2)
        i += 1

    if sum == n:
        return i - 1
    else:
        return -1


n = int(input())

result = check_for_pyramid(n)

print(result) if result != -1 else print("It is impossible")
