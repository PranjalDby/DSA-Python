# cut the rods of length 'N' into given {x,y,z segments}
# we have to determine the maximum no of segments.

from pickle import INT


INT_MIN = float('-inf')
def maxRodCuts(n,x,y,z):
    
    if n == 0:
        return 0
    
    if n < 0:
        # if n is negative.this is when legth of segment is greater than our remaining length of rod.
        # so, we return -infinity
        return INT_MIN
    
    for_x = maxRodCuts(n-x,x,y,z) + 1
    for_y = maxRodCuts(n-y,x,y,z) + 1
    for_z = maxRodCuts(n-z,x,y,z) + 1

    ans = max(for_x,for_y,for_z)

    return ans

def maxRodCutsMemoized(n,x,y,z,dp):
    
    if n == 0:
        return 0
    
    if n < 0:
        # if n is negative.this is when legth of segment is greater than our remaining length of rod.
        # so, we return -infinity
        return INT_MIN
    
    if dp[n] != INT_MIN:
        return dp[n]
    
    for_x = maxRodCutsMemoized(n-x,x,y,z,dp) + 1
    for_y = maxRodCutsMemoized(n-y,x,y,z,dp) + 1
    for_z = maxRodCutsMemoized(n-z,x,y,z,dp) + 1

    dp[n] = max(for_x,for_y,for_z)

    return dp[n]

def maxRodCutsTab(n,x,y,z):
    dp = [INT_MIN] * (n+1)

    dp[0] = 0
   
    for i in range(1,n+1):
        if i-x >= 0:
            dp[i] = max(dp[i],dp[i-x] + 1)

        if i-y >= 0:
            dp[i] = max(dp[i],dp[i-y] + 1)

        if i-z >= 0:
            dp[i] = max(dp[i],dp[i-z] + 1)
    
    if dp[n] < 0:
        return 0
    
    else:
        return dp[n]




rod_len = 7
x = 5;
y = 2;z=2

dp = [INT_MIN] * (rod_len + 1)
ans = maxRodCutsTab(rod_len,x,y,z)

if ans <0:
    print(0)

else:
    print(ans)
        



