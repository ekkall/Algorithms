if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())

    dy = [1000] * (m + 1)
    dy[0] = 0

    for i in range(n):
        for j in range(coin[i], m + 1):
            dy[j] = min(dy[j], dy[j - coin[i]] + 1)
    print(dy[m])

'''
# 동전교환 

냅색알고리즘 문제와 다르게 입력이
3
1 2 5
15
와 같이 배열크기(15)보다 동전금액(1 3 5)이 먼저 입력되므로
동전금액을 배열에 넣어서 처리해야함

'''