import sys

sys.stdin = open("input.txt", "r")

n = int(input())
body = []

for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse=True)  # 첫번째 원소에 의해 내림차순 정렬
largest = 0
cnt = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)

'''
씨름 선수 문제 (그리디)

키, 몸무게 중 적어도 하나는 나머지 모든 지원자들보다 커야 선발됨

     -> 키순으로 정렬 후
     -> 자신보다 키가 큰 선수들보다 몸무게가 제일 무거워야 함(모두 자신보다 키가 크므로 몸무게라도 무거워야 한다)
     -> 즉, largest 몸무게로 갱신될 때마다 cnt=1

입력
5
172 67
183 65
180 70 
170 72 
181 60

출력
3

'''