h, m = map(int, input().split())
c = int(input())

a, b = (h+((m+c)//60), (m+c))
if b>59:
    print((h+((m+c)//60))%24, b%60)
elif b<59:
    print(a, b)
else:
    print(a, b%60)
