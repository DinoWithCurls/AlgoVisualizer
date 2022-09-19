import sys
import constants
sys.path.append("..")

from visualiser import draw_list
   
def insertion_sort(view, ascending=True):
	array = view.array

	for i in range(1, len(array)):
		current = array[i]

		while True:
			ascending_sort = i > 0 and array[i - 1] > current and ascending
			descending_sort = i > 0 and array[i - 1] < current and not ascending

			if not ascending_sort and not descending_sort:
				break

			array[i] = array[i - 1]
			i = i - 1
			array[i] = current
			draw_list(view, {i - 1: constants.GREEN, i: constants.BLUE}, True)
			yield True

	return array