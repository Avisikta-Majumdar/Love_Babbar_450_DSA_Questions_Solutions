#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

def addOne(head):
    h=head
    prev=head
    value=0
    while h:
        v=h.data
        value=value*10+v
        h=h.next
    s=str(value)
    l1=len(s)
    value+=1
    value=str(value)
    l2=len(value)
    temp = head
    if l1==l2:
        for i in value:
            if temp:
                temp.data = int(i)
                temp = temp.next
        return head
    else:
        for i in value:
            if temp.next:
                temp.data = int(i)
                temp = temp.next
            else:
                x= int(value[-1])
                temp_node = Node(x)
                temp.data = int(i)
                temp.next = temp_node
                return head

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends
