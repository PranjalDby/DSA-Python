from functools import lru_cache
import functools
import time
def modified_clock(func):
    @functools.wraps(func)
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        print(f'[{elapsed:0.8f}s] {name}({args[0]}) -> {result}\n',end="\n")
        return result

    return clocked

# Memoiztion with lru_cache
@lru_cache()
@modified_clock
def fibonnacci(num):
    if num == 0 or num == 1:
        return num
    
    return fibonnacci(num - 1) + fibonnacci(num - 2)
    
# print(fibonnacci(50))

# using list

#top-down = recursion + memoization
# @modified_clock
def fibonnacciWithList(num,memo):    
    if num ==1 or num == 0:
        return num
    

    if memo[num] !=-1:
        return memo[num]
    
    memo[num] = fibonnacciWithList(num-1,memo) +fibonnacciWithList(num-2,memo)
    return memo[num]


# fibonnacciWithList(n)
# fibonnaci - series
# for i in range(n+1):
#     print(fibonnacciWithList(i),end=' ')

# Using bottom-up or tabulation approach for fibonnaci.

def fibonnaciBottomUp(n):
    # create the array with the base cases are already solved.
    dp = [0] * (n+1)
    if n == 1 or n == 0:
        return n;

    # we know the first two values of fibonnaci series
    dp[0] = 0;dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def fibonnaciBottomUp_Optimized(n):
    if n == 1 or n== 0:
        return n
    
    prev1 = 0
    prev2 = 1

    for i in range(2,n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr

    
    return prev2
# time-complexity - O(n) or sc O(n) better than top-down
# space-optimized fibonacci space-complexity is O(1)
# print(fibonnaciBottomUp(50))

# Space Optimized Solution
# we know that curr-num is sum of prev two_number,curr-num = prev1 + prev2;

n = 900
memo = [-1] * (n+1)
print(fibonnacci(330))