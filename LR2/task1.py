"""Вывести словарь с именами и номерами телефонов"""
dct ={}


while True:
    value = input()
    key_value = value.split(':')
    if len(value) > 0:
        if key_value[0] in dct:
            dct[key_value[0]].append(key_value[1])
        else:
            dct[key_value[0]] = []
            dct[key_value[0]].append(key_value[1])
    else: 
        break

for item in dct:
    print("Name:", item, ", Phone numbers:", dct[item])