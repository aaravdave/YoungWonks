import pygame, random
pygame.init()


def touching(item_1=[0, 0, 0, 0], item_2=[0, 0, 0, 0]):
    x1, y1, x2, y2 = item_1[:2] + item_2[:2]
    w1, h1, w2, h2 = item_1[2:] + item_2[2:]
    return (x2 + w2 >= x1 + w1 >= x2 or x2 + w2 >= x1 >= x2) and (y2 + h2 >= y1 >= y2 or y1 + h1 >= y2 >= y1)


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


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Flappy Bird')

pipes = [[600, random.randint(-100, 100), 1]]
bird_y, gravity, score = 300, 0, 0
flag = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEMOTION:
            pong_one_y = event.pos[1] - 50
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y -= 50
                gravity = 2

    screen.fill((200, 230, 255))
    pygame.draw.rect(screen, (205, 130, 50), (0, 580, 600, 20))

    pygame.draw.rect(screen, (100, 100, 255), (200, bird_y, 25, 25))
    bird_y += gravity
    gravity += 1

    for pipe in pipes:
        if touching([200, bird_y, 25, 25], [pipe[0], 0, 100, 225 + pipe[1]]) or touching([200, bird_y, 25, 25], [pipe[0], 375 + pipe[1], 100, 600 - (375 + pipe[1])]) or touching([200, bird_y, 25, 25], [0, 580, 600, 20]) or touching([200, bird_y, 25, 25], [0, 0, 600, 0]):
            pipes = [[600, random.randint(-100, 100), 1]]
            bird_y, gravity = 300, 0
            score = 0
            break
        elif pipe[0] - 250 == 100:
            pipes.append([600, random.randint(-100, 100), random.choice([1, 1, 1, 1, 5])])
        elif pipe[0] == 100:
            score += pipe[2]
        elif pipe[0] + 100 < 0:
            del pipes[pipes.index(pipe)]
            continue
        pygame.draw.rect(screen, [(180, 225, 200), (255, 200, 200)][pipe[2] - 1 - 3 if pipe[2] - 1 else 0], (pipe[0], 0, 100, 225 + pipe[1]))
        pygame.draw.rect(screen, [(180, 225, 200), (255, 200, 200)][pipe[2] - 1 - 3 if pipe[2] - 1 else 0], (pipe[0], 375 + pipe[1], 100, 600 - (375 + pipe[1])))
        pipe[0] -= 10

    display_score(20, 20, score, 35)
    pygame.display.update()

    clock.tick(30)
