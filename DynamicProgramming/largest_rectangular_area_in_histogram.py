from queue import LifoQueue

def solve(arr):
 
    next_element = next_smaller_elements(arr)
    prev_element = prev_smaller_elements(arr)

    print(next_element,prev_element)
    area = float('-inf')

    for i in range(0,len(arr)):
        l = arr[i]
        # here we calculate breadth of rectangle,prev = left me ,next = right

        if next_element[i] == -1:
            next_element[i] = len(arr)

        b = next_element[i] - prev_element[i] - 1

        newarea = l * b
        area = max(area,newarea)
        print(f'At i = {i} newarea = {newarea} area = {area}')

    return area


def next_smaller_elements(arr):
    stack = LifoQueue()
    stack.put(-1)
    ans = [0] * len(arr)

    for i in range(len(arr)-1,-1,-1):

        # to move the pointer to next smallest element
        curr = arr[i]
        while stack.queue[-1] != -1 and arr[stack.queue[-1]] >= curr:

            el = stack.get()

        ans[i] = stack.queue[-1] # this is a just smaller element

        stack.put(i)

    return ans
        

def prev_smaller_elements(arr):
    stack2 = LifoQueue()
    stack2.put(-1)
    ans = [0] * len(arr)

    for i in range(0,len(arr)):
        # to move the pointer to next smallest element
        curr = arr[i]

        while stack2.queue[-1] != -1 and arr[stack2.queue[-1]] >= curr:

            el = stack2.get()

        ans[i] = stack2.queue[-1] # this is a just smaller element

        stack2.put(i)

    return ans

arr = [2,1,5,6,2,3]

rr = solve(arr)
print(rr)