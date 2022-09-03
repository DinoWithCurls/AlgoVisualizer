import pygame
import random
import math
pygame.init()


class View:
	black = 0, 0, 0
	white = 255, 255, 255
	green = 0, 255, 0
	blue = 127, 0, 255
	bg_color = white

	gradient = [
		(153, 255, 153),
		(255, 102, 178),
		(192, 192, 192)
	]

	normal_font = pygame.font.SysFont('helvetica', 24)
	title_font = pygame.font.SysFont('helvetica', 40)

	horizontal_padding = 100
	top_padding = 100

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Visualiser")
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_item = min(lst)
		self.max_item = max(lst)

		self.block_width = round((self.width - self.horizontal_padding) / len(lst))
		self.block_height = math.floor(
		    (self.height - self.top_padding) / (self.max_item - self.min_item))
		self.start_x = self.horizontal_padding // 2


def draw(view, algo, ascending):
	view.window.fill(view.bg_color)

	title = view.title_font.render(
	    f"{algo} - {'Ascending' if ascending else 'Descending'}", 1, view.black)
	view.window.blit(title, (view.width/2 - title.get_width()/2, 5))

	controls = view.normal_font.render(
	    "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, view.black)
	view.window.blit(controls, (view.width/2 - controls.get_width()/2, 45))

	draw_list(view)
	pygame.display.update()


def draw_list(view, color_positions={}, clear_bg=False):
	lst = view.lst

	if clear_bg:
		clear_rect = (view.horizontal_padding//2, view.top_padding,
						view.width - view.horizontal_padding, view.height - view.top_padding)
		pygame.draw.rect(view.window, view.bg_color, clear_rect)

	for i, val in enumerate(lst):
		x = view.start_x + i * view.block_width
		y = view.height - (val - view.min_item) * view.block_height

		color = view.gradient[i % 3]

		if i in color_positions:
			color = color_positions[i]

		pygame.draw.rect(view.window, color, (x, y, view.block_width, view.height))

	if clear_bg:
		pygame.display.update()


def generate_array(n, min_item, max_item):
	lst = []
	for _ in range(n):
		val = random.randint(min_item, max_item)
		lst.append(val)
	return lst


def bubble_sort(view, ascending=True):
	lst = view.lst
	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_list(view, {j: view.green, j + 1: view.blue}, True)
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
				lst = generate_array(n, min_item, max_item)
				view.set_list(lst)
				sorting = False
			elif event.key == pygame.K_SPACE and sorting == False:
				sorting = True
				sorting_algorithm_generator = sorting_algorithm(view, ascending)
			elif event.key == pygame.K_a and not sorting:
				ascending = True
			elif event.key == pygame.K_d and not sorting:
				ascending = False
			elif event.key == pygame.K_b and not sorting:
				sorting_algorithm = bubble_sort
				sorting_algo_name = "Bubble Sort"
	pygame.quit()


if __name__ == "__main__":
	main()