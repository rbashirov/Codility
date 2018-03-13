def solution(A):
    l = len(A)
    B = [0]*l
    E = [0]*l

    for elem in range(1,l):
        B[elem] = max(B[elem-1]+A[elem],A[elem],0)
    for elem in reversed(range(1,l-1)):
        E[elem] = max(E[elem+1]+A[elem],A[elem],0)

    maxdoubleslice = 0
    for border in range(1,l-1):
        maxdoubleslice = max(maxdoubleslice, B[border-1]+E[border+1])
    return maxdoubleslice 
