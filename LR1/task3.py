"""Программа для замены символа точки на процент в строке"""

string = input()
old = string.count(".")

string = string.replace(".", "")

new = string.count(".")

print(old - new)
print(string)
