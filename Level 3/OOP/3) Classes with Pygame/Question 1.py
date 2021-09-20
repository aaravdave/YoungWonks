from random import randint
import pygame
pygame.init()

class Circle:
	def __init__(self, radius, x, y, color):
		self.radius = radius
		self.x = x
		self.y = y
		self.color = color
	
	def render(self, surface):
		pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

if __name__ == '__main__':
	screen = pygame.display.set_mode((600, 600))
	pygame.display.set_caption('Shapes!!')
	for i in range(10):
		Circle(randint(5, 15), randint(0, 600), randint(0, 600), (randint(0, 255), randint(0, 255), randint(0, 255))).render(screen)
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()
