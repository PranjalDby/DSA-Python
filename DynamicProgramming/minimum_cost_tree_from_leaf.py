


def solve(arr,left,right,maxi):

    # leaf node
    if left == right:
        return 0
    
    ans = float('inf')
    # loop for dividing array into left-subtree and right subtree
    for k in range(left,right):
        ans = min(ans,(maxi[(left,k)] * maxi[(k+1,right)] + solve(arr,left,k,maxi) + solve(arr,k+1,right,maxi)))


    return ans





def solve_helper(arr):
    precomputed_max_node = {}
    # calculating maxi of leaf node
    for i in range(0,len(arr)):
        precomputed_max_node[(i,i)] = arr[i]
        for j in range(i+1,len(arr)):
            precomputed_max_node[(i,j)] = max(arr[j],precomputed_max_node[(i,j-1)])

    
    ans = solve(arr,0,len(arr)-1,precomputed_max_node)
    print(ans)
    

ip = [3,6,4,7,2,5]

solve_helper(ip)

