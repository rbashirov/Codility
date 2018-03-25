def solution(A, B, K):
    # write your code in Python 3.6
    N=((B-A)-(K-A)%K)//K+1
    return N
    pass
