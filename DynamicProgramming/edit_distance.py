def solve(str1,str2,i,j):

    if i == len(str1):
        return len(str2)-j
    
    if j == len(str2):
        return len(str1)-i
    
    ans = 0
    if str1[i] == str2[j]:
        ans = 0 + solve(str1,str2,i+1,j+1)

    else:
        #inset ka case
        ans_insert = 1 + solve(str1,str2,i,j+1)
        
        #delete ka case
        ans_delete =  1 + solve(str1,str2,i+1,j)

        #replace ka case
        ans_replaced = 1 + solve(str1,str2,i+1,j+1)

        ans = min(ans_insert,ans_delete,ans_replaced)

    
    return ans

        
def solve_memo(str1,str2,i,j,dp):
    if i == len(str1):
        return len(str2)-j

    if j == len(str2):
        return len(str1)-i

    
    if dp[i][j] != -1:
        return dp[i][j]
        
    ans = 0
    if str1[i] == str2[j]:
        ans = 0 + solve_memo(str1,str2,i+1,j+1,dp)

    else:
        #inset ka case
        ans_insert = 1 + solve_memo(str1,str2,i,j+1,dp)
        
        #delete ka case
        ans_delete =  1 + solve_memo(str1,str2,i+1,j,dp)

        #replace ka case
        ans_replaced = 1 + solve_memo(str1,str2,i+1,j+1,dp)

        ans = min(ans_insert,ans_delete,ans_replaced)

    dp[i][j] = ans

    return dp[i][j]

def solve_tab(str1,str2):
    dp = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    str1_len = len(str1)
    str2_len = len(str2)

    # j iterate through 0 - len(str2)
    for j in range(0,str2_len):
        dp[len(str1)][j] = str2_len - j

    # i  iterate through 0 - len(str1)
    for i in range(0,str1_len):
        dp[i][str2_len] = str1_len - i

    for i in range(str1_len-1,-1,-1):
        for j in range(str2_len-1,-1,-1):
            
            ans = 0
            if str1[i] == str2[j]:

                ans = 0 + dp[i+1][j+1]

            else:
                #inset ka case
                ans_insert = 1 + dp[i][j+1]
                
                #delete ka case
                ans_delete =  1 + dp[i+1][j]

                #replace ka case
                ans_replaced = 1 + dp[i+1][j+1]

                ans = min(ans_insert,ans_delete,ans_replaced)

            
            dp[i][j] = ans


    return dp[0][0]

def solve_tab_SOPT(str1,str2):
    str1_len = len(str1)
    str2_len = len(str2)
    
    next_row = [0 for _ in range(str2_len+1)]

    for j in range(0,str2_len):
        next_row[j] = str2_len - j



    for i in range(str1_len-1,-1,-1):
        curr_row = [0 for _ in range(str2_len+1)]
        # important catch
        curr_row[str2_len] = str1_len-i
        for j in range(str2_len-1,-1,-1):
            
            ans = 0
            if str1[i] == str2[j]:

                ans = 0 + next_row[j+1]

            else:
                #inset ka case
                ans_insert = 1 + curr_row[j+1]
                
                #delete ka case
                ans_delete =  1 + next_row[j]

                #replace ka case
                ans_replaced = 1 + next_row[j+1]

                ans = min(ans_insert,ans_delete,ans_replaced)

            
            curr_row[j] = ans

        next_row = curr_row

    return next_row[0]




word1 = "horse"
word2 = "ros"

dp = [[-1 for j in range(len(word2))] for i in range(len(word1))]

print(solve_tab_SOPT(word1,word2))