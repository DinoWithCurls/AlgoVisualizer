import constants
import pygame
import random

#This function is for the application window
def draw(view, algo, ascending):
	view.window.fill(view.bg_color)

	title = view.title_font.render(
	    f"{algo} - {'Ascending' if ascending else 'Descending'}", 1, constants.BLACK)
	view.window.blit(title, (view.width/2 - title.get_width()/2, 5))

	controls = view.normal_font.render(
	    "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, constants.BLACK)
	view.window.blit(controls, (view.width/2 - controls.get_width()/2, 45))

	draw_list(view)
	pygame.display.update()

#This function is for the sorting visualisation
def draw_list(view, color_positions={}, clear_bg=False):
	lst = view.lst

	if clear_bg:
		clear_rect = (constants.HORIZONTAL_PADDING//2, constants.TOP_PADDING,
						view.width - constants.HORIZONTAL_PADDING, view.height - constants.TOP_PADDING)
		pygame.draw.rect(view.window, view.bg_color, clear_rect)

	for i, val in enumerate(lst):
		x = view.start_x + i * view.block_width
		y = view.height - (val - view.min_item) * view.block_height

		color = constants.BAR_GRADIENTS[i % 3]

		if i in color_positions:
			color = color_positions[i]

		pygame.draw.rect(view.window, color, (x, y, view.block_width, view.height))

	if clear_bg:
		pygame.display.update()