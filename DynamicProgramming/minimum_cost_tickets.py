# we have i/p array consisting of no of days and a cost array which denotes the cost of 1 day pass,7 day pass and 30 day pass



def minimum_cost(days,costs,index):

    # base case
    if index >= len(days):
        return 0

    taking_day1pass = costs[0] + minimum_cost(days,costs,index + 1)

    # 7 day pass

    i = index

    while (i < len(days) and days[i] < days[index] + 7): i+=1
    taking_7daypass = costs[1] + minimum_cost(days,costs,i)

    i = index
    # 30 day pass
    while (i < len(days) and days[i] < days[index] + 30): i+=1
    taking_30daypass = costs[2] + minimum_cost(days,costs,i)



    ans = min(taking_day1pass,taking_7daypass,taking_30daypass)


    return ans


def minimum_cost_memo(days,costs,index,dp):

    # base case
    if index >= len(days):
        return 0
    

    if dp[index] != -1:
        return dp[index]

    taking_day1pass = costs[0] + minimum_cost_memo(days,costs,index + 1,dp)

    # 7 day pass

    i = index

    while (i < len(days) and days[i] < days[index] + 7): i+=1



    taking_7daypass = costs[1] + minimum_cost_memo(days,costs,i,dp)


    i = index
    # 30 day pass
    while (i < len(days) and days[i] < days[index] + 30): i+=1

    taking_30daypass = costs[2] + minimum_cost_memo(days,costs,i,dp)



    dp[index] = min(taking_day1pass,taking_7daypass,taking_30daypass)


    return dp[index]





INT_MAXX = 10 ** 9

def minimum_cost_tab(days,costs):
    dp = [INT_MAXX] * (len(days) + 1)

    dp[len(days)] = 0
    
    # bottom-up approach

    for k in range(len(days)-1,-1,-1):

        taking_day1pass = costs[0] + dp[k + 1]

        i = k

        while (i < len(days) and days[i] < days[k] + 7): i+=1

        taking_7daypass = costs[1] + dp[i]


        
        # 30 day pass
        while (i < len(days) and days[i] < days[k] + 30): i+=1

        taking_30daypass = costs[2] + dp[i]

        dp[k] = min(taking_day1pass,taking_7daypass,taking_30daypass)


    print(dp)
    return dp[0]


import queue
from collections import deque

def minimum_cost_tab_sopt(days,cost):
    weekly_queue = queue.Queue() #queue to track the weeks
    monthly_queue = queue.Queue() # queue to track the months
    ans = 0

    for day in days:
        # remove expired days
        while not weekly_queue.empty() and weekly_queue.queue[0][0] + 7 <= day:
            weekly_queue.get()
        

        while not monthly_queue.empty() and monthly_queue.queue[0][0] + 30 <= day:
           monthly_queue.get()

        # add cost for current day
            
        weekly_queue.put((day,ans + cost[1]))
        monthly_queue.put((day,ans + cost[2]))

        ans = min(ans + cost[0],min(weekly_queue.queue[0][1],monthly_queue.queue[0][1]))
    
    return ans

days = [1,3,4,5,7,8,10]
costs = [2,7,20]

# dp = [-1] * (len(days) + 1)

print(minimum_cost_tab(days,costs))