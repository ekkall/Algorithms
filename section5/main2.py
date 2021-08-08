import sys

s = input()

stack = []
cnt = 0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i - 1] == '(':
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)


'''
# 쇠막대기 문제 (스택 활용)

'''
