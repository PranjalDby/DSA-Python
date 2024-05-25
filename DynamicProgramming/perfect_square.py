"""
Given a number 'N'. find the minimum number of squares of any number that sums to "N".
for example N= 100, N can be expressed as (10 * 10) and also as (5 * 5 + 5 * 5 + 5 * 5 + 5 * 5),
but output is 1 as min no of squares
"""

def get_minin_squares(n):

    # base case : becuase we can't make zero with perfect square
    if n == 0:
        return 0
    
    ans = n
    for i in range(1,n+1):

        if (i * i) <= n:
            # here ans is minimum of utilized squares
            ans = min(ans,1 + get_minin_squares(n - (i*i)))

        
    return ans


def get_mini_sqr_memo(n,dp):
    
    # base case
    if n == 0:
        return 0
    

    if dp[n] != -1:
        return dp[n]
    
    ans = n
    for i in range(1,n+1):

        if (i * i) <= n:
            # here ans is minimum of utilized squares
            ans = min(ans,1 + get_mini_sqr_memo(n - (i*i),dp))

    dp[n] = ans

    return dp[n]


INT_MAX = (10 ** 9) + 7
def get_mini_sqr_tab(n):

    dp = [INT_MAX] * (n + 1)

    # base case

    dp[0] = 0

    for i in range(1,n+1):

        for j in range(1,n+1):

            if j * j  <= i:
                if i - (j *j) >= 0:
                    dp[i] = min(dp[i],dp[i - (j * j)] + 1)

    
    if dp[n] !=INT_MAX:
        return dp[n]
    
def fibonnaci(n,dp):

    if n == 0:
        return 0
    
    if n== 1:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    ans = fibonnaci(n-1,dp) + fibonnaci(n-2,dp)

    dp[n] = ans
    
    return ans

import sys
sys.setrecursionlimit(3000)
n = 1000
dp = [-1] * (n + 1)
print(get_mini_sqr_tab(n))

# print('{0:3e}'.format(fibonnaci(500,dp)))