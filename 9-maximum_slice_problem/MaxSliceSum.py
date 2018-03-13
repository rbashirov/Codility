def solution(A):
    l = len(A)
    max_slice, max_end = A[0], A[0]
    for elem in range(1,l):
        max_end = max(max_end + A[elem], A[elem])
        max_slice = max(max_slice,max_end)
    return max_slice
