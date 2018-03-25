def solution(S, P, Q):
    LS=len(S)
    LP=len(P)
    DNAcode = [0]*LS
    output = [0]*LP
    counter = [[0 for j in range(LS+1)] for i in range(4)]
    a=[0]*4
    for elem in range(0,LS):
        if S[elem] is 'A':
            DNAcode[elem] = 1
        if S[elem] is 'C':
            DNAcode[elem] = 2
        if S[elem] is 'G':
            DNAcode[elem] = 3
        if S[elem] is 'T':
            DNAcode[elem] = 4
    for i in range(4): #first apperance
            counter[i][0]=0
    for index in range(1,LS+1):
        a[DNAcode[index-1]-1]+=1
        for i in range(4):
            counter[i][index]=a[i]
    for index in range(LP):
        if Q[index]==P[index]:
            output[index]=DNAcode[Q[index]]
        elif counter[0][Q[index]+1] - counter[0][P[index]] > 0:
            output[index]=1
        elif counter[1][Q[index]+1] - counter[1][P[index]] > 0:
            output[index]=2
        elif counter[2][Q[index]+1] - counter[2][P[index]] > 0:
            output[index]=3
        elif counter[3][Q[index]+1] - counter[3][P[index]] > 0:
            output[index]=4
    return output
    pass
