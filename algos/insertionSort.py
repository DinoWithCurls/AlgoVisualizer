import sys
sys.path.append("..")																			#This is done to access functions located outside the current directory.

import constants
from visualiser import draw_list
   
def insertion_sort(view, ascending=True):
	array = view.array																			#Fetch the randomised array.
	for i in range(1, len(array)):
		current = array[i]
		while True:
			ascending_sort = i > 0 and array[i - 1] > current and ascending						#Decide on the order of sorting.
			descending_sort = i > 0 and array[i - 1] < current and not ascending
			if not ascending_sort and not descending_sort:
				break
			array[i] = array[i - 1]
			i = i - 1
			array[i] = current
			draw_list(view, {i - 1: constants.GREEN, i: constants.BLUE}, True)
			yield True																			#Ensure the sorting continues till the end, and the window doesn't close after that.

	return array