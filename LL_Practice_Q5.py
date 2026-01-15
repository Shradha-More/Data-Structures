'''
Given a linkedlist of characters. Write a python function to return a new string that is created by appending all charactersgiven in the linkedlist a sper the list given below.

'''

def change_sent(self):

    temp = self.head
    while temp != None:
        if temp.data == '*' or temp.data == '/':
            temp.data = ' '

            if temp.next.data == '*' or temp.next.data == '/':
                temp.next.next.data = temp.next.next.data.upper()
                temp.next = temp.next.next

        temp = temp.next


