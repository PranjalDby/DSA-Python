
def helper(arr,d):
    dp ={}
    ans = 0
    for i in range(len(arr)):
        element = arr[i]-d
        temp_ans = 0
        if element in dp.keys():
            temp_ans = dp[element]

        dp[arr[i]] = 1 + temp_ans

        ans = max(ans,dp[arr[i]])

    
    return ans


arr =[1,3,5,7]
d = 1

print(helper(arr,d))
