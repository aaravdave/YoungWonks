import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

current_color, other_color = (0, 0, 255), (255, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    x = 0
    for i in range(6):
        pygame.draw.rect(screen, current_color, (x, 0, 100, 100))
        current_color, other_color = other_color, current_color
        x += 100

    pygame.display.update()
