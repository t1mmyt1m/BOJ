h, m = map(int, input().split())
c = int(input())

#if 0<=h<=23 and 0<=m<=59 and 0<=c<=1000:
a, b = (h+((m+c)//60), (m+c))
if b>59: #처음에 h>=23이라고 썼는데 어차피 어떤 수가 오든 모듈로 24를 하면 알맞는 값이 나오기 때문에 빼줌(그랬더니 통과함)
#그리고 어차피 c의 최댓값이 1000이기 때문에 (1000 + 59) % 60 = 39으로 h를 0으로 설정해도 무방함. 그래서 빼줌
    print((h+((m+c)//60))%24, b%60)
elif b<59:
    print(a, b)
else:
    print(a, b%60)

#(1000 + 59) % 60 = 39
