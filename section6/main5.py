def DFS(L, sum, tsum):
    global result
    if sum + (total - tsum) < result:
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L + 1, sum + a[L], tsum + a[L])
        DFS(L + 1, sum, tsum + a[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0] * n
    result = -2147000000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)

'''
#바둑이 승차

dfs 활용

* 현재의 sum 에 total-tsum(현재 합하지 않은 바둑이들의 총 합)을 더한 것과, result를 비교함으로써 cut edge하면 시간복잡도 더 줄일 수 있음.
* ' result = ' 는 함수 내에서 지역변수를 선언하는 것이므로
global result << 꼭 지역변수인지 / 전역변수인지 명시하기!!

'''
