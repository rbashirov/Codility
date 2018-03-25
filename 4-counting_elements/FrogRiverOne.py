def solution(X, A):
    L=len(A)
    Check=[0]*X
    counter = 0
    time = 0

    for elem in A:
        time+=1
        if Check[elem-1]==0:
            Check[elem-1]=1
            counter+=1
        if counter == X:
            return  time-1
        # write your code in Python 3.6
    return -1
    pass
