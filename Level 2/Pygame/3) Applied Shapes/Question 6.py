from random import randint
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

radius, negative, color = 10, 10, tuple([randint(0, 255) for i in range(3)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, color, (300, 300), radius)
    radius, negative, color = radius + negative, -negative if radius + negative == 300 or radius + negative == 10 else negative, tuple([randint(0, 255) for i in range(3)]) if radius == 300 else color

    radius += negative
    if radius == 300 or radius == 10:
        negative = -negative
    if radius == 300:
        color = tuple([randint(0, 255) for i in range(3)])

    pygame.display.update()
