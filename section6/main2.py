def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ') #전위순회
        DFS(v * 2)
        DFS(v * 2 + 1)


if __name__ == "__main__":
    DFS(1)


'''
# 이진트리 순회(DFS)

'''