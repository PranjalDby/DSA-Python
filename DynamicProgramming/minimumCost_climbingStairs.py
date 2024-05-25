from cmath import cos


def count_possible_climb(current_step, n):
    if current_step == n:
        return 1

    if current_step > n:
        return 0

    return count_possible_climb(current_step + 1, n) + count_possible_climb(current_step + 2, n)


def minimum_cost_memoization(n, cost, dp):
    # Recursion + Memoization
    if n == 0:
        return cost[0]

    if n == 1:
        return cost[1]

    # cost of climbinfg stairs will be added
    # We have to optimize the solution

    if dp[n] == -1:
        dp[n] = min(minimum_cost_memoization(n - 1, cost, dp), minimum_cost_memoization(n - 2, cost, dp)) + cost[n]
        return dp[n]

    return dp[n]


def minimumCostHelper_Tabulation(n, cost, dp):
    # Bottom-Up Approach

    """ 
    Bottom-Up Approach with Memoization
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2,n):
        dp[i] = cost[i] + min(dp[i-1],dp[i-2])

    """

    # Space optimized - Bottom Up
    prev1 = cost[0];
    prev2 = cost[1]
    for i in range(2, n):
        curr = min(prev1, prev2) + cost[i]
        prev2 = prev1
        prev1 = curr

    return min(prev1, prev2)


def findMinimumCostClimbStairs(cost):
    n = len(cost)
    dp = [-1] * n
    return minimumCostHelper_Tabulation(n, cost, dp)


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

print(findMinimumCostClimbStairs(cost))
