import pygame, time
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

tile = [0, 0, 50, 50]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), tile)
    tile[0] = 0 if tile[0] >= 600 - tile[2] else tile[0] + tile[2]

    pygame.display.update()

    time.sleep(0.1)
