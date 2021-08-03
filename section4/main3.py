import sys

sys.stdin = open("input.txt", "r")


def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())
Music = list(map(int, input().split()))

maxx = max(Music)
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m: # 적어도 maxx보다 용량이 크거나 같아야 함
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)

'''
# 뮤직비디오 문제 (결정알고리즘)

m개로 저장할 수 있는 최소 용량 크기를 출력해야 함
이분검색 사용

입력
9 3
1 2 3 4 5 6 7 8 9

출력
17

'''