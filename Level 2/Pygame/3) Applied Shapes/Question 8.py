import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

x = x_change = 1
y = y_change = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 150, 150), (x, 275, 150, 50))  # THE BODY

    pygame.draw.circle(screen, (255, 255, 255), (x + 25, 355), 30)  # THE WHEELS
    pygame.draw.circle(screen, (255, 255, 255), (x + 125, 355), 30)

    x += x_change  # MOVEMENT
    if x >= 450 or x == 0:
        x_change = -x_change

    pygame.display.update()
