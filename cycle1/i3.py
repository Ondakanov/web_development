import math
n = int(input())
c = 0
b = int(math.sqrt(n))
for i in range(1, b):
    if n % i == 0:
        c += 1
c *= 2
if n % b == 0:
    c += 1

print(c)