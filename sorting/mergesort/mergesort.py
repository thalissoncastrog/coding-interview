def Merge(list, start, middle, end):
    
    left = list[start:middle]
    right = list[middle:end]

    topLeft, topRight = 0, 0

    for k in range(start, end):

        if(topLeft >= len(left)):
            list[k] = right[topRight]
            topRight += 1
        
        elif(topRight >= len(right)):
            list[k] = left[topLeft]
            topLeft += 1
        
        elif(left[topLeft] < right[topRight]):
            list[k] = left[topLeft]
            topLeft += 1
        else:
            list[k] = right[topRight]
            topRight += 1

def MergeSort(list, start = 0, end = None):
    
    if(end is None):
        end = len(list)

    if(end - start > 1):
        
        middle = (end + start)//2
        MergeSort(list, start, middle)
        MergeSort(list, middle, end)

        Merge(list, start, middle, end)


    