def equal_subsets(array,N):
  
    total = 0
    for i in array:
        total += i
    
    if total % 2 == 0:
       
       return solve_TAB_SOPT(array,total//2,N)
    
    else:
       return 0


def solve(array,index,target):

    if index >= len(array):
        return 0
    
    if target < 0 :
        return 0
    
    if target == 0:
        return 1
    

    incl = solve(array,index+1,target-array[index])
    excl = solve(array,index+1,target)


    # only true element get returned
    return incl or excl


def equal_subsets_for_DP(array,N,/):
    total = 0
    for i in array:
        total += i
    
    if total % 2 == 0:
       
       even_total = (total // 2)
       dp = [[-1 for _ in range(even_total+1)] for __ in range(N+1)]

       return solve_MEMO(array,0,even_total,dp,N)
    
    else:
       return 0
    
def solve_MEMO(array,index,target,dp,N):

    if index >= N:
        return 0
    
    if target < 0 :
        return 0
    
    if target == 0:
        return 1
    
    if dp[index][target] != -1:
        return dp[index][target]
    

    incl = solve_MEMO(array,index+1,target-array[index],dp,N)
    excl = solve_MEMO(array,index+1,target,dp,N)


    dp[index][target] = incl or excl
    # only true element get returned
    return dp[index][target]

def solve_TAB(array,target,N):

    dp = [[0 for _ in range(target + 1)] for __ in range(N+1)]

    # traversing in rows of column target = 0 
    for r in range(N+1):
        dp[r][0] = 1


    for index in range(N-1,-1,-1):

        for t in range(0,target+1):
            incl = 0
            if t - array[index] >= 0:
                incl = dp[index+1][t - array[index]]

            excl = dp[index+1][t]

            dp[index][t] = incl or excl # item that are true

    
    return dp[0][target]

def solve_TAB_SOPT(array,target,N):

    curr = [0] * (target + 1)
    next = [0] * (target + 1)
    
   
    next[0] = 1
    for index in range(N-1,-1,-1):
        curr = [0] * (target + 1)
        for t in range(0,target+1):
            incl = 0
            if t - array[index] >= 0:
                incl = next[t - array[index]]

            excl = next[t]

            curr[t] = incl or excl # item that are true

        next = curr

    return next[target]


# arr = [478,757,314,471,729,100,459,618]
arr = [1,5,11,5]
N = len(arr)
print(equal_subsets(arr,N))

