def solution(A):
    l = len(A)
    if l<2: return 0
    max_so_far = A[l-1]
    max_profit = 0
    for elem in reversed(range(0,l-1)):
        max_so_far = max(max_so_far, A[elem])
        max_profit = max(max_profit, max_so_far - A[elem])
    return max_profit
