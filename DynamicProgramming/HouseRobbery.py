"""
Given:
Houses are arranged in form circle so that `first house is adjacent of last house`
We have to ignore robbing in to adjacent house.

# ds
an array containing non negative integers. represent the amount of money of each house
return the maximum amount of money earn by robbing into the house.
"""

def maximumRobedMoney(arr,i):

    # base cases : left-right
    
    if i < 0:
        return 0
    
    if i == 0:
        return arr[i]
    
    include = maximumRobedMoney(arr,i-2) + arr[i] #including the amount
    exclude = maximumRobedMoney(arr,i-1) # excluding the amount

    ans = max(include,exclude)

    return ans


def maximumRobbedMoneyBottom_up(arr,n):

    prev2 = 0
    prev1 = arr[0]

    for i in range(1,n):
        include = prev2 + arr[i]
        exclude = prev1 + 0

        prev2 = prev1
        prev1 = max(include,exclude)


    return prev1

arr = [9,8,7]

if len(arr) == 1:

    print(arr[0])

else:

    sol1 = arr[1:]
    sol2 = arr[0:-1]

    ans = max(maximumRobedMoney(sol1,len(sol1)-1),maximumRobedMoney(sol2,len(sol2)-1))

    print(ans)