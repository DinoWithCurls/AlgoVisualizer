import sys
sys.path.append("..")
import constants
from visualiser import draw_list

def selection_sort(view, ascending=True):
    array = view.array
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if (array[i] < array[min_idx] and ascending) or (array[i] > array[min_idx] and not ascending):
                min_idx = i
                draw_list(view, {i: constants.BLACK, min_idx: constants.BLUE}, True)
                yield True
        (array[step], array[min_idx]) = (array[min_idx], array[step])
        draw_list(view, {step: constants.GREEN, min_idx: constants.BLUE}, True)
        yield True
    return array