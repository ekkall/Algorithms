import sys

n = int(input())

ch = [0] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = 1
print(cnt)

'''
입력된 자연수까지의 소수 개수를 구하는 문제(에라토스테네스 체)
2부터 1씩 증가하면서, 0이면 cnt를 1증가하고, 자신의 배수는 모두 1로 체크한다. 

입력
20

출력
8

'''