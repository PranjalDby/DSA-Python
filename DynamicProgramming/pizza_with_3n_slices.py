# hint: based house robberry question

def pizza_sum_max(slices,index,end_index,n):

    if n == 0 or index > end_index:
        return 0
    
    take = slices[index] + pizza_sum_max(slices,index+2,end_index,n-1)
    notTake = 0 + pizza_sum_max(slices,index+1,end_index,n)

    return max(take,notTake)


def pizza_sum_max_memo(slices,index,end_index,n,dp):

    if n == 0 or index > end_index :
        return 0
    
    if dp[index][n] != -1:
        return dp[index][n]
    

    take = slices[index] + pizza_sum_max_memo(slices,index+2,end_index,n-1,dp)
    notTake = 0 + pizza_sum_max_memo(slices,index+1,end_index,n,dp)

    dp[index][n] =  max(take,notTake)

    return dp[index][n]


def bottom_Up(slices):
    k = len(slices)
    dp1 = [[0 for i in range(k+2)] for j in range(k+2)]
    dp2 = [[0 for i in range(k+2)] for j in range(k+2)]

    # case 1
    for index in range(k-2,-1,-1):
        for n in range(1,(k//3)+1):
            include = slices[index] + dp1[index+2][n-1]
            exclude =  0 + dp1[index+1][n]

            dp1[index][n] = max(include,exclude)

    case1 = dp1[0][k//3]

    # case2
    for index2 in range(k-1,0,-1):
        for n in range(1,(k//3)+1):
            include = slices[index2] + dp2[index2+2][n-1]
            exclude =  0 + dp2[index2+1][n]

            dp2[index2][n] = max(include,exclude)

    case2 = dp2[1][k//3]

    return max(case1,case2)

def bottom_Up_SOPT(slices):
    k = len(slices)

    curr1 = [0] * (k+2)
    next1 = [0] * (k+2)
    prev1 = [0] * (k+2)
    # case 1
    for index in range(k-2,-1,-1):
        # curr1 = [0] * (k+2)
        prev1 = [0]*(k+2)
        for n in range(1,(k//3)+1):
            include = slices[index] + next1[n-1]
            exclude =  0 + curr1[n]

            prev1[n] = max(include,exclude)
        
        next1 = curr1
        curr1 = prev1

    print(next1)
    case1 = curr1[k//3]

    curr2 = [0] * (k+2)
    next2 = [0] * (k+2)
    prev2 = [0] * (k+2)
    # case2
    for index2 in range(k-1,0,-1):
        # curr2 = [0] * (k+2)
        prev2 = [0] * (k+2)
        for n in range(1,(k//3)+1):
            include = slices[index2] + next2[n-1]
            exclude =  0 + curr2[n]

            prev2[n] = max(include,exclude)

        next2 = curr2
        curr2 = prev2

    print(next2)
    case2 = curr2[k//3]

    return max(case1,case2)


sliced = [1,2,3,4,5,6]
slices = [8,9,8,6,1,1]
k = len(slices)
# print(k/3)
# dp = [[-1 for i in range(k)] for j in range(k)]

# first_incl = pizza_sum_max_memo(sliced,0,k-2,k//3,dp)
# dp2 = [[-1 for i in range(k)] for j in range(k)]
# second_incl = pizza_sum_max_memo(sliced,1,k-1,k//3,dp2)


print(bottom_Up_SOPT(slices))



