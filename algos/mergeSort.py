def mergeSort(arr, left, right):
    if(left<right):
        mid = int((left + right)/2)
        yield from mergeSort(arr, left, mid)
        yield from mergeSort(arr, mid+1, right)
        yield from merge(arr, left, mid, right)
def merge(arr, left, mid, right):
    left_array = arr[left: mid+1]
    right_array = arr[mid+1: right+1]
    i=0
    j=0
    k=left
    while i < len(left_array) and j < len(right_array):
        yield arr, left+i, mid+j, left, right
        if(left_array[i] < right_array[j]):
            arr[k] = left_array[i]
            i+=1
        else:
            arr[k] = right_array[j]
            j+=1
        k+=1
    while i < len(left_array):
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array): 
        arr[k] = right_array[j]
        j += 1
        k += 1