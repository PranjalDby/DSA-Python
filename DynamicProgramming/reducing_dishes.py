
def maximum_sum_liketime_coefficient(satisfaction,index,time):
    # base case
    if index >= len(satisfaction):
        return 0
    
    
    include = satisfaction[index] * (time + 1) + maximum_sum_liketime_coefficient(satisfaction,index + 1,time + 1)
    exclude = 0 + maximum_sum_liketime_coefficient(satisfaction,index+1,time)
    
    return max(include,exclude)


def maximum_sum_liketime_coefficient_memo(satisfaction,index,time,dp):
    
    if index == len(satisfaction):
        return 0
    
    if dp[index][time] != -1:
        return dp[index][time]
    
    include = satisfaction[index] * (time +1) + maximum_sum_liketime_coefficient_memo(satisfaction,index+1,time+1,dp)
    exclude = 0 + maximum_sum_liketime_coefficient_memo(satisfaction,index+1,time,dp)

    dp[index][time] = max(include,exclude)

    return dp[index][time]


def maximum_sum_tab(satisfaction):

    dp = [[0 for i in range(len(satisfaction)+1)] for j in range(len(satisfaction)+1)]

    for index in range(len(satisfaction)-1,-1,-1):
        
        for time in range(index,-1,-1):
            include = satisfaction[index] * (time + 1) + dp[index+1][time+1]
            exclude = 0 + dp[index+1][time]
            ans = max(include,exclude)
            dp[index][time] = ans


    return dp[0][0]

def maximum_sum_tab_spOpt(satisfaction):

    n = len(satisfaction)
    next_row = [0] * (n + 1)


    for index in range(n-1,-1,-1):
        curr_row = [0] * (n + 1)
        for time in range(index,-1,-1):
            include = satisfaction[index] * (time + 1) + next_row[time+1]
            exclude = 0 + next_row[time]
            curr_row[time] = max(include,exclude)
        # point next_row to curr_row and so on
        next_row = curr_row

    print(next_row)
    return next_row[0]


satisfaction = [-1,-8,0,5,-9]

satisfaction = sorted(satisfaction)
# dp = [[-1 for i in range(len(satisfaction)+1)] for j in range(len(satisfaction)+1)]
print(maximum_sum_tab_spOpt(satisfaction))
