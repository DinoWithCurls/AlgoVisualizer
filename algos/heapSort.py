def heapSort(arr, *args):
    yield from heapify(arr, len(arr))
    end = len(arr) - 1
    while end > 0:
        yield arr, -1, -1, 0, end
        arr[end], arr[0] = arr[0], arr[end]
        end -= 1
        yield from siftDown(arr, 0, end)


def heapify(arr, count):
    start = (count-1) // 2
    while start >= 0:
        yield from siftDown(arr, start, count - 1)
        start -= 1


def siftDown(arr, start, end):
    root = start
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        swap = root
        if arr[swap] < arr[child]:
            swap = child
        if child + 1 <= end and arr[swap] < arr[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            yield arr, root, swap, -1, -1
            arr[root], arr[swap] = arr[swap], arr[root]
            root = swap