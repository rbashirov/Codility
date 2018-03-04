def solution(H):
    count = 0
    stack = []

    for elem in H:
        while len(stack) != 0 and stack[-1] > elem:
            stack.pop()

        if len(stack) == 0 or stack[-1] < elem:
            count += 1
            stack.append(elem)
    return count
    pass
