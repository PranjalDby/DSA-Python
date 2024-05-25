class Solution:  
    def solve(self,prices,index,buy,k):
            if k == 0:
                return 0
            
            if index >= len(prices):
                return 0

            profit = 0
            if buy:

                #buy karo or skip karo
                buyit = -prices[index] + self.solve(prices ,index + 1,0,k)
                skipit = 0 + self.solve(prices,index + 1,1,k)

                profit = max(buyit,skipit)

            else:
                #sell karo or skip karo

                sellit = prices[index]  + self.solve(prices,index+1,1,k-1)
                skipit  = 0 + self.solve(prices,index+1,0,k)

                profit = max(sellit,skipit)


            return profit

    def solve_memo(self,prices,index,buy,k,dp):
        if k == 0:
            return 0
        
        if index >= len(prices):
            return 0
        
        if dp[index][buy][k] != -1:
            return dp[index][buy][k]

        profit = 0
        if buy:

            #buy karo or skip karo
            buyit = -prices[index] + self.solve_memo(prices ,index + 1,0,k,dp)
            skipit = 0 + self.solve_memo(prices,index + 1,1,k,dp)

            profit = max(buyit,skipit)

        else:
            #sell karo or skip karo

            sellit = prices[index]  + self.solve_memo(prices,index+1,1,k-1,dp)
            skipit  = 0 + self.solve_memo(prices,index+1,0,k,dp)

            profit = max(sellit,skipit)

        dp[index][buy][k] = profit
        return dp[index][buy][k]
    


def solve_tab(prices,n,k):
    dp = [[[0 for k_ in range(k+1)] for col in range(2)] for row in range(len(prices)+1)]
    
    profit = 0
    for index in range(n-1,-1,-1):
        for buy in range(0,2):
            for k_ in range(1,k+1):
                if buy:
                    #buy karo or skip karo
                    buyit = -prices[index] + dp[index + 1][0][k_]
                    skipit = 0 + dp[index + 1][1][k_]

                    profit = max(buyit,skipit)

                else:
                    #sell karo or skip karo

                    sellit = prices[index]  + dp[index+1][1][k_-1]
                    skipit  = 0 + dp[index+1][0][k_]

                    profit = max(sellit,skipit)

                dp[index][buy][k_] = profit


    print(dp)
    
    return dp[0][1][k]


def solve_tab_sopt(prices,n,k):

    next_row = [[0 for col in range(k+1)] for row in range(2)]
    profit = 0
    for index in range(n-1,-1,-1):
        curr_row = [[0 for col in range(k+1)] for row in range(2)]
        for buy in range(0,2):
            for k_ in range(1,k+1):
                if buy:
                    #buy karo or skip karo
                    buyit = -prices[index] + next_row[0][k_]
                    skipit = 0 + next_row[1][k_]

                    profit = max(buyit,skipit)

                else:
                    #sell karo or skip karo

                    sellit = prices[index]  + next_row[1][k_-1]
                    skipit  = 0 + next_row[0][k_]

                    profit = max(sellit,skipit)

                curr_row[buy][k_] = profit
            
        next_row = curr_row


    print(next_row)
    return next_row[1][k]



def using_no_of_transactions(prices,index,operations,k):
    if index >= len(prices):
        return 0
    
    if operations >= (2 * k):
        return 0
    
    
    profit = 0
    if operations % 2 == 0:
        buy_it = -prices[index] + using_no_of_transactions(prices,index+1,operations+1,k)
        skip_it = 0 + using_no_of_transactions(prices,index+1,operations,k)

        profit = max(buy_it,skip_it)

    else:
        sell_it = prices[index] + using_no_of_transactions(prices,index+1,operations+1,k)
        skip_it = 0 + using_no_of_transactions(prices,index+1,operations,k)

        profit = max(sell_it,skip_it)


    return profit

def using_no_of_transactions_memo(prices,index,operations,k,dp):
    if index >= len(prices):
        return 0
    
    if operations >= (2 * k):
        return 0
    

    if dp[index][operations] != -1:
        
        return dp[index][operations]
    
    profit = 0
    if operations % 2 == 0:
        buy_it = -prices[index] + using_no_of_transactions_memo(prices,index+1,operations+1,k,dp)
        skip_it = 0 + using_no_of_transactions_memo(prices,index+1,operations,k,dp)

        profit = max(buy_it,skip_it)

    else:
        sell_it = prices[index] + using_no_of_transactions_memo(prices,index+1,operations+1,k,dp)
        skip_it = 0 + using_no_of_transactions_memo(prices,index+1,operations,k,dp)

        profit = max(sell_it,skip_it)


    dp[index][operations] = profit
    return dp[index][operations]

    
def using_no_of_transactions_tab(prices,n,k):
    # dp = [[0 for k_ in range((2 * k)+1)] for row in range(len(prices)+1)]

    next = [0] * (2 * k + 1)
    profit = 0
    for index in range(n-1,-1,-1):
        curr = [0] * (2 * k + 1)
        for operations in range(0,2 * k):
            if operations % 2 == 0:
                buy_it = -prices[index] + next[operations+1]
                skip_it = 0 + next[operations]

                profit = max(buy_it,skip_it)

            else:
                sell_it = prices[index] + next[operations+1]
                skip_it = 0 + next[operations]
                profit = max(sell_it,skip_it)

            curr[operations] = profit
        
        next = curr

    return next[0]



sol = Solution()

prices = [1,2,4,2,5,7,2,4,9,0]
k = 4
dp = [ [-1 for k_ in range(2 * k)] for row in range(len(prices)+1)]
# print(sol.solve_memo(prices,0,1,k,dp))

print(using_no_of_transactions_tab(prices,len(prices),k))
