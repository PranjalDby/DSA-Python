"""
There is a 3 lane road of length n that consists of n + 1 points labeled from 0 to n. A frog starts at point 0 in the second lane and wants to jump to point n. However, there could be obstacles along the way.

You are given an array obstacles of length n + 1 where each obstacles[i] (ranging from 0 to 3) describes an obstacle on the lane obstacles[i] at point i. If obstacles[i] == 0, there are no obstacles at point i. There will be at most one obstacle in the 3 lanes at each point.

For example, if obstacles[2] == 1, then there is an obstacle on lane 1 at point 2.
The frog can only travel from point i to point i + 1 on the same lane if there is not an obstacle on the lane at point i + 1. To avoid obstacles, the frog can also perform a side jump to jump to another lane (even if they are not adjacent) at the same point if there is no obstacle on the new lane.

For example, the frog can jump from lane 3 at point 3 to lane 1 at point 3.
Return the minimum number of side jumps the frog needs to reach any lane at point n starting from lane 2 at point 0.

Note: There will be no obstacles on points 0 and n.
 
"""
import sys
sys.setrecursionlimit(10 ** 9)
def min_sideways_jump(obstacles,curr_lane,curr_pos):
    n = len(obstacles)-1
    # base-case
    if curr_pos == n:
        return 0
    
    #check if next pos of our current lane does not have obstacle and go straight
    if obstacles[curr_pos + 1] != curr_lane:
        return min_sideways_jump(obstacles,curr_lane,curr_pos+1)
    
    else:
        # sideways -jump
        ans = float('inf')
        # looping through lanes
        for i in range(1,4):
            # sideways jump not equal to our curr_lane
            if curr_lane != i and obstacles[curr_pos] != i:
                ans = min(ans,1 + min_sideways_jump(obstacles,i,curr_pos))

        return ans
    
def min_sideways_jump_memo(obstacles,curr_lane,curr_pos,dp):
    n = len(obstacles)-1
    # base-case
    if curr_pos == n:
        return 0
    
    if dp[curr_lane][curr_pos] != -1:
        return dp[curr_lane][curr_pos]

    #check if next lane does not have obstacle and we are moving straight ways
    if obstacles[curr_pos + 1] != curr_lane:
        return min_sideways_jump_memo(obstacles,curr_lane,curr_pos+1,dp)
    
    else:
        # sideways -jump on different lanes
        ans = float('inf')
        # loop to iterate on lanes
        for i in range(1,4):
            # sideways jump not equal to our curr_lane
            if curr_lane != i and obstacles[curr_pos] != i:
                ans = min(ans,1 + min_sideways_jump_memo(obstacles,i,curr_pos,dp))
        
        dp[curr_lane][curr_pos] = ans
        return dp[curr_lane][curr_pos]

def min_sideways_jump_Tab(obstacles):
    n = len(obstacles)-1
    INT_MAX = 100000000
    dp = [[INT_MAX for i in range(len(obstacles))] for k in range(4)]

    # base case analysis
    dp[0][n] = 0
    dp[1][n] = 0
    dp[2][n] = 0
    dp[3][n] = 0

    for pos in range(n-1,-1,-1):

        for lane in range(1,4):

            if obstacles[pos + 1] != lane:

                dp[lane][pos] = dp[lane][pos+1]
        
            else:
                # sideways -jump
                # looping through lanes
                ans = INT_MAX
                for i in range(1,4):
                    # sideways jump not equal to our curr_lane
                    if lane != i and obstacles[pos] != i:
                        ans = min(ans,1 + dp[i][pos+1])

                dp[lane][pos] = ans

    # at last position frog still have choice to jump sideways, so we have to return the min of overall sidways jump
    
    return min(dp[2][0],dp[1][0]+1,dp[3][0] + 1)


def min_sideways_jump_Tab_sopt(obstacles):
    n = len(obstacles)-1
    INT_MAX = 100000000
    curr = [INT_MAX] * (4)
    next = [INT_MAX] * (4)

    # base case analysis
    next[0] = 0
    next[1] = 0
    next[2] = 0
    next[3] = 0

    for pos in range(n-1,-1,-1):

        for lane in range(1,4):

            if obstacles[pos + 1] != lane:
                curr[lane] = next[lane]
        
            else:
                # sideways -jump
                # looping through lanes
                ans = INT_MAX
                for i in range(1,4):
                    # sideways jump not equal to our curr_lane
                    if lane != i and obstacles[pos] != i:
                        ans = min(ans,1 + next[i])

                curr[lane] = ans

        # after each iteration copy curr in next
        next = curr

    # at last position frog still have choice to jump sideways, so we have to return the min of overall sidways jump
    
    return min(next[2],next[1]+1,next[3] + 1)

from large_subproblem import obstacles

# obstacles = [0,1,2,3,0]
# dp = [[-1 for i in range(len(obstacles))] for j in range(4)]
# print(min_sideways_jump_memo(obstacles,2,0,dp))

print(min_sideways_jump_Tab_sopt(obstacles))