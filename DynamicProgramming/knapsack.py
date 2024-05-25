import sys

def knapsack_impl(weight,value,max_weight,index):

    # base case: if only one item to steal, then compare if we capacity to hold it or not
    if index == 0:
        if weight[index] <= max_weight:
            return value[0]
        else:
            return 0
        
    
    incl = 0
    
    if(weight[index] <= max_weight):
        incl = knapsack_impl(weight,value,max_weight-weight[index],index - 1) + value[index]

    excl = 0
    excl = knapsack_impl(weight,value,max_weight,index-1) + 0

    return max(incl,excl)


def knapsack_impl_memoized(weight,value,capacity,index,dp):

    # Base Case
    if index == 0:
        if weight[index] <= capacity:
            return value[index]
        
        else:
            return 0
    
    if dp[index][capacity] != -1:
        return dp[index][capacity]

    include = 0
    exclude = 0
    if weight[index] <= capacity:
        include = knapsack_impl_memoized(weight,value,capacity-weight[index],index-1,dp) + value[index]

    
    exclude = knapsack_impl_memoized(weight,value,capacity,index-1,dp) + 0

    ans = max(include,exclude)

    dp[index][capacity] = ans

    return dp[index][capacity]
        

def knapsack_impl_tab(weight,value,capacity,index):
    dp = [[0 for i in range(capacity+1)] for j in range(index)]
    
    # Analyse Base case
    for w in range(weight[0],capacity+1):
        if weight[0] <= w:
            dp[0][w] = value[0]
        else:
            dp[0][w] = 0

    for ind in range(1,index):

        for w in range(0,capacity+1):
            include = 0
            if weight[ind] <= w:
                include = dp[ind-1][w-weight[ind]] + value[ind]
            
            exclude = 0 + dp[ind-1][w]

            dp[ind][w] = max(include,exclude)

        
    
    return dp[index-1][capacity]

def knapsack_impl_tab_sopt(weight,value,capacity,n):

    # prev = [0] * (capacity + 1)
    curr = [0] * (capacity + 1) 

    # Base case Analysis
    for w in range(weight[0],capacity+1):

        if w <= capacity:

            curr[w] = value[0]

        else:
            curr[w] = 0        


    for index in range(1,n):

        for w in range(capacity,0,-1):

            include = 0
            if weight[index] <= w:
                include = value[index] + curr[w-weight[index]]

            exclude = curr[w] + 0

            curr[w] = max(exclude,include)

        

    return curr[capacity]

if __name__ == "__main__":

    weight = [6 ,5 ,1 ,5 ,6 ,5 ,9 ]
    max_w = 7
    n = 7
    value = [5, 3, 4, 9 , 6 ,1, 1]

    dp = [[-1 for i in range(max_w + 1)] for i in range(n)] #2d dp array becuase of 2D dynamic programming
 
    print(knapsack_impl_memoized(weight,value,max_w,n-1,dp))
    # print(knapsack_impl_tab(weight,value,max_w,n))

    # if len(sys.argv) < 2:
    #     print ("Error You")
    # else:
        
    #     T = 0
    #     n = 0;values = []
    #     weight = []
    #     W = 0
    #     print("module namwe",sys.argv[0])
    #     for i in range(len(sys.argv)):
    #         print("loop runninf")
    #         print(sys.argv[i])

