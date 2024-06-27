from queue import LifoQueue
def prev_smaller_element(heights):
    stk1 = LifoQueue()
    res = [-1] * len(heights)
    stk1.put(-1)
    for i in range(0,len(heights)):
        curr = heights[i]
        while stk1.queue[-1] != -1 and heights[stk1.queue[-1]] >= curr:
            stk1.get()

        res[i] = stk1.queue[-1]
        stk1.put(i)

    return res

def next_smaller_element(heights):
    stack = LifoQueue()
    res = [-1] * len(heights) 
    stack.put(-1)

    for i in range(len(heights)-1,-1,-1):
        curr = heights[i]
        while stack.queue[-1] != -1 and heights[stack.queue[-1]] >= curr:
            stack.get()

        res[i] = stack.queue[-1]
        stack.put(i)

    return res



def solve(heights):
    next_smaller_index = next_smaller_element(heights)
    
    prev_smaller_index = prev_smaller_element(heights)
    
    print(prev_smaller_index)
    print(next_smaller_index)
    area = float('-inf')

    n = len(heights)
    for i in range(0,n):

        l = heights[i]

        # if next[i] == -1 we need to move next[i] = n

        if next_smaller_index[i] == -1:
            next_smaller_index[i] = n

        b = next_smaller_index[i] - prev_smaller_index[i] -1

        area_rec = l * b
        area = max(area,area_rec)
        print(area)


    return area



arr =[2,4]
print(solve(arr))
