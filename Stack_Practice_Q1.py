

# We have a string as an inout suppose "Hello"
# You have to reverse this string to "olleH"

# --> Understand that to use stacks is not an optimal and best solution to reverse the string because it needs more memory.

# Use an inplace reversal for utilization of memory


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top == None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

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
            return popped_data


def reverse_string(text):
    s = Stack()
    for i in text:
        s.push(i)
    res = ""
    while(not s.isempty()):
        res = res + s.pop()
    print(res)


reverse_string("Hello")



