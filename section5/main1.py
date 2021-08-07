import sys

num, m = map(int, input().split())

num = list(map(int, str(num)))
stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]  # 남은 m만큼 뒤에서부터 자른다.
res = ''.join(map(str, stack))
print(res)

'''
#가장 큰 수 문제 - 스택 활용

스택에 큰 자릿수부터 하나씩 넣으면서,
스택에 있는 수들 중에서 그것보다 더 작은 수가 있으면 pop() 한다.

'''
