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

    text('Welcome to YoungWonks', 10, 10, (0, 0, 255), 32)

    pygame.display.update()
