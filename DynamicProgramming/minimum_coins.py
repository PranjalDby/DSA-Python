
INT_MAX = 1000000
def minimumCoins(target,coins):
    # time complexity O(2 ^ x)
    # base Case
    if target == 0:
        return 0
    
    if target < 0:
        return INT_MAX

    mini = INT_MAX #infinity

    for i in range(len(coins)):
        ans = minimumCoins(target-coins[i],coins)
        if ans != INT_MAX :
            #update the minimum
            mini = min(mini,1 + ans)

    
    return mini

def minimumCoinsMemoized(target,coins,dp):
    # base Case
    # time complexity = target * len(coins)
    # space complexity = len(callstack) + len(dp datatstructure)
    if target == 0:
        return 0
    
    if target < 0:
        return INT_MAX

    if dp[target] != -1:
        return dp[target]
    
    mini = INT_MAX #infinity

    for i in range(len(coins)):
        ans = minimumCoinsMemoized(target-coins[i],coins,dp)
        if ans != INT_MAX :
            #update the minimum
            mini = min(mini,1 + ans)

    dp[target] = mini

    return mini

def minimumCoinsTabulation(coins,target):
    dp = [INT_MAX] * (target + 1)

    dp[0] = 0
    for i in range(1,target+1):
        # i'm trying to solve for every amount figure
        for j in range(0,len(coins)):
            if i-coins[j] >=0 and dp[i-coins[j]] != INT_MAX:
                dp[i] = min(dp[i],1 + dp[i-coins[j]])

    
    if dp[target] == INT_MAX:
        return -1
    
    return dp[target]


coins = [1,2,3] # with infinite amount

target = 7
dp = [-1] * (target + 1)
# mini = minimumCoinsTabulation(coins,target)
mini = minimumCoinsMemoized(target,coins,dp)
print(mini)
