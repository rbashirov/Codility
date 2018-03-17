def solution(A):
    first_peak = 0
    l=len(A)
    next_peak = [-1]*l
    count_peaks = 0

    for elem in range(l-2,0,-1):
        if A[elem]>A[elem+1] and A[elem]>A[elem-1]:
            next_peak[elem] = elem
            first_peak = elem
            count_peaks+=1
        else:
            next_peak[elem] = next_peak[elem+1]

    max_flag = 1
    if count_peaks < 2: return count_peaks
    max_peaks = int(l**.5)+1
    for distance in range(max_peaks,1,-1):
        used_flags=1
        remain_flags = distance - 1
        pos = first_peak
        while remain_flags > 0:
            tmp = pos + distance
            if tmp >= l-1: break
            if next_peak[tmp] == -1: break
            pos = next_peak[tmp]
            used_flags += 1
            remain_flags -= 1
        max_flag = max(max_flag, used_flags)

    return max_flag
