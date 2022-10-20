import sys

t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    #.rstrip() -> 공백 및 개행문자 제거 이거는 없어도 정답처리됨
    sum = a+b
    print(sum)
