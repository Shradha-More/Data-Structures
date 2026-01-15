

def selection_sort(arr):
    for i in range(len(arr) - 1):
        print(i+1,"pass", end=" ")
        min = i

        print("Current min is",arr[min])

        for j in range(i+1, len(arr)):
            print("Current item under observation is",arr[j])

            if arr[j] < arr[min]:
                print("Current item is less than min")
                min = j
                print("Now the min has become",arr[min])
        arr[i],arr[min] = arr[min],arr[i]
        print(arr)
        print("*" * 40)
    print(arr)


arr = [45,35,87,57,97,40,67,29]
selection_sort(arr)