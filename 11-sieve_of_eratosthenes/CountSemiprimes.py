def semi_primes(N):
    result = set()
    sieve = [1]*(N+1)
    c = 2
    sieve[0], sieve[1] = 0,0
    while c*c<(N+1):
        if sieve[c] == 1:
            for i in range(c*c,(N+1),c):
                sieve[i] = 0
        c+=1
    c=2
    while c*c<(N+1):
        if sieve[c]==1:
            for i in range(c*c,(N+1),c):
                if i%c==0 and sieve[int(i/c)] == 1:
                    result.add(i)
        c+=1
    return result


def solution(N, P, Q):
    # write your code in Python 3.6
    L=len(P)
    d = [0]*(N+1)
    semi_prime = semi_primes(N)
    for i in range(1,N+1):
        d[i]=d[i-1]+1 if i in semi_prime else d[i-1]

    result = []
    for i in range(L):
        result.append(d[Q[i]]-d[P[i]-1])
    return(result)
