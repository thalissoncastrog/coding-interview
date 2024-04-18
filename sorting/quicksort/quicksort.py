def quicksort(list, start = 0, end = None):
    
    if end is None:
        end = len(list) - 1
    
    if start < end:
        p = partition(list, start, end)
        quicksort(list, start, p - 1)
        quicksort(list, p + 1, end)


def partition(list, start, end):
    
    pivot = list[end]
    i = start

    for j in range(start, end):

        if(list[j] <= pivot):
            list[j], list[i] = list[i], list[j]
            i += 1

    list[i], list[end] = list[end], list[i]
    return i

#arr = [3, 7, 5, 1, 2] 
#arr = [3, 5, 5, 1, 2]
arr = [1, 2, 3, 5, 5]

result = quicksort(arr)

print(arr)