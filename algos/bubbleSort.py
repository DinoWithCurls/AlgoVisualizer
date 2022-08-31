def bubbleSort(arr, *args):
    for i in range(0, len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            yield arr, j, j+1, -1, -1
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            break