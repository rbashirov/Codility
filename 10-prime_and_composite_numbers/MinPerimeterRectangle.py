def solution(N):
    result = 0
    c = 1
    min_per = 2*(N+1)
    while c*c < N:
        if N%c == 0:
            result+=2
            min_per = min(min_per, 2*(c+int(N/c)))
        c+=1
        if c*c == N:
            result+=1
            min_per = min(min_per, 2*(c+int(N/c)))
    return min_per
