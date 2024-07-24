def BinarySearch(arr, target, low = 0, high = None):
    
    if high is None:
        high = len(arr) - 1


    while low <= high:
        
        middle = low + (high - low) // 2

        if arr[middle] == target:
            return middle
        
        if arr[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = BinarySearch(arr, target)
print(result)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# low = 0 , high = 9, middle = 0 + (9 - 0) // 2 = 4
# low = 5 , high = 9, middle = 5 + (9 - 5) // 2 = 7
# low = 8 , high = 9, middle = 8 + (9 - 8) // 2 = 8

