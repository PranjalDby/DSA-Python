class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



def create_linkedlist_from_list(list_)->Node:

    head = Node(list_[0])
    ptr = head
    for i in range(1,len(list_)):
        newnode = Node(list_[i])
        ptr.next = newnode
        ptr = newnode
    
    return head


def printElement(head):
    if head == None:
        return
    
    pt = head

    while(pt!=None):
        print(pt.data)
        pt = pt.next


def count_LL_elements(head):
    if head == None:
        return 0
    
    if head.next == None:
        return 1
    
    ans = 1 + count_LL_elements(head.next)

    return ans
    


def solve(head,k,length):

    if k > length:
        return head
    
    curr = head
    prev = None
    temp = None
    cout = 0

    while curr != None and cout < k:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        cout += 1
    
    if temp != None:
        head.next = solve(temp,k,length-k)

    
    return prev



def solve_mostOptimized(head,k):
    curr = head
    # to check if the list is empty or not
    for _ in range(k):
        if not curr:
            return head
        
        curr = curr.next

    
    prev = None
    curr = head

    for i in range(k):
        nxt = curr.next
        curr.next = prev # first connection broked
        prev = curr # marking the element as prev
        curr = nxt # moving curr to nxt element
    

    head.next = solve_mostOptimized(curr,k)

    return prev



ll = [1,2,3,4]

head = create_linkedlist_from_list(ll)

n = count_LL_elements(head)

head = solve_mostOptimized(head,2)
printElement(head)

