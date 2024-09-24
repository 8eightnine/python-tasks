def checkString(value):
    flag = {}

    for ch in value:
        if ch in flag and flag[ch] == 1:
            return False
        else:
            flag[ch] = 1

    return True


input_val = input()
result = checkString(input_val)
print("True") if result else print("False")
