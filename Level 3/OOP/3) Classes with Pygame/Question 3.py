import pygame
pygame.init()

Circle = __import__('Question 1').Circle

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

circles = []
for i in range(30):
	circles.append(Circle(25, (i / 10 - int(i / 10)) * 1000, 200 + int(i / 10) * 100, (255, 255, 255)))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
	
	screen.fill((0, 0, 0))

	for circle in circles:
		circle.render(screen)
		if circle.x >= 575:
			circle.x = 20
		circle.x += 5
	
	pygame.display.update()
