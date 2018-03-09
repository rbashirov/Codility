def solution(A):

    ladder = 0
    candidate = 0
    index = 0
    for elem in range(len(A)):
        if ladder == 0:
            candidate = A[elem]
            index = elem
            ladder+=1
        else:
            ladder=ladder+1 if candidate == A[elem] else ladder-1
    if len([i for i in A if i == candidate]) > len(A)/2:
        return index
    else:
        return -1
