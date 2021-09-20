import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

radius = negative = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (300, 300), radius)
    radius, negative = radius + negative, -negative if radius + negative == 300 or radius + negative == 10 else negative

    # radius += negative
    # if radius == 300 or radius == 10:
    #     negative = -negative

    pygame.display.update()
