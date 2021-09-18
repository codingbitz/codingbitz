def swp_arr(a,b,arr):
    if a!=b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements,start_ele,end_ele):
    pivot_idx =start_ele
    pivot = elements[pivot_idx]

    start_ele = pivot_idx+1
    end_ele = len(elements)-1

    while start_ele < end_ele:
        while start_ele < len(elements) and elements[start_ele] <= pivot:
            start_ele += 1

        while elements[end_ele] > pivot:
            end_ele -= 1
            
        if start_ele < end_ele:
            swp_arr(start_ele,end_ele,elements)
    swp_arr(pivot_idx,end_ele,elements)
    return end_ele

def quicksrt(elements,start_ele,end_ele):
    if start_ele < end_ele:
        pi = partition(elements,start_ele,end_ele)
        quicksrt(elements,start_ele,pi-1) # Left Partition
        quicksrt(elements,pi+1,end_ele) #Right Partition

if __name__=='__main__':
    elements = [10,8,28,6,1,14,27]
    tests = [
        [10,8,28,6,1,14,27],
        [3,7,9,11],
        [25,24,22,11],
        [],
        [2]
    ]

    for elements in tests:
        quicksrt(elements,0,len(elements)-1)
        print(f'sorted array: {elements}')