
def maximum_russian_doll(array,index,prev):

    # base case

    if index == len(array):
        return 0
    
    include = 0

    if prev == -1 or array[prev][1] < array[index][1] :
        include = 1 + maximum_russian_doll(array,index + 1,index)
    
    exclude = 0 + maximum_russian_doll(array,index+1,prev)


    return max(include,exclude)

def helper_BS(array,element):
    i = 0
    n = len(array)
    # Actually performing binary search
    while i < n:
        mid = i + (n-i)//2
        if array[mid][1] >= element:
            n = mid

        else:
            i = mid+1

    return n

def maximum_russian_DP(array):
    n = len(array)

    res = [array[0]] #res array which contains first element
    print(res)
    for i in range(1,n):
        # compaire the last element of res with element at index i in array
        if array[i][1] > res[-1][1]:
            res.append(array[i])
        
        else:
            just_bada_index = helper_BS(res,array[i][1])
            print(just_bada_index)
            res[just_bada_index][1] = array[i][1]

    print(res)
    return len(res)

envelopes = [[5,4],[6,4],[6,7],[2,3]]

envelopes.sort(key=lambda x: (x[0],-x[1]))
print(envelopes)
print(maximum_russian_DP(envelopes))
# print(envelopes[0][0])