
def is_sorted(arr):
    sorted = True

    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            sorted = False

    return sorted

arr = [22,33,44,55,66,77,88,99,100]
print(is_sorted(arr))