def solution(A, B):
    survivals = 0
    stack = [] # sizes of fish that flowing downstream
    for fish in range(len(A)):
        if B[fish]==0:
            while len(stack)!=0:
                if stack[-1] > A[fish]:
                    break
                else:
                    stack.pop()
            else:
                survivals+=1
        else:
            stack.append(A[fish])

    survivals+=len(stack)
    return survivals
