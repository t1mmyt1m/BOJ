t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if 0<a and b<10:
        print('Case #{}: {}' .format(i+1, a+b))
