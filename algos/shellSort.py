import sys
sys.path.append("..")

import constants
from visualiser import draw_list

def shell_sort(view, ascending=True):
    array = view.array
    n = len(array)
    gap = int(n/2)
    while gap > 0:
        for i in range(gap,n):
            temp = array[i]
            j = i
            while  j >= gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                draw_list(view, {j: constants.BLUE, j-gap: constants.GREEN}, True)
                yield True
                j -= gap
            array[j] = temp
            draw_list(view, {i: constants.BLACK, j: constants.BLUE}, True)
            yield True
        gap = int(gap / 2)
    return array