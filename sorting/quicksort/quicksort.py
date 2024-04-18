def quicksort(arr):
    
    
    pivot = arr[len(arr) - 1]

    arr = partition(arr, pivot, low = 0, high = 0)
    #arr, low, high = partition(arr, pivot, low = 0, high = 0)

    return arr
# arr = [3, 7, 5, 1, 2]
# low = 0
# high = 3 
# pivot = 2

# i = 4 

def partition(arr, pivot, low, high):
    
    for i in range(0, len(arr) - 1):

        if (arr[i] < pivot):

            if(i < high):
                low = i
            else:
                aux = arr[low] #aux = 3
                arr[low] = arr[i] # arr[0] = arr[3] = 1
                arr[i] = aux # arr[3] = 3
                low += 1
        high = i
    
    if(low == high):
        return arr
    
    aux = pivot # 2
    arr[len(arr) - 1] = arr[low] # arr[4] = arr[0] = 3
    arr[low] = pivot #arr[0] = 2
    
    arrLeft = arr[0:low]
    arrRight = arr[low + 1:len(arr)]
    arrPivot = [pivot]
    
    return quicksort(arrLeft) + arrPivot + quicksort(arrRight)

arr = [3, 7, 5, 1, 2]

result = quicksort(arr)

print(arr)