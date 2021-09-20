import pygame
pygame.init()


def text(message, x, y, color, size):
    font = pygame.font.SysFont('freesans', size)
    message = font.render(message, False, color)
    screen.blit(message, (x, y))


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 0, 255), (275, 290, 50, 20))
    text('PLAY', 282, 291, (255, 255, 255), 15)

    pygame.draw.rect(screen, (255, 0, 0), (275, 340, 50, 20))
    text('QUIT', 282, 341, (255, 255, 255), 15)

    pygame.display.update()
