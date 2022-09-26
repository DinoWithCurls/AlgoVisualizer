import sys
sys.path.append("..")																			#This is done to access functions located outside the current directory.

import constants
from visualiser import draw_list

def bubble_sort(view, ascending=True):
	array = view.array																			#Fetch the randomised array.
	for i in range(len(array) - 1):									
		for j in range(len(array) - 1 - i):
			num1 = array[j]
			num2 = array[j + 1]
			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):					#Check the order of sorting, and then swap the items based on that.
				array[j], array[j + 1] = array[j + 1], array[j]
				draw_list(view, {j: constants.GREEN, j + 1: constants.BLUE}, True)
				yield True																		#This ensures the next() doesnt hit a null, and the window remains open even after the visualisation is completed.

	return array