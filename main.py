import pygame
import random
import math
import constants
from View import View
from Visualiser import *
pygame.init()


# For generating a random array.
def generate_array(n, min_item, max_item):
	lst = []
	for _ in range(n):
		val = random.randint(min_item, max_item)
		lst.append(val)
	return lst

#This is temporary, just for testing the visualiser. Will be removed when other algorithms are added.
def bubble_sort(view, ascending=True):
	lst = view.lst
	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_list(view, {j: constants.GREEN, j + 1: constants.BLUE}, True)
				yield True

	return lst


def main():
	run = True
	clock = pygame.time.Clock()

	n = 50
	min_item = 0
	max_item = 200
	lst = generate_array(n, min_item, max_item)
	view = View(1000, 800, lst)
	sorting = False
	ascending = True

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
				lst = generate_array(n, min_item, max_item)			#The array to be sorted is generated
				view.set_list(lst)
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