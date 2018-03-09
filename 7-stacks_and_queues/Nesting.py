def solution(S):
    stack = 0
    for elem in S:
        if elem == ')':
            if stack == 0:
                return 0
            else:
                stack-=1
        if elem == '(':
            stack+=1

    if stack == 0:
        return 1
    else:
        return 0
