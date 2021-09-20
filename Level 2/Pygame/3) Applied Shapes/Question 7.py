import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.draw.rect(screen, (255, 150, 150), (50, 275, 150, 50))  # THE BODY

    pygame.draw.circle(screen, (255, 255, 255), (75, 355), 30)  # THE WHEELS
    pygame.draw.circle(screen, (255, 255, 255), (175, 355), 30)

    pygame.display.update()
