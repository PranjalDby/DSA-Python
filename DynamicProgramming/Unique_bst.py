
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def do_bst(root,data,n):

    # base case
    if data >= n :
        return 1
    
    if root == None:
        root = Node(data)

    left_ans = 1
    # left-subtree
    if root.data > data and root.data != data:
        left_ans = left_ans + do_bst(root.left,data+1,n)
    

    right_ans = 1
    # right-subtree
    if root.data < data and root.data != data:
        right_ans = right_ans + do_bst(root.right,data+1,n)

    
    return left_ans * right_ans

def solve(n):
    if n <= 1:
        return 1
    
    ans = 0

    for i in range(1,n+1):
        ans += solve(i-1) * solve(n-i)

    return ans

def solve_memo(n,dp):
    if n <= 1:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    ans = 0

    for i in range(1,n+1):
        ans += solve_memo(i-1,dp) * solve_memo(n-i,dp)

    dp[n] = ans
    return dp[n]


def solve_tab(n):
    dp = [0 for _ in range(n+1)]

    dp[0] = dp[1] = 1

    for i in range(2,n+1):
        # j-root node
        for j in range(1,i+1):
            dp[i] += dp[j-1] * dp[i-j]

    
    print(dp)
    return dp[n]


# using catalan number 
"""
formula for calculating catalan 

cn = (2n)!//(n+1)! * n!

"""


def catalan(n):
    if n <= 1:
        return 1
    
    ans = 0
    for i in range(0,n):
        ans += catalan(i) * catalan(n-i-1)

    return ans
        



n = 3
dp = [-1 for _ in range(n+1)]
res = catalan(n)
print(res)