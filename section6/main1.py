
def DFS(x):
    if x == 0:
        return
    else:
        DFS(x // 2)
        print(x % 2, end='')


n = int(input())
DFS(n)

'''
# 이진수를 재귀함수로 구하는 문제

'''
