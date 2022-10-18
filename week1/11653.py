import math

n = int(input())
i = 2

while i <= math.sqrt(n):
    if n % i != 0:
        i += 1
    else:
        print(i)
        n //= i

if n > 1:
    print(n)
