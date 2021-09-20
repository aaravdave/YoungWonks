import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('___')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))
    pygame.display.update()
