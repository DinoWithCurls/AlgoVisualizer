import sys

sys.path.append("..")

from visualiser import draw_list
   
def insertionSort(arr, ascending=True):
	#array = view.lst
	array = arr
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
			#draw_list(view, {i - 1: constants.GREEN, i: constants.RED}, True)
			#yield True

	return array