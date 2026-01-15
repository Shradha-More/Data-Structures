

# Linear Search
# Brute Search

def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        
    return -1


arr = [12, 34, 56, 75, 32, 65, 89, 29, 100, 122]
print(linear_search(arr, 100))

# Time Complexity O(n)
# No Sorting Required

