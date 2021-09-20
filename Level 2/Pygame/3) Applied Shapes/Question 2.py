from random import *
import pygame, time
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

tile = [0, 0, 50, 50]
color = tuple([randint(0, 255) for i in range(3)])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, color, tile)
    tile[0] = 0 if tile[0] >= 600 - tile[2] else tile[0] + tile[2]
    if tile[0] == 0:
        tile[1] += tile[3]
        color = tuple([randint(0, 255) for i in range(3)])
    if tile[1] >= 600:
        tile[1] = 0

    pygame.display.update()

    time.sleep(0.1)
