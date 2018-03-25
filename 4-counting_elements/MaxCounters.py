def solution(N, A):
    Counter = [0]*N
    fix_value = 0
    max_value = 0
    for elem in A:
        if elem > N:
            fix_value = max_value
        else :
            if Counter[elem-1]< fix_value:
                Counter[elem-1] = fix_value
            Counter[elem-1]+=1
            if Counter[elem-1] > max_value:
                max_value = Counter[elem-1]
    for i in range(0,N):
      if Counter[i-1]< fix_value:
          Counter[i-1] = fix_value
    return Counter
    pass
