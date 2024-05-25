"""
Given:
n = no of post to paint
k = no of colors
:: ninja wants to paint the post so that not more than two adjacent post has the same color.

we have to find how many ways to do the above task
"""
MODULO = (10 ** 9) + 7


def add(a, b):
    return ((a % MODULO) + (b % MODULO)) % MODULO


def mul(a,b):
    return ((a % MODULO) * (b % MODULO)) % MODULO


def solve(n, k):
    # basecase
    if n == 1:
        return k
    
    if n == 2:
        return add(k,mul(k,k-1))

    ans = add(mul(solve(n-2,k),k-1),mul(solve(n-1,k),k-1))

    return ans

def solveMemoization(n, k,dp):
    # basecase
    if n == 1:
        return k
    
    if n == 2:
        return add(k,mul(k,k-1))

    if dp[n] != -1:
        return dp[n]
    
    dp[n] = add(mul(solveMemoization(n-2,k,dp),k-1),mul(solveMemoization(n-1,k,dp),k-1))

    return dp[n]

def solveTab(n,k):
    # dp = [0] * (n+1)
    # dp[1] = k
    # dp[2] = add(k,mul(k,k-1))

    # for i in range(3,n+1):
    #     same_color = mul(dp[i-2],k-1)
    #     diff_color = mul(dp[i-1],k-1)

    #     ans = add(same_color,diff_color)

    #     dp[i] = ans

    
    # return dp[n]

    # Space Optimized

    prev2 = k
    prev1 = add(k,mul(k,k-1))

    for i in range(3,n+1):
        ans = add(mul(prev2,k-1),mul(prev1,k-1))
        prev2 = prev1
        prev1 = ans

    return ans


n = 4
dp = [-1] * (n+1)
print(solveTab(n,3))