# largest square fromed in matrix: given a binary matrix on n * m ans we have to find out the maximum size of square sub-matrix with 1's

def max_square(r,c,mat,maxi):
    # base case
    if r >= len(mat) or c >= len(mat[0]):
        return 0
    
    right = max_square(r,c + 1,mat,maxi)
    diagonal = max_square(r + 1,c + 1,mat,maxi)
    bottom = max_square(r+1,c,mat,maxi)

    if mat[r][c] == 1:
        ans = min(right,min(bottom,diagonal)) + 1
        maxi = max(maxi,ans)
        return ans
    else:
        # matrix contain zero

        return 0
    
def max_square_memo(r,c,mat,maxi,dp):
    # base case
    if r >= len(mat) or c >= len(mat[0]):
        return 0
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    right = max_square_memo(r,c + 1,mat,maxi,dp)
    diagonal = max_square_memo(r + 1,c + 1,mat,maxi,dp)
    bottom = max_square_memo(r+1,c,mat,maxi,dp)

    if mat[r][c] == 1:
        ans = min(right,min(bottom,diagonal)) + 1
        maxi = max(maxi,ans)
        dp[r][c] = maxi
        return ans
    else:
        # matrix contain zero
        dp[r][c] = 0
        return dp[r][c]
    
def max_sqr_tab(mat):
    global maxi
    dp = [[0 for c in range(len(mat[0]) + 1)] for r in range(len(mat) + 1)]
    
    # base case analysis
    dp[len(mat)][len(mat[0])] = 0
    for r in range(len(mat)-1,-1,-1):
        for c in range(len(mat[0])-1,-1,-1):
            right = dp[r][c+1]
            diagonal = dp[r+1][c+1]
            down = dp[r+1][c]

            if mat[r][c] == 1:
                dp[r][c] = 1 + min(right,min(down,diagonal))
                maxi = max(maxi,dp[r][c])
            else:
                dp[r][c] = 0

    
    return dp[0][0]

def max_sqr_tab_spaceOpt(mat):
    global maxi
    curr = [0 for c in range(len(mat[0]) + 1)]
    next = [0 for c in range(len(mat[0]) + 1)]
    # base case analysis
    dp[len(mat)][len(mat[0])] = 0
    for r in range(len(mat)-1,-1,-1):
        for c in range(len(mat[0])-1,-1,-1):
            right = curr[c+1]
            diagonal = next[c+1]
            down = next[c]

            if mat[r][c] == 1:
                curr[c] = 1 + min(right,min(down,diagonal))
                maxi = max(maxi,curr[c])
            else:
                dp[r][c] = 0
        
        # move next to the curr and we then calculate curr
        next = curr
            

    
    return next[0]



mat = [[1,1],
       [1,1]]

r = 2;m = 2
maxi = 0
dp = [[-1 for c in range(m+1)] for j in range(r+1)]
# print(dp)
# maxi = max_square_memo(0,0,mat,maxi,dp)
# print(maxi)

max_sqr_tab_spaceOpt(mat)
print(maxi)
    