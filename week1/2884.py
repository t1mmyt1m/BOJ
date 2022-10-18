h, m = map(int, input().split())

if 0<=h<=23 and 0<=m<=59:
    if m>=45:
        print(h, m-45)
    else:
        if h==0:
            print(23, m+15)
        else:
            print(h-1, m+15) # +15 = +60-45
