

def checkEligi(base,new_box):

    if new_box[0] <= base[0] and new_box[1] <= base[1] and new_box[2] <= base[2]:
        return True   

    else:
        return False
    
def longest_inc_subs(array,index,prev):
        if index == -2:
            return 0
        
        # include
        include = 0
        if prev == len(array) or((array[index][0] <= array[prev][0]) and (array[index][1] <= array[prev][1]) and (array[index][2] <= array[prev][2])):
            include = array[index][2] + longest_inc_subs(array,index-1,index)
        
        exclude = 0 + longest_inc_subs(array,index-1,prev)

        return max(include,exclude)

def longest_inc_subs_bottomUp(array):
    n = len(array)
    currRow = [0] * (len(array)+1)
    next = [0] * (len(array)+1)
    # bottom - up approach

    for curr in range(n-1,-1,-1):
        for prev in range(curr-1,-2,-1):
            include = 0
            if prev == -1 or checkEligi(array[curr],array[prev]):
                include = array[curr][2] + next[curr + 1]  # index + 1 becuase we have to move prev to curr and curr to the next index
            
            exclude = 0 + next[prev+1]

            currRow[prev + 1] = max(include,exclude)

        next = currRow

    return next[0]
cuboids = [[38,25,45],[76,35,3]]

cb = [[29,59,36],[12,13,97],[49,86,43],[9,57,50],[97,19,10],[17,92,69],[92,36,15],[16,63,8],[94,24,78],[52,11,39],[48,61,57],[15,44,79],[6,69,98],[30,70,41],[23,17,33],[85,86,12],[13,75,98],[75,30,30],[89,18,27],[94,83,81]]


print(len(cb))

cuboids = sorted([sorted(cub) for cub in cb])
print(cuboids)
print(longest_inc_subs(cuboids,len(cuboids)-1,-1))