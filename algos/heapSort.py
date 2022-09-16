import sys
import constants

sys.path.append("..")

from visualiser import draw_list

def heap_sort(view, ascending=True):
    array = view.array
    yield from heapify(view, array, len(array))
    end = len(array) - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        draw_list(view, {0: constants.GREEN, end: constants.BLUE}, True)
        yield True
        end -= 1
        yield from siftDown(view, array, 0, end)
    return array


def heapify(view, array, count):
    start = (count-1) // 2
    while start >= 0:
        yield from siftDown(view, array, start, count - 1)
        start -= 1


def siftDown(view, array, start, end):
    root = start
    while 2 * root + 1 <= end:
        child = 2 * root + 1
        swap = root
        if array[swap] < array[child]:
            swap = child
        if child + 1 <= end and array[swap] < array[child + 1]:
            swap = child + 1
        if swap == root:
            return
        else:
            array[root], array[swap] = array[swap], array[root]
            draw_list(view, {root: constants.GREEN, swap: constants.BLUE}, True)
            yield True
            root = swap