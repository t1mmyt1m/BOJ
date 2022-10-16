m, n = list(map(int, input().split()))

for i in range(m, n+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1): #소수의 배수를 다 설정할 수 없으니 1/2 제곱에 1씩 더해줘서 범위를 지정해줌
            if i % j == 0:
                break
    else:
        print(i)
