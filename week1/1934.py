import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

line = int(input())

for i in range(line):
    x, y = map(int, input().split())
    print(lcm(x, y))
