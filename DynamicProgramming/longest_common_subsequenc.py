def solve(str1,str2,i,j):
    if i == len(str1) or j == len(str2):
        return 0
    
    # if match found
    ans = 0
    if str1[i] == str2[j]:
        ans = 1 + solve(str1,str2,i+1,j+1)
    
    # if match not found
    else:
        increment_i = solve(str1,str2,i+1,j)
        increment_j = solve(str1,str2,i,j+1)
        
        ans = max(increment_i,increment_j)

    
    return ans

def solve_memo(str1,str2,i,j,dp):
    if i == len(str1) or j == len(str2):
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    # if match found
    ans = 0
    if str1[i] == str2[j]:
        ans = 1 + solve_memo(str1,str2,i+1,j+1,dp)
    
    # if match not found
    else:
        increment_i = solve_memo(str1,str2,i+1,j,dp)
        increment_j = solve_memo(str1,str2,i,j+1,dp)
        
        ans = max(increment_i,increment_j)

    dp[i][j] = ans

    return dp[i][j]

print("prankd".index('p'))
def solve_tab(text1,text2):
    dp = [[0 for col in range(len(text2)+1)] for row in range(len(text1)+1)]
    
    ans = 0
    for index1 in range(len(text1)-1,-1,-1):
        for index2 in range(len(text2)-1,-1,-1):
            if text1[index1] == text2[index2]:
                ans = 1 + dp[index1+1][index2+1]
            
            # if match not found
            else:
                increment_i = dp[index1+1][index2]
                increment_j = dp[index1][index2 + 1]                
                ans = max(increment_i,increment_j)

            dp[index1][index2] = ans


    return dp[0][0]

def solve_tab_sopt(text1,text2):
   
    next_row = [0 for i in range(len(text2)+1)]
    ans = 0
    for index1 in range(len(text1)-1,-1,-1):
        curr_row = [0 for k in range(len(text2)+1)]
        for index2 in range(len(text2)-1,-1,-1):
            if text1[index1] == text2[index2]:
                ans = 1 + next_row[index2+1]
            
            # if match not found
            else:
                increment_i = next_row[index2]
                increment_j = curr_row[index2 + 1]                
                ans = max(increment_i,increment_j)

            curr_row[index2] = ans

        next_row = curr_row


    return next_row[0]


text1 ="abcde";text2 = "ace"

print(solve_tab_sopt(text1,text2))