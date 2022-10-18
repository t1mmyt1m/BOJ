a = int(input())
b = int(input())
c = int(input())

num = list(str(a*b*c))
count = [0]*10

for i in range(10):
    for j in num:
        if int(j) == i:
            count[i] += 1
for i in count:
    print(i)
