import sys

sys.path.append("..")

from visualiser import draw_list

def bubbleSort(arr, ascending=True):
    #array = view.lst
    array = arr
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            num1 = array[j]
            num2 = array[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                array[j], array[j + 1] = array[j + 1], array[j]
                #draw_list(view, {j: constants.GREEN, j + 1: constants.BLUE}, True)
                #yield True
    return array
