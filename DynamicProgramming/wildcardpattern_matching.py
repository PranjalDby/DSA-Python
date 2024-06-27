
def solve(s,pattern,i,j):
    if i < 0 and j < 0:
        return True
    
    #if our pattern is fully cosumed but pattern not
    if i >= 0 > j:
        return False
    
    if i < 0 <= j:
        for k in range(j+1):
            if pattern[k] != "*":
                return False
            
        return True
    
    #case 1
  
    if s[i] == pattern[j] or pattern[j] == "?":
        return solve(s,pattern,i-1,j-1)
    
    elif pattern[j] == "*":
    
        return solve(s, pattern, i - 1, j) or solve(s, pattern, i, j - 1)

    else:
        # pattern is invalid
        return False
    
def solve_with1_based_index(s,pattern,i,j):
    if i == 0 and j == 0:
        return True
    
    #if our pattern is fully cosumed but pattern not
    if i>0 and j == 0:
        return False
    
    if i == 0 and j>0:
        for k in range(1,j+1):
            if pattern[k-1] != "*":
                return False
            
        return True
    
    #case 1
  
    if s[i-1] == pattern[j-1] or pattern[j-1] == "?":
        return solve(s,pattern,i-1,j-1)
    
    elif pattern[j - 1] == "*":
    
        return solve(s, pattern, i - 1, j) or solve(s, pattern, i, j - 1)

    else:
        # pattern is invalid
        return False
    

def solve_memo(s,pattern,i,j,dp):
    if i < 0 and j < 0:
        return True
    
    #if our pattern is fully cosumed but out string not
    if i >= 0 > j:
        return False
    
    if i < 0 <= j:
        for k in range(j+1):
            if pattern[k] != "*":
                return False
            
        return True
    
    if dp[i][j] != -1:
        return dp[i][j]
    #case 1
    ans: bool = False
    if s[i] == pattern[j] or pattern[j] == "?":
        ans = solve_memo(s,pattern,i-1,j-1,dp)
    
    elif pattern[j] == "*":
       
        # replacing * with any no of characters
        ans1 = solve_memo(s,pattern,i-1,j,dp)
    
        # replacing * with an empty string:
        ans2 = solve_memo(s,pattern,i,j-1,dp)

        ans = ans1 or ans2
    else:
        # pattern is invalid
        return False
    
    dp[i][j] = ans

    return ans
    

def solve_tab(s,p):
    dp = [[0 for col in range(len(p)+1)] for row in range(len(s)+1)]

    dp[0][0] = True
    for j in range(1,len(p)+1):
        flag = True
        for k in range(1,j+1):
            if p[k-1] != "*":
                flag = False
                break
            
        dp[0][j] = flag

    j = 0

    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            if s[i-1] == p[j-1] or p[j-1] == "?":
                dp[i][j] = dp[i-1][j-1]
            
            elif p[j - 1] == "*":
            
                dp[i][j] = dp[i-1][j] or dp[i][j-1]

            else:
                # pattern is invalid
                dp[i][j] = False

    
    return dp[len(s)][len(p)]

def solve_tab_sopt(s,p):
    
    prev_row = [0] * (len(p) + 1)

    prev_row[0] = True
    for j in range(1,len(p)+1):
        flag = True
        for k in range(1,j+1):
            if p[k-1] != "*":
                flag = False
                break
            
        prev_row[j] = flag

    j = 0

    for i in range(1,len(s)+1):
        curr_row = [0] * (len(p) + 1)
        for j in range(1,len(p)+1):
            if s[i-1] == p[j-1] or p[j-1] == "?":
                curr_row[j] = prev_row[j-1]
            
            elif p[j - 1] == "*":
            
                curr_row[j] = prev_row[j] or curr_row[j-1]

            else:
                # pattern is invalid
                curr_row[j] = False

        prev_row = curr_row

    return prev_row[len(p)]

    
        


          
s = "aab";p = "c*a*b"

# dp = [[-1 for col in range(len(p)+1)] for row in range(len(s)+1)]

print(solve_tab_sopt(s,p))



#----------------------------------------------------- DYNAMIC PROGRAMMING COMPLETE ---------------------------------------------------------------------------