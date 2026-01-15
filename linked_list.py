
# a = Node(1)
# b = Node(2)
# c = Node(3)

# a.next = b
# b.next = c

# print(a.next)
# print(b.data)
# print(id(c))

class Node:

    def __init__(self, value):

        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):

        # Empty Linked List
        self.head = None
        # Number of the nodes in LL
        self.n = 0
        
    def __len__(self):
        return self.n
    
    def insert_head(self,value):

        # new node
        new_node = Node(value)
        #create connection
        new_node.next = self.head
        #reassign head
        self.head = new_node
        # increment n
        self.n = self.n + 1

    def __str__(self):

        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    def append(self, value):

        new_node = Node(value)
        if self.head == None:
            #empty
            self.head = new_node
            self.n = self.n + 1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        # You are at the last node
        curr.next = new_node
        self.n = self.n + 1

    def insert_after(self, after, value):

        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
       
        if curr != None:
            # logic
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n + 1
        else:
            return 'Item not Found'

    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):

        if self.head == None:
            return "Empty LL"
        self.head = self.head.next
        self.n = self.n - 1

    def pop(self):
        
        if self.head == None:
            return "Empty LL"

        curr = self.head

        if curr.next == None:
            return self.delete_head()

        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n - 1

    def remove(self, value):

        if self.head == None:
            return 'Empty LL'

        if self.head.data == value:
            return self.delete_head()

        curr = self.head
        while curr.next != None:
            if curr.next.data == value:
                break  
            curr = curr.next

        if curr.next == None:
            return 'Not Found'
        else:
            curr.next = curr.next.next

    def search(self, item):
        curr = self.head
        pos = 0
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos + 1
        return "Not Found"

    def delete_by_index(self, index):
        if self.head is None:  # Case: Empty list
            return "List is empty"

        if index < 0:  # Case: Invalid index
            return "Invalid index"

        # Case: Deleting the head node
        if index == 0:
            self.head = self.head.next  # Update head to the next node
            return "Node deleted"

        # Case: Deleting a node at other positions
        curr = self.head
        prev = None
        pos = 0

        while curr is not None and pos < index:
            prev = curr
            curr = curr.next
            pos += 1

        if curr is None:  # Case: Index out of bounds
            return "Index out of bounds"

        prev.next = curr.next  # Bypass the node to delete it
        return "Node deleted"


    def __getitem__(self, index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.data
            curr = curr.next
            pos = pos + 1

        return 'Index Error'

L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.insert_head(5)
print(L)

len(L)     # Length of the LinkedList is number of nodes in the LinkedList

L.append(7)
L.append(9)
print(L)

L.insert_after(3,10)
L.insert_after(7,15)
print(L)

print(L.search(5))

print(L[7])

L.pop()
print(L)

L.remove(1)
print(L)

L.delete_head()
print(L)

L.clear()
print(L)








