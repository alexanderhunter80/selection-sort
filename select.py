unsorted = [5, 13, 21, 25, 1, 12, 23, 15, 14, 6, 10, 9, 7, 16, 8, 19, 11, 3, 24, 22, 4, 2, 17, 20, 18]

def selectSort(arr):
    print(arr)
    for i in range(0,len(arr)):
        min = arr[i]
        swapAt = i
        for j in range(i,len(arr)):
            if min > arr[j]:
                swapAt = j
                min = arr[j]
        if swapAt != i:
            arr[i],arr[swapAt] = arr[swapAt],arr[i]
        print(arr)

selectSort(unsorted)            