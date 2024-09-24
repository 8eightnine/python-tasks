def NOD(a, b):
    """Вычисляется НОД для натуральных чисел a и b
        по быстрому алгоритму Евклида.
        Возвращает вычисленный НОД.
    """
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def find_result(A, B, C, D, divisor):
    A = A * (divisor / B)
    B = B * (divisor / B)
    C = C * (divisor / D)
    D = B
    E = A - C

    divisor = NOD(E, B)
    E = E / divisor
    B = B / divisor
    print("Answer:", E, "/", B)


val1 = input()
val2 = input()

val1_split = val1.split("/")
val2_split = val2.split("/")

divisor = NOD(int(val1_split[1]), int(val2_split[1]))
find_result(int(val1_split[0]), int(val1_split[1]), int(val2_split[0]),
            int(val2_split[1]), divisor)
