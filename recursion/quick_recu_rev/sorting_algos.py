# insertion sort : places a unsorted element at its suitable place in each iteration.

import array


def insertion_sort(array,n):

    if n <= 1:
        return
    
    # recursively sort the first n-1 items
    insertion_sort(array,n-1)

    # insert the nth item in the sorted part

    key = array[n-1]
    j = n-2

    while j >= 0 and array[j] > key:
        array[j+1] = array[j]
        j-=1

    array[j+1] = key

arr = [14,1,6,1,4,19,6,14,3,15]

# insertion_sort(arr,len(arr))
def insertion_sort_iterative(arr):
    for i in range(1,len(arr)):
        
        # move elements of arr[0,..,i-1], that are greater than key one step ahead of there current position. example if element at postion 0 is greater than element at 1 then move element that are at pos 0 to 1
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key
        # for j in range(i,0,-1):
        #     if key <= arr[j-1]:
        #         temp = arr[j-1]
        #         arr[j-1] = arr[j]
        #         arr[j] = temp

    return arr

# arr = insertion_sort_iterative(arr)
# print(arr)

# Selection Sort: 
def smallest(arrr,i,j):
    if i == j:
        return i
    
    mini = smallest(arrr,i+1,j)

    return i if arr[i] <= arr[mini] else mini

def selection_sort(array,index):

    if len(array) <= 1:
        return

    print(array)
    for i in range(0,len(array)):
        small_in = smallest(array,i,len(array)-1)

        # placing smallest element to the beg..
        array[i],array[small_in] = array[small_in],array[i]

     
    selection_sort(array[index+1:],index + 1)


def selection_sort_iterative(array,n):
    if n <=1 :
        return []
    
    for steps in range(0,n):
        min_indx = steps # let assume that our first element is minimum
        for j in range(steps + 1,n):
            # selecting the minimum element in each loop
            if array[min_indx] > array[j]:
                min_indx = j
        
        # putting minimum element at correct postion
                
        (array[min_indx],array[steps]) = array[steps],array[min_indx]

    return array

# print(selection_sort_iterative(arr,len(arr)))

def insertion_sort_recur(array,n):

    if n <= 1:
        return
    
    # divinding the problem into smaller sub-problems

    insertion_sort_recur(array,n-1)

    key = array[n-1]

    for i in range(0,n):
        if key <= arr[i]:
            temp = arr[i]
            arr[i] = key
            key = temp

    array[n-1] = key

    return

    

def getMin_iter(arr,i,j):
    mini = arr[i]
    min_idx = -1
    print(arr)
    for k in range(i,j+1):
        if arr[k] <= mini:
            min_idx = k
            mini = arr[k] 
    
    print('mini = ',min_idx)
    return min_idx

arr = [14,1,6,0,-1,2]


def insertion_sort_iter(arr,n):
    if n <= 0:
        return []
    
    if n == 1:
        return arr
    
    for i in range(1,n):
        key = arr[i]
        for j in range(0,i+1):
            if key <= arr[j]:
                temp = arr[j]
                arr[j] = key
                key = temp
        arr[i] = key

    
    return arr


def selection_sort_recur(arr,index):

    if len(arr) <= 1 or index >= len(arr):
        return

    for i in range(0,len(arr)):
        minim = getMin_iter(arr,i,len(arr)-1)
        arr[i],arr[minim] = arr[minim],arr[i]

    selection_sort_recur(arr[index+1:],index + 1)


def bubble_sort_rec(array,n):
    
    # base case

    if n == 0 :
        return
    
    # loop to traverse to each element of the array

    for i in range(0,n-1):

        if array[i] >= array[i+1]:
            # swap largest element with smallest element
            array[i],array[i+1] = array[i+1],array[i]
        

    # RR for next iteration
            
    bubble_sort_rec(array,n-1)


def bubble_iterative_approach(array):
    if len(array) == 1:
        return array
    
    for i in range(len(array)):

        for j in range(0,len(array)-i-1):

            if array[j] >= array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]

    
    return array
    

arr2 = [-2,0,11,-9,45]

arr2 = bubble_iterative_approach(arr2)

print(arr2)
    
