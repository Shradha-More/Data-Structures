
# What is output of followinh function when head node of following linked list is passed as in put?
# 1->2->3->4->5

def fun(head):
    if(head == None):
        return
    if head.next.next != None:
        print(head.data, "", end="")
        fun(head.next)
    print(head.data, "", end="")


# Ans -> # 1234321