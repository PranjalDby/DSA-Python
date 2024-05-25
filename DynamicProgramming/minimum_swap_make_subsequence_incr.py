
# given two arrays of same length;

def solve_min_helper(nums1,nums2):

    nums1.append(0)
    for i in range(len(nums1)-1,-1,-1):
        nums1[i] = nums1[i-1]

    nums1[0] = -1
    nums2.append(0)
    for i in range(len(nums2)-1,-1,-1):
        nums2[i] = nums2[i-1]

    nums2[0] = -1

    # for memoization

    # dp = [[-1 for i in range(3)] for k in range(len(nums1)+1)]

    return solve_min_swapSOPT(nums1,nums2)


INT_MAX = 10 ** 9
def solve_min_swap(nums1,nums2,index,swapped):
    
    if index == len(nums1):
        return 0

    ans = INT_MAX
    prev1 = nums1[index-1]
    prev2 = nums2[index-1]

    # catch
    if swapped == 1:
        temp = prev1
        prev1 = prev2
        prev2 = temp

    # no swap
    if nums1[index] > prev1 and nums2[index] > prev2:

        ans = solve_min_swap(nums1,nums2,index + 1,0)

    # swap :  more generally this is to handle the repition of number
    if nums1[index] > prev2 and nums2[index] > prev1:
        # 1 + to include the swapped way
        ans = min(ans,1 + solve_min_swap(nums1,nums2,index + 1,1))

    
    return ans

def solve_min_swapMEMO(nums1,nums2,index,swapped,dp):
    
    if index == len(nums1):
        return 0


    if dp[index][swapped] != -1:
        return dp[index][swapped]
    
    ans = INT_MAX
    prev1 = nums1[index-1]
    prev2 = nums2[index-1]

    # catch
    if swapped == 1:
        temp = prev1
        prev1 = prev2
        prev2 = temp

    # no swap
    if nums1[index] > prev1 and nums2[index] > prev2:

        ans = solve_min_swapMEMO(nums1,nums2,index + 1,0,dp)

    # swap

    if nums1[index] > prev2 and nums2[index] > prev1:
        # 1 + to include the swapped way
        ans = min(ans,1 + solve_min_swapMEMO(nums1,nums2,index + 1,1,dp))
    
    dp[index][swapped] = ans

    return ans

def solve_min_swapTAB(nums1,nums2):
    # already handled the base case
    dp = [[0 for i in range(3)] for k in range(len(nums1)+1)]

    for index in range(len(nums1)-1,0,-1):
        for swapped in range(1,-1,-1):
            ans = INT_MAX
            prev1 = nums1[index-1]
            prev2 = nums2[index-1]
            if swapped == 1:
                temp = prev1
                prev1 = prev2
                prev2 = temp
            
             # no swap
            if nums1[index] > prev1 and nums2[index] > prev2:
                ans = dp[index+1][0]

            # swap
            if nums1[index] > prev2 and nums2[index] > prev1:
                # 1 + to include the swapped way
                ans = min(ans,1 + dp[index+1][1])

            dp[index][swapped] = ans

    
    return dp[1][1]

def solve_min_swapSOPT(nums1,nums2):
    # already handled the base case
    
    swap = 0
    noswap = 0
    for index in range(len(nums1)-1,0,-1):
        currentSwap = 0
        current_noSwap = 0
        for swapped in range(1,-1,-1):
            ans = INT_MAX
            prev1 = nums1[index-1]
            prev2 = nums2[index-1]
            if swapped == 1:
                temp = prev1
                prev1 = prev2
                prev2 = temp
            
             # no swap
            if nums1[index] > prev1 and nums2[index] > prev2:
                ans = noswap

            # swap
            if nums1[index] > prev2 and nums2[index] > prev1:
                # 1 + to include the swapped way
                ans = min(ans,1 + swap)

            if swapped:
                currentSwap = ans

            else:
                current_noSwap = ans

        # moving from last row to first row
        swap = currentSwap
        noswap = current_noSwap
            

    
    return min(swap,noswap)


num1 = [1,3,5,4]; 
num2 = [1,2,3,7]

ans = solve_min_helper(num1,num2)
print(ans)