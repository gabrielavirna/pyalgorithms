def bubbleSort(elementsList):
    n = len(elementsList)
    for j in range(0,n-1):
        swapped = False
        for i in range(0,n-1-j):
            if elementsList[i] > elementsList[i+1]:
                tmp = elementsList[i]
                elementsList[i]= elementsList[i+1]
                elementsList[i+1] = tmp
                swapped = True
        if not swapped: break
    return elementsList


elementsList = [1,4,5,2,7,0,13,9]
bubbleSort(elementsList)
print('The sorted list is:', elementsList)


