def solution(N):
    result = 0
    c = 1
    while c*c < N:
        if N%c == 0: result+=2
        c+=1
    if c*c == N: result+=1
    return result
