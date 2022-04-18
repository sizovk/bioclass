# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     for j in range(1, i + 1):
#         if j * j == i:
#             print(i, end=' ')

import math

a=int(input())
b=int(input())
sq_a = math.ceil(a ** 0.5)
sq_b = math.floor(b ** 0.5)
for i in range(sq_a, sq_b + 1):
    print(i ** 2, end=' ')