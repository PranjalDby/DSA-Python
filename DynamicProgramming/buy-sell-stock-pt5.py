def solve(prices,index,buy,fees):
    if index == len(prices):
        return 0
    
    profit = 0
    if buy:
        buy_it = -prices[index] + solve(prices,index+1,0,fees)
        skipit = 0 + solve(prices,index+1,1,fees)
        profit = max(buy_it,skipit)

    else:
        # here a complete transactions take place,so subtract with fees
        sell_it = prices[index]-fees + solve(prices,index+1,1,fees)
        skipit = 0 + solve(prices,index+1,0,fees)
        profit = max(sell_it,skipit)

    return profit


def solve_memo(prices,index,buy,fees,dp):
    if index == len(prices):
        return 0
    
    if dp[index][buy] != -1:
        return dp[index][buy]
    
    profit = 0
    if buy:
        buy_it = -prices[index] + solve(prices,index+1,0,fees)
        skipit = 0 + solve(prices,index+1,1,fees)
        profit = max(buy_it,skipit)

    else:
        # here a complete transactions take place,so subtract with fees
        sell_it = prices[index]-fees + solve(prices,index+1,1,fees)
        skipit = 0 + solve(prices,index+1,0,fees)
        profit = max(sell_it,skipit)

    dp[index][buy] = profit
    return dp[index][buy]

def solve_tab(prices,fee):
    n = len(prices)
    dp = [[0 for col in range(2)] for row in range(n+1)]
    profit = 0
    for index in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                buy_it = -prices[index] + dp[index+1][0]
                skipit = 0 + dp[index+1][1]
                profit = max(buy_it,skipit)

            else:
                # here a complete transactions take place,so subtract with fees
                sell_it = prices[index]-fee + dp[index+1][1]
                skipit = 0 + dp[index+1][0]
                profit = max(sell_it,skipit)
            
            dp[index][buy] = profit


    return dp[0][1]

def solve_tab_sopt(prices,fee):
    n = len(prices)
    next_row = [0 for _ in range(2)]
    profit = 0
    for index in range(n-1,-1,-1):
        curr_row = [0 for _ in range(2)]
        for buy in range(2):
            if buy:
                buy_it = -prices[index] + next_row[0]
                skipit = 0 + next_row[1]
                profit = max(buy_it,skipit)

            else:
                # here a complete transactions take place,so subtract with fees
                sell_it = prices[index]-fee + next_row[1]
                skipit = 0 + next_row[0]
                profit = max(sell_it,skipit)
            
            curr_row[buy] = profit

        next_row = curr_row


    return next_row[0][1]




