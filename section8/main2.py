def DFS(len):
    if dy[len] > 0:
        return dy[len]
    if len == 1 or len == 2:
        return len
    else:
        dy[len] = DFS(len - 1) + DFS(len - 2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)
    print(DFS(n))


'''
#네트워크 선 자르기 문제(Top-Down) - (계단오르기 문제와 동일)

- (top down) : 재귀, 메모이제이션 활용

'''



