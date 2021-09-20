import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

ball_one_x, ball_two_x, speed = 10, 590, 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 255, 255), (ball_one_x, 300), 10)
    pygame.draw.circle(screen, (225, 210, 88), (ball_two_x, 300), 10)

    ball_one_x += speed * 5
    ball_two_x += -speed * 5
    if ball_one_x + 10 >= 300 >= ball_two_x - 10 or ball_one_x - 10 <= 0 and ball_two_x + 10 >= 600:
        speed = -speed

    pygame.display.update()
