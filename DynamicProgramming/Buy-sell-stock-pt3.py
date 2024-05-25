
def solve(prices,index,buy,limit):
    if index >= len(prices):
        return 0
    
    if limit == 0:
        return 0
    

    profit = 0
    if buy: #! purchased the stock
        buy_it = -prices[index] + solve(prices,index+1,0,limit)
        skip_it = 0 + solve(prices,index +1,1,limit)
        profit = max(buy_it,skip_it)

    else: #! sell'd the stock

        sell_it = prices[index] + solve(prices,index+1,1,limit-1)
        skip_it_ = 0 + solve(prices,index+1,0,limit)

        profit = max(sell_it,skip_it_)

    

    return profit

def solve_memo(prices,index,buy,limit,dp):
    if index >= len(prices):
        return 0
    
    if limit == 0:
        return 0
    
    if dp[index][buy][limit] != -1:

        return dp[index][buy][limit]
    
    profit = 0
    if buy: #! purchased the stock
        buy_it = -prices[index] + solve_memo(prices,index+1,0,limit,dp)
        skip_it = 0 + solve_memo(prices,index +1,1,limit,dp)
        profit = max(buy_it,skip_it)

    else: #! sell'd the stock

        sell_it = prices[index] + solve_memo(prices,index+1,1,limit-1,dp)
        skip_it_ = 0 + solve_memo(prices,index+1,0,limit,dp)

        profit = max(sell_it,skip_it_)


    dp[index][buy][limit] = profit

    return dp[index][buy][limit]

def solve_tab(prices,n):
    dp = [[[0 for limits in range(3)] for cols in range(2)] for rows in range(n+1)]

    profit = 0
    for index in range(n-1,-1,-1):
        for buy in range(0,2):
            for limit in range(1,3):
                if buy: #! purchased the stock
                    buy_it = -prices[index] + dp[index+1][0][limit]
                    skip_it = 0 + dp[index +1][1][limit]
                    profit = max(buy_it,skip_it)
                
                else: #! sell the stock
                    sell_it = prices[index] + dp[index+1][1][limit-1]
                    skip_it_ = 0 + dp[index+1][0][limit]

                    profit = max(sell_it,skip_it_)
                
                dp[index][buy][limit] = profit


    return dp[0][1][2]

def solve_tab_sopt(prices,n):

    next_row= [[0 for col in range(3)] for row in range(2)]
    profit = 0
    for index in range(n-1,-1,-1):
        curr_row = [[0 for col in range(3)] for row in range(2)]
        for buy in range(0,2):
            for limit in range(1,3):
                if buy: #! purchased the stock
                    buy_it = -prices[index] + next_row[0][limit]
                    skip_it = 0 + next_row[1][limit]
                    profit = max(buy_it,skip_it)
                
                else: #! sell the stock
                    sell_it = prices[index] + next_row[1][limit-1]
                    skip_it_ = 0 + next_row[0][limit]

                    profit = max(sell_it,skip_it_)
                
                curr_row[buy][limit] = profit
        
        next_row = curr_row


    return next_row[1][2]



prices = [3,3,5,0,0,3,1,4]
n = len(prices)

print(solve_tab_sopt(prices,n))

