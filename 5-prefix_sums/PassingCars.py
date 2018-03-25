def solution(A):
    L=len(A)
    zeronum = 0
    countpairs=0
    for elem in range(0,L):
        if A[elem] == 0:
            zeronum+=1
        elif A[elem] == 1:
            countpairs+=zeronum
        if countpairs > 1000000000:
            return -1
    return countpairs
    pass
