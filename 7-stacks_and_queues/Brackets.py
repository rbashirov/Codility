def solution(S):
    brackets ={']':'[','}':'{',')':'('}
    stack = []
    for elem in S:
        if elem not in brackets:
            stack.append(elem)
        else:
            if len(stack)==0:
                return 0
            elif brackets[elem] != stack.pop():
                return 0
    if len(stack)==0:
        return 1
    else:
        return 0
    pass
