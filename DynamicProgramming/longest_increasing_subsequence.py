
def longest_incr_subsequence(array,index,prev):

    if index == len(array):
        return 0
    
    # include
    incl = 0
    if prev == -1 or array[index] > array[prev]:
        incl = 1 + longest_incr_subsequence(array,index + 1,index)

    # exclude
    excl = 0 + longest_incr_subsequence(array,index+1,prev)


    return max(incl,excl)

def longest_incr_subsequence_Memo(array,index,prev,dp):

    if index == len(array):
        return 0
    
    if dp[index][prev] != -1:
        return dp[index][prev]
    
    # include
    incl = 0
    if prev == -1 or array[index] > array[prev]:
        incl = 1 + longest_incr_subsequence_Memo(array,index + 1,index,dp)

    # exclude
    excl = 0 + longest_incr_subsequence_Memo(array,index+1,prev,dp)

    dp[index][prev+1] = max(incl,excl)
    
    return dp[index][prev+1] # prev +1 is to not throw invalid index


def bottom_up_lngst_incr_subs(array):
    n = len(array)
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    for index in range(n-1,-1,-1):

        for prev in range(index-1,-2,-1):

            incl = 0
            if prev == -1 or array[index] > array[prev]:
                incl = 1 + dp[index + 1][index+1] # index + 1 becuase we to move prev to curr and curr to the next index

            excl = 0 + dp[index + 1][prev+1]

            dp[index][prev + 1] = max(incl,excl)


    return dp[0][0]

def bottom_up_lngst_incr_subs_SOPT(array):
    n = len(array)

    next = [0] * (n+1)
    curr = [0] * (n+1)

    for index in range(n-1,-1,-1):
        for prev in range(index-1,-2,-1):

            incl = 0
            if prev == -1 or array[index] > array[prev]:

                incl = 1 + next[index+1] # index + 1 becuase we to move prev to curr and curr to the next index

            excl = 0 + next[prev+1]

            curr[prev + 1] = max(incl,excl)

        next = curr
    

    return next[0]

def getJustBadaElement_binarysearch(array,element):
    i = 0
    n = len(array)

    while i < n:
        mid = i + (n-i)//2
        if array[mid] >= element:
            n = mid

        else:
            i = mid+1

    return n
def dp_binarysearch_sol(array):
    n = len(array)
    if n == 0:
        return 0
    
    res = []
    res.append(array[0])

    for i in range(1,n):
        if array[i] > res[-1]:
            res.append(array[i])
        else:
            # find index of just bada element
            just_bada_element = getJustBadaElement_binarysearch(res,array[i])
            print(just_bada_element)
            res[just_bada_element] = array[i]

    return len(res)

arr = "0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15".split(" ")
arr = [int(i) for i in arr]
# dp = [[-1 for i in range(len(arr)+1)] for j in range(len(arr))]
print(dp_binarysearch_sol(arr))
