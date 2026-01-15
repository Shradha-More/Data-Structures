

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    def enqueue(self, value):
        # Push the value onto stack1
        self.stack1.append(value)

    def dequeue(self):
        if not self.stack2:
            # If stack2 is empty, move elements from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # If stack2 is still empty, the queue is empty
        if not self.stack2:
            return "Queue is empty"
        
        # Pop the top element from stack2
        return self.stack2.pop()

    def traverse(self):
        # Combine stack1 and reversed stack2 for traversal
        result = list(reversed(self.stack2)) + self.stack1
        for element in result:
            print(element)

# Example Usage
queue = QueueUsingStacks()

# Enqueue elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue elements
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2

# Enqueue another element
queue.enqueue(4)

# Traverse the queue
queue.traverse()  # Output: 3 4
