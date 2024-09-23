n = int(input())

A = [] * n

# Заполняем массив
for i in range(n):
    B = []
    for j in range(n):
        B.append(int(input()))
    A.append(B)

flag = 1
# Ищем сумму первой строки для последующей проверки
for i in range(0,n,1):
    sum += A[0][i]

sum = 0
for i in range(0,n,1):
    temp1 = temp2 = 0
    for j in range(0,n,1):
        # Ищем сумму строки и столбца
        temp1 += A[i][j]
        temp2 += A[j][i]
    # Проверяем на равенство 
    if temp1 != sum or temp2 != sum:
        flag = 0
        break

print("YES") if flag else print("NO")