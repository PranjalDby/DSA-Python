



from queue import LifoQueue
stack = LifoQueue()
def solve(arr,res):

    global stack

    if  len(arr) == 1:
        return [-1]
        
    
    stack.put(-1)
    for k in range(len(arr)-1,-1,-1):
        curr = arr[k]
        while stack.queue[-1] >= arr[k]:
            stack.get()

        res.append(stack.queue[-1])
        stack.put(curr)

    
    return res[::-1]

    


    



arr = [2,3,1]
res = solve(arr,[])
print(res)