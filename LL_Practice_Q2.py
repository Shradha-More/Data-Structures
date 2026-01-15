
# Write a python program to fing the maximum value in LinkedList and replace it with a given value
# Assume that the LinkedList is populated with whole numbers and there is only one maximum value in the LinkedList
    

def replace_max(self, value):
    temp = self.head
    max = temp
    while temp != None:
        if temp.data > max:
            max = temp
        temp = temp.next
    max.data = value

