
# Write a python program to reverse a linked list containing integer data

def reverse(self):
    prev_node = None
    curr_node = self.head

    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node  = next_node

    self.head = prev_node
 