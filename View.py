import constants
import pygame
import math

pygame.init()

# The class 
class View:
	bg_color = constants.WHITE

	normal_font = pygame.font.SysFont('helvetica', 24)
	title_font = pygame.font.SysFont('helvetica', 40)
    #Initialise the application window
	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Visualiser")
		self.set_list(lst)
    #Declare and initialise the list undergoing the sorting
	def set_list(self, lst):
		self.lst = lst
		self.min_item = min(lst)
		self.max_item = max(lst)

		self.block_width = round((self.width - constants.HORIZONTAL_PADDING) / len(lst))
		self.block_height = math.floor(
		    (self.height - constants.TOP_PADDING) / (self.max_item - self.min_item))
		self.start_x = constants.HORIZONTAL_PADDING // 2
