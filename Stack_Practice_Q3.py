
# Celebrity Problem

# You will have a matrix of any order in input.
# You have to find out celebrity item from than matrix
# Celebrity is the person who doesn't know anyone but everyone knows him.


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
        self.count = 0

    def isempty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def get_size(self):
        return self.count

    def traverse(self):
        temp = self.top
        while temp != None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            return self.top.data

    def pop(self):
        if(self.isempty()):
            return "Stack Empty"
        else:
            popped_data = self.top.data
            self.top = self.top.next 
            self.count -= 1
            return popped_data

 
L = [
        [0,0,1,1],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,1,0]
]

def find_the_celeb(L):

    s = Stack()

    for i in range(len(L)):
        s.push(i)

    while s.get_size() >= 2:
        i = s.pop()
        j = s.pop()

        if L[i][j] == 0:
            # j is not a celebrity
            s.push(i)

        else:
            # i is not a celeb
            s.push(j)

    celeb = s.pop()

    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No one is a celebrity")
                return
            
    print("The celebrity is",celeb)

find_the_celeb(L)

