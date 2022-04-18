import math

h = int(input())
a = int(input())
b = int(input())
# s = math.ceil((h - a) / (a - b)) + 1
s = (h - a + (a - b - 1)) // (a - b) + 1
# math.ceil(a / b) == (a + b - 1) // b

print(s)