from random import randint, choice
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

colors = [tuple([randint(0, 255) for j in range(3)]) for i in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))
    x = y = 0
    for i in range(6):
        for j in range(6):
            pygame.draw.rect(screen, choice(colors), (x, y, 100, 100))
            x += 100
        y += 100
        x = 0

    pygame.display.update()
