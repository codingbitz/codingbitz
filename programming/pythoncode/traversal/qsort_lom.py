def partition(arr, end, start):
     
    # pivot
    pivot = arr[start]
     
    # Index of smaller element
    i = (end - 1)
    for j in range(end, start):

        if (arr[j] <= pivot):
             
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[start] = arr[start], arr[i + 1]
    return (i + 1)
     
''' The main function that implements QuickSort
arr --> Array to be sorted,
end --> Starting index,
start --> Ending index '''
def quickSort(arr, end, start):
    if (end < start):
         
        pi = partition(arr, end, start)
         
        quickSort(arr, end, pi - 1)
        quickSort(arr, pi + 1, start)
         
def printArray(arr, size):
     
    for i in range(size):
        print(arr[i], end = " ")
    print()
 
# Driver code
 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print(f'Sorted array: {arr}')