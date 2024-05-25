
#! based on "No of Distinct ways DP approach"


def no_of_ways_target(n,m,target):

    #! base Case
    
    if target < 0:
        return 0
    
    if n == 0 and target != 0:
        return 0
    
    if target == 0 and n != 0:
        return 0
    
    if target == 0 and n == 0:
        return 1
    
    ans = 0
    for faces in range(1,m+1):
        ans = ans + no_of_ways_target(n-1,m,target-faces)


    return ans

def no_of_ways_target_MEMO(n,m,target,dp):

    #! base Case
    
    if target < 0:
        return 0
    
    if n == 0 and target != 0:
        return 0
    
    if target == 0 and n != 0:
        return 0
    
    if target == 0 and n == 0:
        return 1
    
    
    if dp[n][target] != -1:
        return dp[n][target]
    
    ans = 0
    for faces in range(1,m+1):
        ans = ans + no_of_ways_target_MEMO(n-1,m,target-faces,dp)
        dp[n][target] = ans


    return ans

def no_of_ways_target_TAB(dices,f,target):

    dp = [[0 for _ in range(target+1)] for _ in range(dices+1)]

    #! base case analysis
    dp[0][0] = 1
    for d in range(1,dices+1):
        for t in range(1,target+1):
            ans = 0
            for faces in range(1,f+1):
                if t-faces >= 0:
                    ans = ans + dp[d-1][t-faces]

            dp[d][t] = ans
            
    return dp[dices][target]

def no_of_ways_target_TAB_SOPT(dices,f,target):

    prev = [0] * (target + 1)
    #! base case analysis
    prev[0] = 1
    for _ in range(1,dices+1,1):
        curr = [0] * (target + 1)
        for t in range(1,target+1,1):
            ans = 0
            for i in range(1,f+1,1):
                if t-i >= 0:
                    ans = ans + prev[t-i]
            curr[t] = ans

        prev = curr
    
    return prev[target]





n = 3 #! no. of dices
m = 6 #! no. of faces on each dice
X = 12 #! target to acheive

#! MEMOIZED SOL

# dp = [[-1 for _ in range(X+1)] for _ in range(n+1)]

print(no_of_ways_target_TAB_SOPT(n,m,X))
