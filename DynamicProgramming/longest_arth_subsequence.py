# TOP DOWN
def solve(arr,index,diff):
    if index == -1:
        return 0
    # backward check
    ans = 0
    for j in range(index-1,-1,-1):
        if arr[index]-arr[j] == diff:
            ans = max(ans,1 + solve(arr,j,diff))

    return ans


def solveMemo(arr,index,diff,dp):

    if index == -1:
        return 0
    
    try:
        if dp[index][diff]:
            return dp[index][diff]
    
    except KeyError as e:
        ...

    # backward check
    ans = 0
    for j in range(index-1,-1,-1):
        if arr[index]-arr[j] == diff:
            ans = max(ans,1 + solveMemo(arr,j,diff,dp))

    dp[index][diff] = ans

    return ans


def bottom_up(array,n):

    # base case: if we have 1,2,0 element
    if n <= 2:
        return n
    ans = 0
    dp = [{} for _ in range(n+1)]

    for i in range(1,n):
        for j in range(0,i):
            diff = array[i] - array[j]
            count = 1
            # check if answer already present
            try:
                if dp[j][diff]:
                   count =  dp[j][diff]
            
            except KeyError as e:
                ...

            # here we add 1 becuase we want to include the i
            dp[i][diff] = count + 1
            ans = max(ans,dp[i][diff])

    return ans

def bottom_up_SOPT(array,n):

    # base case: if we have 1,2,0 element
    if n <= 2:
        return n
    
    ans = 1
    dp = [2 for i in range(n)]

    for j in range(n-3,-1,-1):
        i = j-1 # a term
        k = j+1 # c term
        while i>= 0 and k<n:

            if array[i] + array[k] == 2 * array[j]:
                # this case ensure to include the element by incrementing count. this ensures that we found the first sequence
                dp[j] = max(dp[k]+1,dp[j])
                ans = max(ans,dp[j])
                i-=1
                k+=1

            elif array[i] + array[k] < 2 * array[j]:
                k+=1

            else:
                i-=1

    return ans


def length_longestAp(arr,n):

    dp = [{} for _ in range(n+1)]
    if n <= 2:
        return n
    
    ans = 0
    for i in range(0,n):
        for j in range(i+1,n):
            # 2 is added becuase we already find some AP of length 2
            ans = max(ans, 2 + solveMemo(arr,i,arr[j]-arr[i],dp))

    return ans


print(bottom_up_SOPT([2, 4, 7, 9, 10],5))
dp = {k:2 for k in range(5+1)}
print(dp)
