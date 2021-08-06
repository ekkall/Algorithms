import sys

n = int(input())
a = list(map(int, input().split()))

a.insert(0, 0) #1번부터 들어가므로 0번은 빈자리로 처리
seq = [0] * n

for i in range(1, n + 1):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i
            break
        elif seq[j] == 0:
            a[i] -= -1

for x in seq:
    print(x, end=' ')

'''
#역수열 문제(그리디)

1, 2, 3, 4, 5 ... n <- 정렬된 순으로 seq 배열에 넣는 것이므로
앞에 자신보다 작은 숫자가 올 수는 없다.
그러므로 1부터 차례로 배열에 넣으면 됨

입력
8
5 3 4 0 2 1 1 0

출력 
4 8 6 2 5 1 3 7
'''
