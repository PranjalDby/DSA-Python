
def solve(start,end):
    
    if start >= end:
        return 0
    
    maxi = 10 ** 9

    for i in range(start,end+1):
        ans = i + max(solve(start,i-1),solve(i+1,end))
        maxi = min(maxi,ans)

    
    return maxi

import functools

@functools.lru_cache(300)
def solve_mem(start,end):
    
    if start >= end:
        return 0
    
    
    maxi = 10 ** 9

    for i in range(start,end+1):
        ans = i + max(solve_mem(start,i-1),solve_mem(i+1,end))
        maxi = min(maxi,ans)

    return maxi


def solve_tab(n):
    dp = [[0 for _ in range(n+2)] for __ in range(n+2)]
    
    for start in range(n,0,-1):
        for end in range(start,n+1):
            if start == end:
                continue
            else:
                maxi = float('inf')
                for i in range(start,end+1):
                    maxi = min(maxi,i + max(dp[start][i-1],dp[i+1][end]))
                    dp[start][end] = maxi
                    
    print(dp)
    return dp[1][n]



n = 10
# dp = [[-1 for _ in range(n+1)] for __ in range(n+1)]
print(solve_tab(10))

    
