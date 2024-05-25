

from json import loads
import json
from sys import stdin


def solve(arr):

    mini = arr[0]
    profit = 0

    for i in range(1,len(arr)):
        diff = arr[i]-mini # selling stock at different day; we purchase sabse minimum price stock on first day
        profit = max(profit,diff)
        mini = min(mini,arr[i]) # next minimum price stock to purchase


    return profit

arr = [7,1,5,3,6,4]


with open('user1.txt', 'w+') as f:
    try:
        for case in map(loads, stdin):
            print(case)
            f.write(f"{solve(case)}\n")
        
        f.seek(0)
    except json.decoder.JSONDecodeError:
        ...


with open('user1.txt') as op:
    print(f'{op.readlines()}')
