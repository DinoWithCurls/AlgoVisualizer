from random import randint

def quickSort(arr, left, right):
    if left >= right:
        return
    idx = left
    rand_idx = randint(left, right)
    arr[right], arr[rand_idx] = arr[rand_idx], arr[right]
    for j in range(left, right):
        yield arr, j, right, idx, -1
        if arr[j] < arr[right]:
            arr[j], arr[idx] = arr[idx], arr[j]
            idx += 1
        arr[idx], arr[right] = arr[right], arr[idx]
        yield from quickSort(arr, idx+1, right)
        yield from quickSort(arr, left, idx-1) 