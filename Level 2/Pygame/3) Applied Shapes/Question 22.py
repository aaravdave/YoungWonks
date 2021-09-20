import pygame
pygame.init()


def text(message, x, y, color, size):
    font = pygame.font.SysFont('freesans', size, bold=True, italic=True)
    message = font.render(message, False, color)
    screen.blit(message, (x, y))


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

string = input('Enter a string: ')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    text(string, 300, 300, (255, 255, 255), 32)

    pygame.display.update()
