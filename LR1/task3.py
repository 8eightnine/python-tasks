string = input()
old = string.count(".")

string = string.replace(".", "")

new = string.count(".")

print(old - new)
print(string)