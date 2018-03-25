def solution(A):
    L=len(A)
    min_slice = (A[0]+A[1])/2
    start_place = 0
    for elem in range(0,L-2):
        if (A[elem+1] + A[elem+2])/2 < min_slice:
            start_place = elem+1
            min_slice = (A[elem+1] + A[elem+2])/2
        if (A[elem] + A[elem+1] + A[elem+2])/3 < min_slice:
            start_place = elem
            min_slice = (A[elem] + A[elem+1] + A[elem+2])/3
    return start_place
    pass
