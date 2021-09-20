import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

coordinates = [(210, 300), (390, 300), (250, 400), (300, 235), (350, 400)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    for i, j in enumerate(coordinates):
        pygame.draw.line(screen, (255, 255, 255), j, coordinates[(i + 1) % 5])

    pygame.display.update()
