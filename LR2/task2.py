dct = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0
}

value = input()
flag = 0

for ch in value:
    if ch.isdigit():
        dct[ch] = dct[ch] + 1

for item in dct:
    if dct[item] == 1:
        print(item)
        flag = 1

if not flag:
    print("HET")
