m = int(input())
n = int(input())
prime = [ ]

for i in range(m, n+1): #m부터 n까지
    if i > 1: #1보다 큰 수
        for j in range(2, i): #2부터 i-1까지
            if (i % j) == 0: #나누어 떨어지면 소수가 아님
                break
        else:
            prime.append(i)

if len(prime) > 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1) #m부터 n까지 소수가 없을 때 -1 출력
