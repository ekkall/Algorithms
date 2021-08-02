import sys

# sys.stdin=open("input.txt", "r")
n = int(input())
a = list(map(int, input().split()))
avr = sum(a) / n
avr = avr + 0.5  #소수 첫째자리에서 반올림
avr = int(avr)
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - avr)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(avr, res)