#Derangments is a permutation of 'N' elements, such that no elements appears in its oringinal postion
"""
given:
i/p = n and we have to find total number of derangments possible of a set of 'N' elements.
"""

MOD = (10 ** 9) + 7


def total_derangments(n):
    # base case
    if n == 1:
        # only single element to derange

        return 0

    if n == 2:
        # two elements were given

        return 1

    # RR

    ans = ((n - 1) % MOD) * ((total_derangments(n - 1) % MOD) + (total_derangments(n - 2) % MOD)) % MOD


def totalDerangmentsMemoiZed(n, dp):
    # base case
    if n == 1:
        # only single element to derange

        return 0

    if n == 2:
        # two elements were given

        return 1

    if dp[n] != -1:
        return dp[n]

    # RR

    dp[n] = (((n - 1) % MOD) * (
                (totalDerangmentsMemoiZed(n - 1, dp) % MOD) + (totalDerangmentsMemoiZed(n - 2, dp) % MOD)) % MOD)

    return dp[n]


def totalDerangmentsTab(n, dp):
    # dp[1] = 0
    # dp[2] = 1

    # for i in range(3,n+1):
    #     first = dp[i-1] % MOD
    #     second = dp[i-2] % MOD

    #     sum = (first + second) % MOD

    #     ans = ((i-1) * sum) % MOD

    #     dp[i] = ans

    # return dp[n]

    # Space  otpimized beacuse,dp[i] -> dp[i-1],dp[i] -> dp[i-2]

    prev1 = 1
    prev2 = 0

    for i in range(3, n + 1):
        first = prev1 % MOD
        second = prev2 % MOD

        sum = (first + second) % MOD
        ans = ((i - 1) * sum) % MOD
        prev2 = prev1
        prev1 = ans

    return prev1


n = 4
dp = [0] * (n + 1)
print(totalDerangmentsTab(n, dp))
