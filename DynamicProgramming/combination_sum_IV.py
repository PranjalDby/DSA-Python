# in this question we have given an array of distinct integers and you have to tell how many different ways of selecting the elements from the array.so that sum of choosen element is equal to the target sum.


def different_ways_to_target(target,arr,stored_ways):
    
    if target == 0:
        return 1
    
    if target < 0:
        return 0
    

    ans = 0
    for i in range(len(arr)):
        # if target-arr[i] >=0 :
        #     stored_ways[i][target-arr[i]] = arr[i]
        ans += different_ways_to_target(target-arr[i],arr,stored_ways)
        # stored_ways[i][i] = arr[i]
        if target-arr[i] >= 0 :
            stored_ways[i][target-arr[i]] = arr[i]
        

    return ans


def different_ways_to_target_memoized(target,arr,dp):
    # base cases
    if target == 0:
        return 1
    
    if target < 0:
        return 0
    
    if dp[target] != -1:
        return dp[target]
    
    ans = 0
    for i in range(len(arr)):
        ans += different_ways_to_target_memoized(target-arr[i],arr,dp)

    dp[target] = ans

    return dp[target]

def different_ways_to_target_tab(target,arr):
    # base cases

    dp = [0] * (target + 1)

    # Analyzed base case
    dp[0] = 1

    for i in range(1,target+1):
        
        for j in range(len(arr)):
            
            if (i-arr[j] >= 0):
                dp[i] += dp[i-arr[j]]

    
    print(dp)
    return dp[target]


    
n = 3
target = 5
arr = [1,2,5]
stored_ways = [[0 for k in range(target)] for i in range(len(arr))]
print(len(stored_ways))

dp = [-1] * (target + 1)
print(different_ways_to_target_tab(target,arr))