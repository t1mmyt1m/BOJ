t1, t2, t3 = list(map(int, input().split()))

if t1==t2==t3:
    print(10000 + t1*1000)
elif t1==t2 or t2==t3:
    print(1000 + t2*100)
elif t3==t1:
    print(1000 + t3*100)
else:
    print(max(t1, t2, t3)*100)
