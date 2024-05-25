

def greedy(str1,str2,index):

    if index >= len(str1):
        return 0
    

    ans = 0
   
    if str1.index(str1[index]) < str2.index(str1[index]):
        ans = -1 * (str1.index(str1[index]) - str2.index(str1[index])) + greedy(str1,str2,index+1)
    
    else:
        ans = str1.index(str1[index]) - str2.index(str1[index]) + greedy(str1,str2,index+1)

    
    return ans




s= "abcde";t="edbac"

print(greedy(s,t,0))