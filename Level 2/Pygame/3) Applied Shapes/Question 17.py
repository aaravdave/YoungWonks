from random import randint, choice
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

coordinates = [[randint(0, 600), randint(0, 600)] for i in range(100)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    for i, j in enumerate(coordinates):
        pygame.draw.circle(screen, choice([(255, 255, 255), (225, 210, 88)]), j, 2)

        coordinates[i][1] += 1
        if coordinates[i][1] > 600:
            coordinates[i][1] = 0

    pygame.display.update()
