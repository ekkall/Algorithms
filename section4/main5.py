import sys

#sys.stdin = open("input.txt", "r")
n = int(input())

meeting = []

for i in range(n):
    a, b = map(int, input().split())
    meeting.append((a, b))
meeting.sort(key=lambda x: (x[1], x[0]))
et = 0
cnt = 0
#print(meeting)
for x, y in meeting:
    if x >= et:
        et = y
        cnt += 1
print(cnt)

'''
# 회의실 배정 문제 - 그리디 알고리즘

끝나는 시간 기준으로 정렬하여 해결한다.
시작하는 시간 기준으로 정렬하면 회의의 최대 수를 구할 수 없다.

'''
