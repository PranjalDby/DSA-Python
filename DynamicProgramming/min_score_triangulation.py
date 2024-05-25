"""
:::Minimum Score of Triangulation of polygon:::

You Have Given convex n-sided polygon where each vertex has an integer value.you are given an integer array `values` where values[i] is the value of ith vertex: we will have to triangulate the polygon into n-2 triangles,the value of that triangle is the product of the values of its vertices,and the total score of triangulation is the sum of these values over all n-2  triangles in the triangulation.

return the minimum of possible scores thart you acheive with triangulation/
"""

INT_MAX = 100000000
def mini_score(values,i,j):

    # base case: if we have only two points

    if i+1 == j:
        return 0
    
    # to choose k
    ans = INT_MAX
    for k in range(i+1,j):
        ans = min(ans,(values[i] * values[j] * values[k]) + mini_score(values,i,k) + mini_score(values,k,j))

    
    return ans


def mini_score_Memo(values,i,j,dp):

    # base case: if we have only two points,if first node = last node

    if i+1 == j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    # to choose k
    ans = INT_MAX
    for k in range(i+1,j):
        ans = min(ans,(values[i] * values[j] * values[k]) + mini_score_Memo(values,i,k,dp) + mini_score_Memo(values,k,j,dp))

    dp[i][j] = ans
    return ans


def mini_score_Tab(values):
    dp = [[0 for i in range(len(values)+1)] for j in range(len(values) + 1)]
    for i in range(len(values)-1,-1,-1):
        for j in range(i+2,len(values)):
            ans = INT_MAX
            for k in range(i+1,j):
                ans = min(ans,(values[i] * values[j] * values[k]) + dp[i][k] + dp[k][j])
            
            dp[i][j] = ans

    return dp[0][len(values)-1]


values = [1,2,3]
dp = [[-1 for i in range(len(values) + 1)] for j in range(len(values) + 1)]
# print(dp)
# print(mini_score(values,0,len(values)-1))
print(mini_score_Tab(values))