import sys
from collections import deque

n, k = map(int, input().split())

q = list(range(1, n + 1))
dq = deque(q)
while dq:
    for _ in range(k - 1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()


'''
deque로 큐 활용

popleft() 제일 위 원소 제거
append() 제일 뒤에 원소 추가
'''
