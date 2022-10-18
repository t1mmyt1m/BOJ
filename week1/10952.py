while True:
    a, b = map(int, input().split())

    if 0<a and b<10:
        print(a+b)
    elif a==0 and b==0:
        break
