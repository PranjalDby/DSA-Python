


def solve_tab(str,revestr):
    dp = [[0 for k in range(len(revestr)+1)] for _ in range(len(str)+1)]
    n = len(str)
    ans =0
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if str[i] == revestr[j]:
                ans = 1 + dp[i+1][j+1]
            
            else:
                increment_i = dp[i+1][j]
                increment_j = dp[i][j+1]
                ans = max(increment_i,increment_j)

            dp[i][j] = ans


    return dp[0][0]


def solve_tab_sopt(str,reverse_str):
    n = len(str)
    ans =0
    next_row = [0 for _ in range(n + 1)]
    for i in range(n-1,-1,-1):
        curr_row = [0 for __ in range(n + 1)]
        for j in range(n-1,-1,-1):
            if str[i] == reverse_str[j]:
                ans = 1 + next_row[j+1]
            
            else:
                increment_i = next_row[j]
                increment_j = curr_row[j+1]
                ans = max(increment_i,increment_j)

            curr_row[j] = ans

        next_row = curr_row

    return next_row[0]


str1 = "acaacab"
reversed_str = str1[::-1]
print(solve_tab_sopt(str1,reversed_str))