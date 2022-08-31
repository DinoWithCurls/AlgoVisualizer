def insertionSort(arr, *args):
    sorted = []
    size = len(arr)
    for i in range(0, size):
        j = i - 1
        key = arr[i]
        sorted.append(i)
        while j >= 0 and arr[j] > key:
            yield arr, j, -1, i, -1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    sorted.clear()