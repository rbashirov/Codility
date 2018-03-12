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

    leader_total = len([i for i in A if i == candidate])
    leader_count = 0
    equileader_count = 0
    for elem in range(len(A)):
        if A[elem] == candidate:
            leader_count+=1
        if leader_count > (elem+1)/2 and (leader_total - leader_count) > (len(A) - elem - 1)/2:
            equileader_count+=1

    return equileader_count
