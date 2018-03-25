def solution(A):
    Check=[0]*len(A)
    for elem in A:
        if elem > len(A) or elem < 1:
            return 0
        elif Check[elem-1]!=0:
            return 0
        else:
            Check[elem-1]=1
    return 1
    pass
