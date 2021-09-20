import pygame
pygame.init()

width, height = 600, 800

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Scroller')

cam_y = 0

while True:
    for event in pygame.event.get():
        if event.type == 4:
            cam_y -= 10
        elif event.type == 5 and cam_y >= 0:
            cam_y += 10

    window.fill((0, 0, 0))
    rect = pygame.font.Font('/System/Library/Fonts/Avenir.ttc', 32).render('a webpage viewer', False, (255, 255, 255))
    window.blit(rect, (10, cam_y + 50))
    pygame.display.update()
