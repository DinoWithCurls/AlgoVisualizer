import pygame
import random
import math
import constants
from View import View
from visualiser import *
pygame.init()


# For generating a random array.
def generate_array(n, min_item, max_item):
	array = []
	for _ in range(n):
		val = random.randint(min_item, max_item)
		array.append(val)
	return array

#This is temporary, just for testing the visualiser. Will be removed when other algorithms are added.
def bubble_sort(view, ascending=True):
	array = view.array
	for i in range(len(array) - 1):
		for j in range(len(array) - 1 - i):
			num1 = array[j]
			num2 = array[j + 1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				array[j], array[j + 1] = array[j + 1], array[j]
				draw_list(view, {j: constants.GREEN, j + 1: constants.BLUE}, True)
				yield True

	return array


def main():
	run = True
	clock = pygame.time.Clock()

	n = 50
	min_item = 0
	max_item = 200
	array = generate_array(n, min_item, max_item)
	view = View(1000, 800, array)
	sorting = False
	ascending = True
	# the algorithm to be shown and run as default
	sorting_algorithm = bubble_sort
	sorting_algo_name = "Bubble Sort"
	sorting_algorithm_generator = None

	while run:
		clock.tick(100)
		if sorting:
			try:
				next(sorting_algorithm_generator)
			except StopIteration:
				sorting = False
		else:
			draw(view, sorting_algo_name, ascending)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				new_array = generate_array(n, min_item, max_item)			#The array to be sorted is generated
				view.set_list(new_array)
				sorting = False
			elif event.key == pygame.K_SPACE and sorting == False:	#When the spacebar is pressed on the keyboard, the array is sorted and this is visualised on the screen
				sorting = True
				sorting_algorithm_generator = sorting_algorithm(view, ascending)
			elif event.key == pygame.K_a and not sorting:			#When A is pressed on the keyboard
				ascending = True
			elif event.key == pygame.K_d and not sorting:			#When D is pressed on the keyboard
				ascending = False
			elif event.key == pygame.K_b and not sorting:			#When B is pressed on the keyboard
				sorting_algorithm = bubble_sort
				sorting_algo_name = "Bubble Sort"
	pygame.quit()


if __name__ == "__main__":
	main()