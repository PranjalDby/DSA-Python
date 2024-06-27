from queue import LifoQueue
def solve(arr):
    stack = LifoQueue()
    res = []
    stack.put(-1)

    for i in range(len(arr)-1,-1,-1):
      
        while arr[i] < stack.queue[-1]:
            stack.queue.pop()

        res.append(stack.queue[-1])
        stack.put(arr[i])

    return res[::-1]



arr = [2,1,4,3]

print(solve(arr))
        

