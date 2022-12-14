import pygame
import random
import math
import constants
from View import View
from visualiser import *
from algos.insertionSort import insertion_sort
from algos.bubbleSort import bubble_sort
from algos.heapSort import heap_sort
from algos.selectionSort import selection_sort
from algos.shellSort import shell_sort

pygame.init()

def generate_array(n, min_item, max_item):							#For generating a randomised array.
	array = []
	for _ in range(n):
		val = random.randint(min_item, max_item)
		array.append(val)
	return array

def main():
	run = True
	clock = pygame.time.Clock()										#Initialise the Clock function

	n = 50
	min_item = 0
	max_item = 200
	array = generate_array(n, min_item, max_item)					#Generate the random array
	view = View(1000, 800, array)									#Create the application window
	sorting = False
	ascending = True
	sorting_algorithm = bubble_sort									#The algorithm to be shown and run as default	
	sorting_algo_name = "Bubble Sort"								#The name of the algorithm being shown.
	sorting_algorithm_generator = None

	while run:
		clock.tick(100)
		if sorting:
			try:
				next(sorting_algorithm_generator)					#This calls the visualiser along with the algorithm			
			except StopIteration:
				sorting = False
		else:
			draw(view, sorting_algo_name, ascending)				#This modifies the header to display the algo being visualised, along with the order of sorting.

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				new_array = generate_array(n, min_item, max_item)	#The array to be sorted is generated
				view.set_list(new_array)
				sorting = False
			elif event.key == pygame.K_SPACE and sorting == False:	#When the spacebar is pressed on the keyboard, the array is sorted and this is visualised on the screen
				sorting = True
				sorting_algorithm_generator = sorting_algorithm(view, ascending)
			elif event.key == pygame.K_a and not sorting:			#When A is pressed on the keyboard
				ascending = True
			elif event.key == pygame.K_d and not sorting:			#When D is pressed on the keyboard
				ascending = False
			elif event.key == pygame.K_i and not sorting:			#when I is pressed on the keyboard
				sorting_algorithm = insertion_sort
				sorting_algo_name = "Insertion Sort"
			elif event.key == pygame.K_h and not sorting:			#when H is pressed on the keyboard
				sorting_algorithm = heap_sort
				sorting_algo_name = "Heap Sort"
			elif event.key == pygame.K_b and not sorting:			#When B is pressed on the keyboard
				sorting_algorithm = bubble_sort
				sorting_algo_name = "Bubble Sort"
			elif event.key == pygame.K_s and not sorting:			#when S is pressed on the keyboard
				sorting_algorithm = selection_sort
				sorting_algo_name = "Selection Sort"
			elif event.key == pygame.K_z and not sorting:			#when Z is pressed on the keyboard
				sorting_algorithm = shell_sort
				sorting_algo_name = "Shell Sort"
	pygame.quit()


if __name__ == "__main__":
	main()