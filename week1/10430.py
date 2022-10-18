a, b, c = map(int, input().split())

if 2<=a<=100000 and 2<=b<=100000 and 2<=c<=100000:
    print((a+b)%c)
    print(((a%c)+(b%c))%c)
    print((a*b)%c)
    print(((a%c)*(b%c))%c)
