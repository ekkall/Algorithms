import sys

sys.stdin = open("input.txt", "r")


def Count(len):
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
Line = []
res = 0
largest = 0

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)

'''
# 랜선 자르기 문제(결정알고리즘)

n개를 만들 수 있는 랜선의 최대 길이를 구해야 함
    ->이분 검색은 결정 알고리즘에 활용됨. (답이 어떤 범위 안에 있다)

입력
4 11
802
743
457
539

출력
200

'''
