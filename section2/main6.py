import sys

sys.stdin = open("input.txt", "r")


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

n = int(input())
a = list(map(int, input().split()))
res = 0
max = -2147000000 # int형의 최소값(대략)
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

'''
자릿수의 합을 구하는 문제

입력
3
125 15232 97

출력
97

'''