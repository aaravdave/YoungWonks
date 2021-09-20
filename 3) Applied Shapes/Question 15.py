from random import randint
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

coordinates = [(randint(0, 600), randint(0, 600)) for i in range(100)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    for i in coordinates:
        pygame.draw.circle(screen, (255, 255, 255), i, 2)

    pygame.display.update()
