import pygame
pygame.init()


def create_score(x: int, y: int, display_num: int, size=100):
    long, short = size // 2, size // 10
    coordinates = [[x + short, y + i] for i in range(0, (long + short) * 2 + 1, long + short)] + [[x + i, y + j + short] for j in range(0, long + short + 1, long + short) for i in range(0, long + short + 1, long + short)]

    segments = [
        [1, 0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 0, 1]
    ]

    enabled = segments[display_num]

    for i, j in enumerate(coordinates):
        if enabled[i] == 1:
            pygame.draw.rect(screen, (255, 255, 255), tuple(j + ([long, short] if j[0] == x + short else [short, long])))


def display_score(x: int, y: int, display_num: int, size=100):
    create_score(x, y, 0 if len(str(display_num)) == 1 else int(str(display_num)[0]), size)
    create_score(x + size / 10 * 8, y, int(str(display_num)[-1]), size)


WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong')

pong_one_y = pong_two_y = HEIGHT / 2
ball_x, ball_y = WIDTH / 2, HEIGHT / 2
move, ball_x_speed, ball_y_speed = 0, 2, 2

scores = [0, 0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEMOTION:
            pong_one_y = event.pos[1] - 50
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move = -1
            elif event.key == pygame.K_DOWN:
                move = 1
        elif event.type == pygame.KEYUP:
            move = 0

    screen.fill((0, 0, 0))

    pong_two_y += move * 5
    ball_x += ball_x_speed
    ball_y += ball_y_speed

    if ball_x <= 5:
        scores[1] += 1
        ball_x, ball_x_speed = 300, -ball_x_speed
    elif ball_x >= 595:
        scores[0] += 1
        ball_x, ball_x_speed = 300, -ball_x_speed

    if ball_y <= 5 or ball_y >= 595:
        ball_y_speed = -ball_y_speed

    pygame.draw.rect(screen, (255, 255, 255), (75, pong_one_y, 25, 100))
    pygame.draw.rect(screen, (255, 255, 255), (WIDTH - 100, pong_two_y - 50, 25, 100))
    pygame.draw.circle(screen, (255, 255, 255), (ball_x, ball_y), 10)

    if (70 <= ball_x <= 100 and pong_one_y <= ball_y <= pong_one_y + 100) or (WIDTH - 70 >= ball_x >= WIDTH - 105 and pong_two_y - 50 <= ball_y <= pong_two_y + 50):
        ball_x_speed = -ball_x_speed
    if scores[0] == 20:
        screen.fill((0, 0, 0))

        text = f'{"Left" if scores[0] > scores[1] else "No" if scores[0] == scores[1] else "Right"} Team Wins!'
        obj2 = pygame.font.Font('/System/Library/Fonts/Avenir.ttc', 32).render(text, False, (255, 255, 255))
        rect = obj2.get_rect()
        rect.center = (300, 300)
        screen.blit(obj2, rect)

        pygame.display.update()
        pygame.font.get_fonts()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

    display_score(75, 50, scores[0], 50)
    display_score(WIDTH - 125, 50, scores[1], 50)

    pygame.display.update()
