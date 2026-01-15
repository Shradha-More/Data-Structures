
import ctypes

class MyList:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a C type array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        # Represent the list as a string [1, 2, 3]
        result = '['
        for i in range(self.n):
            result += str(self.A[i])
            if i < self.n - 1:
                result += ', '
        result += ']'
        return result

    def __iter__(self):
        # Returns an iterator object
        for i in range(self.n):
            yield self.A[i]
    
    def __getitem__(self,index):
        if isinstance(index, slice):
        # Handle slicing
            start = index.start or 0
            end = index.stop or self.n
            step = index.step or 1
        
            # Return a new MyList object with the sliced content
            sliced_list = MyList()
            for i in range(start, end, step):
                sliced_list.append(self.A[i])
            return sliced_list
        elif 0 <= index < self.n:
            return self.A[index]
        else:
            return "IndexError - Index out of range.."

    def append(self, item):
        if self.n == self.size:
            # resize
            self.resize(self.size*2)
            # append
        self.A[self.n] = item
        self.n += 1

    def pop(self):
        if self.n == 0:
            return "Empty List"
        print("The item popped is ",self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i  
        return "Value Error- The number not in the list"

    def __delitem__(self, pos):
        if pos < 0 or pos >= self.n:
            raise IndexError("Index out of range")
        if 0<= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
        self.n = self.n - 1

    def insert(self, pos, item):
        if self.n == self.size:
            self.__resize(self.size*2)
            for i in range(self.n, pos, -1):
                self.A[i] = self.A[i-1]
            self.A[pos] = item
            self.n = self.n + 1
        else:
            return "IndexError"

    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            # Delete
            self.__delitem__(pos)
        else:
            return pos

    def resize(self, new_capacity):
        # create new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        # reassign A
        self.A = B

    def __make_array(self,capacity):
        # creates a C type array(static, referential) with size capacity
        return (capacity*ctypes.py_object)()

    def bubble_sort(self):
        # Perform bubble sort on the list
        for i in range(self.n - 1):
            swapped = False
            for j in range(self.n - i - 1):
                if self.A[j] > self.A[j + 1]:
                    # Swap elements if they are in the wrong order
                    self.A[j], self.A[j + 1] = self.A[j + 1], self.A[j]
                    swapped = True
            if not swapped:  # If no swaps occurred, the list is sorted
                break
    
    def find_min(self):
        if self.n == 0:
            return "The list is empty."
        min_value = self.A[0]
        for i in range(1, self.n):
            if self.A[i] < min_value:
                min_value = self.A[i]
        return min_value

    def find_max(self):
        if self.n == 0:
            return "The list is empty."
        max_value = self.A[0]
        for i in range(1, self.n):
            if self.A[i] > max_value:
                max_value = self.A[i]
        return max_value

    def find_sum(self):
        total = 0
        for i in range(self.n):
            total += self.A[i]
        return total

    def extend(self, other_list):
    # Check if the other_list is a valid MyList instance
        if isinstance(other_list, MyList):
            for item in other_list:
                self.append(item)
        else:
            return "The input is not a valid MyList instance."

    def merge(self, other_list):
    # Check if the other_list is a valid MyList instance
        if isinstance(other_list, MyList):
            # Append all elements of the other_list to the current list
            for item in other_list:
                self.append(item)
        else:
            return "The input is not a valid MyList instance."


L = MyList()

# L = []    # To access the negative indexing

L.append(869)
L.append(3)
L.append(38)
L.append(100)
L.append(945)

print("The dynamic Array is ",L)
print("Element at index 6 is ",L[6])
print("The length of dynamic array is",len(L))

L.insert(2,18)
print("Array after inserting item is ",L)

index = L.find("Shraddha")
print(f"Index of 'Shraddha' is {index}")

L.bubble_sort()
print("Sorted String List:", L)

print("Smallest element:", L.find_min())

print("Largest element:", L.find_max())

print("Sum of elements:", L.find_sum())

# Applying slicing
print("The elements between range of index 1 to 4 is ",L[1:4])  
print("The elements between range of index 0 to 3 is ",L[:3])  
print("The elements of list with the gap of 2 is ",L[::2])  

# print(L[-1])   # Access last element
# print(L[-2])   # Access second last element

L2 = MyList()
L2.append(4)
L2.append(5)
L.merge(L2)
print("Merged List:", L) 

L.extend(L2)
print("Extended List:", L)

L.remove(0)
print("Array after removing item is ",L)

L.__delitem__(1)
print("Array after deleting item is ",L)

L.pop()
print("Array after popping item is ",L)


L.clear()
print("Array after clearing it is ",L)




