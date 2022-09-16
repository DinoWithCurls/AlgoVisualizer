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
	def __init__(self, width, height, array):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Visualiser")
		self.set_list(array)
    #Declare and initialise the list undergoing the sorting
	def set_list(self, array):
		self.array = array
		self.min_item = min(array)
		self.max_item = max(array)
		# width and height for the visualisation operation view block.
		self.block_width = round((self.width - constants.HORIZONTAL_PADDING) / len(array))
		self.block_height = math.floor(
		    (self.height - constants.TOP_PADDING) / (self.max_item - self.min_item))
		# starting coordinate for the visualisation operation view block
		self.start_x = constants.HORIZONTAL_PADDING // 2
