from random import randint
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
    pygame.draw.rect(screen, color, (600 - tile[2] - tile[0], *tile[1:]))

    tile[0], tile[1], color = 0 if tile[0] >= 600 - tile[2] else tile[0] + tile[2], 0 if tile[1] >= 600 - tile[3] else tile[1] + tile[3], tuple([randint(0, 255) for i in range(3)])

    pygame.display.update()
    time.sleep(0.5)
