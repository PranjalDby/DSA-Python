
def solveMaximumSumNonADJ(array,i):

    # Base Case: for left- right

    if i >= len(array):
        return 0
    
    # Recurisve Relation

    include = solveMaximumSumNonADJ(array,i+2) + array[i] # to include non adjacent element
    exclude = solveMaximumSumNonADJ(array,i+1) + 0 # to exclude the element.


    # maximum Sum

    return max(include,exclude)


def solveMaximumSumNonADJMemoized(array,i,dp):
    
    if i >= len(array):
        return 0
    

    if dp[i] != -1:
        return dp[i]

    include = solveMaximumSumNonADJMemoized(array,i+2,dp) + array[i] # to include non adjacent element
    exclude = solveMaximumSumNonADJMemoized(array,i+1,dp) + 0 # to exclude the element.

    dp[i] = max(include,exclude)

    return dp[i]

def solveMaximumSumNonADJTabulation(array,n):

    # dp = [0] * (n)
    # dp[0] = array[0]

    # for j in range(1,n):
    #     include = dp[j-2] + array[j]
    #     exclude = dp[j-1] + 0
    #     dp[j] = max(include,exclude)

    
    # print(dp)
    # return dp[n-1]

    prev2 = 0
    prev1 = array[0]

    for i in range(1,n):
        incl = prev2 + array[i]
        excl = prev1 + 0
        ans = max(incl,excl)
        prev2 = prev1
        prev1 = ans
    
    return prev1



array = [9,9,8,2]

dp = [-1] * (len(array) + 1)
print(solveMaximumSumNonADJTabulation(array,len(array)))
