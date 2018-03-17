def solution(A):
    c=1
    div=[]
    L=len(A)
    if L<3: return 0

    while c*c<L:
        if L%c==0:
            if c>1: div.append(c)
            div.append(int(L/c))
        c+=1
    if c*c==L: div.append(c)
    div.sort()

    next_peak = [-1]*L
    dist = [-1]*L
    count_peaks = 0
    first_peak = 0
    for elem in range(L-2,0,-1):
        if A[elem]>A[elem+1] and A[elem]>A[elem-1]:
            next_peak[elem] = elem
            first_peak = elem
            count_peaks+=1
        else:
            next_peak[elem] = next_peak[elem+1]
    for elem in range(L-2,0,-1):
        dist[elem] = next_peak[elem]-elem

    count=0
    dist[0]=dist[1]+1
    if dist[0]<0: return 0

    for divisor in div:
        for elem in range(int(L/divisor)):
            if dist[divisor*elem] >= divisor or dist[divisor*elem]<0:
                break
            else:
                count=elem
        if count == int(L/divisor)-1:
            return int(L/divisor)
