def solution(A):
    max_endings = [A[0]]*len(A)
    max_endings[1] = A[0]+A[1]
    for i in range(2,len(A)):
        max_endings[i] = max(max_endings[(i-min(i,6)):i])+A[i]
    return(max_endings[-1])
