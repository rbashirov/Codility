def solution(A):
    Check = [0]*(len(A)+1)
    min_int = 1
    count = 0
    for elem in A:
        if elem>0 and elem<(len(A)+1):
            if Check[elem-1]==0:
                Check[elem-1] = 1
    for checkelem in Check:
        if checkelem == 0:
            return count+1
        count+=1
pass
