import sys
sys.path.append("..")                                                                           #This is done to access functions located outside the current directory.

import constants
from visualiser import draw_list

def shell_sort(view, ascending=None):
    array = view.array                                                                          #Fetch the randomised array.
    n = len(array)
    gap = int(n/2)                                                                              #The initial interval between the elements to be swapped.
    while gap > 0:
        for i in range(gap,n):
            temp = array[i]
            j = i
            while  (j >= gap and array[j-gap] > temp and ascending):
                array[j] = array[j-gap]
                draw_list(view, {j: constants.BLUE, j-gap: constants.GREEN}, True)
                yield True
                j -= gap
            array[j] = temp
            draw_list(view, {i: constants.BLACK, j: constants.BLUE}, True)
            yield True
        gap = int(gap / 2)
    return array