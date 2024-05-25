"""
Given:
You have been given a number of stairs. initially, you are at the 0th stair, and you need to reach to the `n th` stair. Each time you can either climb `One Step` or `Two Steps`.

We have to return the number of distinct way. in which you can climb from 0th step to N th step.
"""
from array import array

MOD = (10 ** 9) + 7
def possibleWayToClimb(n,i):

    if i == n:
        return 1
    
    if i >= n:
        return 0

    return (possibleWayToClimb(n,i+1) + possibleWayToClimb(n,i+2)) % MOD
    

# Using Top-down approach or recursion + memoization

def minimumCostMemoized(cost,step,dp):
    
    if step == 0:
        return cost[0]
    
    if step == 1:
        return cost[1]
    

    if dp[step] != -1:
        return dp[step]
    
    ans = min(minimumCostMemoized(cost,step-1,dp),minimumCostMemoized(cost,step-2,dp)) + cost[step]

    dp[step] = ans
    return ans


# Using tabulation or (bottom-up approach)

def minimumCostTabulation(cost,n):

    # dp = [-1] * (n+1)

    # # base case analyze
    # dp[0] = cost[0]
    # dp[1] = cost[1]

    # for i in range(2,len(cost)):
    #     dp[i] = cost[i] + min(dp[i-1],dp[i-2])
    
    # return min(dp[n-1],dp[n-2])

    # Space optimized

    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2,n):
        curr = cost[i] + min(prev1,prev2)
        prev2 = prev1
        prev1 = curr

    return min(prev1,prev2)


# Minimum No of coins required to make the target amount
"""
given:

we have a infinite supply of coins, we have `n` no of coins and we have target amount 'X'

base cases:

1.if we can't make to the target by using the given coins, if that the case return -1.
2. if our target is to reach 0,then we need 0 coins to get zero.

"""

INT_MAX = 1000000
def findMinimumCoins(nums,x):
    
    if x == 0:
        return 0
    
    if x < 0:
        return INT_MAX

    # traversing through each coins
    mini = INT_MAX
    for coins in range(len(nums)):
        ans = findMinimumCoins(nums,x-nums[coins])

        if ans != INT_MAX:
            mini = min(mini,ans + 1)

    
    return mini


def findMinimumCoinsMemoized(nums,x,dp):
    if x==0:
        return 0
    
    if x < 0:
        return INT_MAX
    
    if dp[x] != INT_MAX:
        return dp[x]
    

    mini = INT_MAX

    for i in range(len(nums)):
        ans = findMinimumCoinsMemoized(nums,x-nums[i],dp)
        if ans != INT_MAX:
            mini = min(mini,ans+1)

    dp[x] = mini

    return dp[x]


def solveTabulation(nums,x):

    dp = [INT_MAX] * (x+1)

    # convert our base case into a solution
    dp[0] = 0

    for i in range(1, target+1):

        for j in range(len(nums)):
            # converted recursive relation
            if i-nums[j] >= 0 and dp[i-nums[j]] != INT_MAX:
                
                dp[i] = min(dp[i],1 + dp[i-nums[j]])

    
    print(dp)
    if dp[x] != INT_MAX:
        return dp[x]
    
    return -1


# cost = [1,100,1,1,1,100,1,1,100,1]
# # cost = [10,15,20]
# dp = [-1] * (len(cost) + 1)

# # ans = min(minimumCostTabulation(cost,len(cost)-1),minimumCostTabulation(cost,len(cost)-2))
# ans = minimumCostTabulation(cost,len(cost))
# print(ans)


nums = [1,2,3]
target = 7
dp = [INT_MAX] * (target + 1)
# print(findMinimumCoinsMemoized(nums,7,dp)) if findMinimumCoinsMemoized(nums,7,dp) != INT_MAX else print('Not find ans',-1)


# Maximum sum of non-adjacent element

def maximum_sum_nonadjelement(nums,n):

    # base case L-R

    if n >= len(nums):
        return 0
    
    include = nums[n] + maximum_sum_nonadjelement(nums,n+2) # we are including the element
    exclude = maximum_sum_nonadjelement(nums,n+1) + 0

    ans = max(include,exclude)

    return ans


def maximum_sum_nonadjMemoized(nums,n,dp):
    if n >= len(nums):
        return 0
    

    if dp[n] != -1:
        return dp[n]
    
    include = nums[n] + maximum_sum_nonadjMemoized(nums,n+2,dp)
    exclude = 0 + maximum_sum_nonadjMemoized(nums,n+1,dp)

    ans = max(include,exclude)
    dp[n] = ans
    return dp[n]


def maximum_sum_nonadjTab(nums):

    # dp = [0] * (len(nums) + 1)

    # dp[0] = nums[0]

    # for i in range(1,len(nums)):
    #     include = nums[i] + dp[i-2]
    #     exclude = 0 + dp[i-1]
    #     ans = max(include,exclude)
    #     dp[i] = ans

    
    # return dp[len(nums)-1]

    # space Optimized

    prev2 = 0
    prev1 = nums[0]

    for i in range(1,len(nums)):
        include = prev2 + nums[i]
        excl = prev1 + 0
        ans =max(include,excl)
        prev2 = prev1
        prev1 = ans

    return ans

nums = [9,9,8,2]
# print(maximum_sum_nonadjelement(nums,0))

# create the dp array

# dp = [-1] * (len(nums) + 1)
# print('SOLUTION USING TAB = ',maximum_sum_nonadjTab(nums))


def maximumAmountRobbed(amounts,i):
    
    # base case 

    if i < 0:
        return 0
    
    if i == 0:
        return amounts[0]
    
    incl = amounts[i] + maximumAmountRobbed(amounts,i-2)
    excl = maximumAmountRobbed(amounts,i-1) + 0

    return max(incl,excl)



def max_robbed_amount_tab(nums):
    dp = [0] * (len(nums) +1)

    dp[0] = nums[0]

    for i in range(1,len(nums)):
        incl = nums[i] + dp[i-2]
        exc = dp[i-1] + 0
        ans = max(incl,exc)
        dp[i] = ans

    return dp[len(nums)-1]

#  --------------------------------------------------------------------------------------------

# Cut the rod into segments of x,y and z

NEG_INF = float('-inf')
def max_no_segments(n,x,y,z):
    if n < 0:
        return NEG_INF
    
    if n == 0:
        return 0
    
    x_segment = max_no_segments_memoized(n-x,x,y,z,dp) + 1
    y_segment = max_no_segments_memoized(n-y,x,y,z,dp) + 1
    z_segment = max_no_segments_memoized(n-z,x,y,z,dp) + 1


    ans = max(x_segment,y_segment,z_segment)

    return ans

def max_no_segments_memoized(n,x,y,z,dp):

    if n == 0:
        return 0
    
    if n < 0:
        return NEG_INF
    
    if dp[n] != NEG_INF:
        return dp[n]
    
    x_segment = max_no_segments(n-x,x,y,z) + 1
    y_segment = max_no_segments(n-y,x,y,z) + 1
    z_segment = max_no_segments(n-z,x,y,z) + 1

    dp[n] = max(x_segment,y_segment,z_segment)

    return dp[n]
    
def max_no_segments_tab(n,x,y,z):
    dp = [NEG_INF] * (n+1)

    dp[0] = 0

    for i in range(1,n+1):
        # important case
        if i-x >=0 and dp[i-x] != NEG_INF:
            dp[i] = max(dp[i],dp[i-x] + 1)
        
        if i-y >=0 and dp[i-y] != NEG_INF:
            dp[i] = max(dp[i],dp[i-y] + 1)

        if i-z >=0 and dp[i-z] != NEG_INF:
            dp[i] = max(dp[i],dp[i-z] + 1)


    
    if dp[n] != NEG_INF:
        return dp[n]
    
    return 0

# target = 7

# dp = [NEG_INF] * (target + 1)
# print("Max Segments = ",max_no_segments_tab(target,5,2,2))


# count derangements ------------------------------------------------------------------------------

D_MOD  = (10 ** 9) + 7

def add(a,b):
    return ((a % D_MOD) + (b % D_MOD)) % D_MOD


def mul(a,b):
    return ((a % D_MOD) * (b % D_MOD)) % D_MOD


def count_no_derangements(n):

    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    ans = mul((n-1),add(count_no_derangements(n-1),count_no_derangements(n-2)))

    return ans

def count_derangements_memo(n,dp):
    
    if n == 1:
        return 0
    
    if n == 2:
        return 1
    
    if dp[n] != -1:
        
        return dp[n]
    

    dp[n] = ( ((n-1) % D_MOD) *  ((count_derangements_memo(n-1,dp) % D_MOD ) + ( count_derangements_memo(n-2,dp) % D_MOD)) %D_MOD)

    return dp[n]


def count_derangment_tab(n):
    # dp = [-1] * (n+1)

    # dp[1] = 0
    # dp[2] = 1

    # for i in  range(3,n+1):
    #     a = dp[i-1] % D_MOD
    #     b = dp[i-2] % D_MOD
    #     ans = (a+b) % MOD
    #     dp[i] = (ans * (i-1)) % D_MOD

    
    # if dp[n] != -1:
    #     return dp[n]
    
    # -----Space optimization

    prev2 = 0
    prev1 = 1

    for i in range(3,n+1):
        a = prev1 % D_MOD
        b = prev2 % D_MOD

        sums = (a + b) % D_MOD

        ans = ((i-1) * sums) % D_MOD
        prev2 = prev1
        prev1 = ans
    
    return prev1


# n = 3000

# dp = [-1] * (n+1)
import sys
# changing the recursion limit to 4000
sys.setrecursionlimit(4000)
# print("total_no_of derangment possible = ",count_derangment_tab(n))
# print("total_no_of derangment possible using memoization = ",count_derangements_memo(n,dp))


#  ------------------- Painting Fence Algorithm -------------------------------------------------

def count_ways_paint(n,k):

    if n == 1:
        return k
    
    if n==2:
        return add(k,mul(k,k-1))
    
    ans = add(mul(count_ways_paint(n-1,k),k-1),mul(count_ways_paint(n-2,k),k-1))

    return ans
    

def count_ways_paint_memoized(n,k,dp):
    if n == 1:
        return k
    
    if n == 2:
        return add(k,mul(k,k-1))
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = add(mul(count_ways_paint_memoized(n-1,k,dp),k-1),mul(count_ways_paint_memoized(n-2,k,dp),k-1))

    return dp[n]  

def count_ways_paint_tab(n,k):
    # dp = [-1] * (n+1)

    # dp[1] = k
    # dp[2] = add(k,mul(k,k-1))

    # for i in range(3,n+1):
    #     dp[i] = add(mul(dp[i-1],(k-1)),mul(dp[i-2],(k-1)))
    
    # return dp[n]

    prev1 = add(k,mul(k,k-1))
    prev2 = k

    for i in range(3,n+1):
        ans = add(mul(prev1,k-1),mul(prev2,k-1))
        prev2 = prev1
        prev1 = ans
    
    return ans

n = 100
k = 3

dp = [-1] * (n+1)
print(count_ways_paint_memoized(n,k,dp))
print("Using Tab ",count_ways_paint_tab(n,k))