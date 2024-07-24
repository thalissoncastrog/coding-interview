def BinarySearch(arr, target, low = 0, high = None):

    if high is None:
        high = len(arr) - 1
    
    if(low > high):
        return -1

    middle = (low + high) // 2

    if target == arr[middle]:
        return middle
    
    if arr[middle] > target:
        return BinarySearch(arr, target, low, middle - 1)

    return BinarySearch(arr, target, middle + 1, high)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

result = BinarySearch(arr, target)

print(result)