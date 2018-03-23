def size_check(A,K,size):
    block_num = 0
    current_sum = 0
    for elem in A:
        if current_sum + elem > size:
            block_num+=1
            current_sum = elem
        else:
            current_sum+=elem
        if block_num+1 > K:
            return False
    return True

def solution(K, M, A):
    lower_size = max(A)
    upper_size = sum(A)

    if K == 1: return upper_size
    if K > len(A): return lower_size

    while upper_size > lower_size:
        mid = (upper_size+lower_size)//2
        if size_check(A,K,mid):
            upper_size = mid
        else:
            lower_size = mid+1
    return lower_size
