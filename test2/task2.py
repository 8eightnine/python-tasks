set1 = set()
set2 = set()

while True:
    value = input()
    if len(value) > 0:
        key_values = value.split( )
        set.add(set1, key_values[0])
        set.add(set2, key_values[1])
    else:
        break

print("YES") if len(set1.difference(set2)) == 0 else print("NO")