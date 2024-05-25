def solve(prices,index,buy):
    if index >= len(prices):
        return 0
    
    #! buy wala case
    ans = 0
    if buy:
        profit_buy = -1 * (prices[index]) + solve(prices,index + 1,0)

        # skip
        profit_skip_buy = 0 + solve(prices,index + 1,1)

        ans = max(profit_buy,profit_skip_buy)
    
    #! sell wala case
    else:
        profit_sell = prices[index] + solve(prices,index + 1,1)

        #skip
        profit_skip_sell = 0 + solve(prices,index+1,0)

        ans = max(profit_sell,profit_skip_sell)


    return ans


def solve_memo(prices,index,buy,dp):
    if index >= len(prices):
        return 0
    

    if dp[index][buy] != -1:
        return dp[index][buy]
    #! buy wala case
    ans = 0
    if buy:
        profit_buy = -1 * (prices[index]) + solve_memo(prices,index + 1,0,dp)

        # skip
        profit_skip_buy = 0 + solve_memo(prices,index + 1,buy,dp)

        ans = max(profit_buy,profit_skip_buy)
    
    #! sell wala case
    else:
        profit_sell = prices[index] + solve_memo(prices,index + 1,1,dp)

        #skip
        profit_skip_sell = 0 + solve_memo(prices,index+1,0,dp)

        ans = max(profit_sell,profit_skip_sell)

    dp[index][buy] = ans
    return ans

def solve_tab(prices):
    dp = [[0 for _ in range(2)]for __ in range(len(prices)+1)]
    
    # loop that denotes recursive call
    ans = 0
    for index in range(len(prices)-1,-1,-1):
        for buy in range(2):
            if(buy):
                profit_buy = -1 * prices[index] + dp[index + 1][0]
                # skip
                profit_skip_buy = 0 + dp[index + 1][buy]
                ans = max(profit_buy,profit_skip_buy)

            else:
                profit_sell = prices[index] + dp[index + 1][1]

                #skip
                profit_skip_sell = 0 + dp[index+1][0]

                ans = max(profit_sell,profit_skip_sell)
            
            dp[index][buy] = ans


    
    return dp[0][1]

def solve_tab_SOPT(prices):

    next = [0] * 2
    # loop that denotes recursive call
    ans = 0
    for index in range(len(prices)-1,-1,-1):
        curr = [0] * 2
        for buy in range(2):
            if(buy):
                profit_buy = -1 * prices[index] + next[0]
                # skip
                profit_skip_buy = 0 + next[buy]
                ans = max(profit_buy,profit_skip_buy)

            else:
                profit_sell = prices[index] + next[1]

                #skip
                profit_skip_sell = 0 + next[0]

                ans = max(profit_sell,profit_skip_sell)
            
            curr[buy] = ans

        next = curr


    
    return next[1]
    
arr = [7,1,5,3,6,4]
# dp = [[-1 for _ in range(2)]for __ in range(len(arr)+1)]

print(solve_tab_SOPT(arr))


