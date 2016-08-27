
def bubbleSort(elementsList):
    n = len(elementsList)
    swapped = True
    while n > 0 and swapped:
        swapped = False
        for i in range(0,n-1):
            if elementsList[i] > elementsList[i+1]:
                swapped = True
                tmp = elementsList[i]
                elementsList[i]= elementsList[i+1]
                elementsList[i+1] = tmp
                print('The swapped elements are:', elementsList[i],'and',elementsList[i+1])
                print(elementsList)
        n = n - 1


elementsList = [1,4,5,2,7,0,13,9]
bubbleSort(elementsList)
print('The sorted list is:', elementsList)

