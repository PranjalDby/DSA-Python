# MCM or matrix chain multiplication :
# MCM is optimization problem which helps us to compute the product of matrices in most efficient way possible.
# in problem we have given a chain of matrices of length n and we have to calculate the minimum cost to multiply the matrices.
from min_score_triangulation import INT_MAX


# recursive approach takes O(n**3) overall complexity
def min_cost_matrix_chain_mult(mat_chain,i,j):
    if i+1 == j:
        return 0
    
    # we have k choices from i+1 to j-1
    ans = INT_MAX
    for k in range(i+1,j):
        ans = min(ans,(mat_chain[i] * mat_chain[k] * mat_chain[j]) + min_cost_matrix_chain_mult(mat_chain,i,k) + min_cost_matrix_chain_mult(mat_chain,k,j))
    

    return ans


#time-complexity = O(i * j * k) and space-complexity = O(n * m)
def min_cost_matrix_chain_memo(mat_chain,i,j,dp):

    #base -case
    if i+1 == j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    ans = INT_MAX
    for k in range(i+1,j):
        ans = min(ans,(mat_chain[i] * mat_chain[k] * mat_chain[j]) + min_cost_matrix_chain_memo(mat_chain,i,k,dp) + min_cost_matrix_chain_memo(mat_chain,k,j,dp))
    
    dp[i][j] = ans
    return ans
    
def min_cost_mat_chain_tab(mat_chain):
    dp = [[0 for i in range(len(mat_chain))] for j in range(len(mat_chain))]

    # analyze-base case

    for i in range(len(mat_chain)-1,-1,-1):
        for j in range(i+2,len(mat_chain)):
            # we have k-choices for our mat[i][j]
            ans = INT_MAX
            for k in range(i+1,j):
                ans = min(ans,(mat_chain[i] * mat_chain[k] * mat_chain[j]) + dp[i][k] + dp[k][j])
            
            dp[i][j] = ans

    return dp[0][len(mat_chain)-1]

    
if __name__ == "__main__":
    mat_chain = [5,10,8,5]
    # dp = [[-1 for i in range(len(mat_chain) + 1)] for k in range(len(mat_chain) + 1)]
    # print(dp)
    print("minimum cost = ",min_cost_mat_chain_tab(mat_chain))