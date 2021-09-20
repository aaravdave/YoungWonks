def collision(xy1, xy2, w=30, h=30):
    return ((xy1[0] > (xy2[0] - w)) and (xy1[0] < (xy2[0] + w))) and ((xy1[1] > (xy2[1] - h)) and (xy1[1] < (xy2[1] + h)))


def sequence(pattern_list):
    return pattern_list + pattern_list[-2:0:-1]


import random, time, math, pygame
pygame.init()

WIDTH, HEIGHT = 600, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')
GRID_SIZE = 30

coordinates = [[WIDTH / 2 - differ, HEIGHT / 2] for differ in range(GRID_SIZE * 3, GRID_SIZE * 8 + 1, GRID_SIZE)]
current_coordinates, current_direction = coordinates[0], 90
speed, length = 0, 0

mouse_coordinates = [0, 0]
create_food = lambda: [random.randint(0, 600) // GRID_SIZE * GRID_SIZE, random.randint(0, 600) // GRID_SIZE * GRID_SIZE]
food_coordinates = create_food()

up = pygame.mixer.Sound('up.wav')
down = pygame.mixer.Sound('down.wav')
left = pygame.mixer.Sound('left.wav')
right = pygame.mixer.Sound('right.wav')
bite = pygame.mixer.Sound('chomp.wav')

apple = pygame.image.load('apple.png')
banana = pygame.image.load('banana.png')
pear = pygame.image.load('pear.png')

corner = pygame.transform.rotozoom(pygame.image.load('corner.png'), 0, 0.4)

clock = pygame.time.Clock()
current_fruit = apple
timer = 0

# pattern = sequence([(53, 172, 242), (33, 152, 222), (13, 132, 202)])
# pattern = sequence([(242, 232, 53), (242, 188, 53), (242, 138, 53)])
pattern = sequence([(255, 100, 100), (255, 180, 100), (255, 255, 100), (100, 255, 100), (100, 255, 255), (100, 100, 255), (190, 100, 255)])

screen.fill((0, 0, 0))
while True:
    clock.tick(15)
    screen.fill((53, 242, 87))
    for i in range(WIDTH // GRID_SIZE + 1):
        for j in range(HEIGHT // GRID_SIZE + 1):
            pygame.draw.rect(screen, (33, 222, 193) if (i + j) % 2 == 0 else (33, 222, 162), (i * GRID_SIZE - GRID_SIZE // 2, j * GRID_SIZE - GRID_SIZE // 2, GRID_SIZE, GRID_SIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not (current_direction in [180, 360] and speed):
                current_direction = 360
                speed = GRID_SIZE
                up.play()
            if event.key == pygame.K_DOWN and not (current_direction in [180, 360] and speed):
                current_direction = 180
                speed = GRID_SIZE
                down.play()
            if event.key == pygame.K_LEFT and not (current_direction in [90, 270] and speed):
                current_direction = 270
                speed = GRID_SIZE
                left.play()
            if event.key == pygame.K_RIGHT and not (current_direction in [90, 270] and speed):
                current_direction = 90
                speed = GRID_SIZE
                right.play()
            if event.key == pygame.K_p:
                time.sleep(0.5)
                paused = True
                while paused:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.QUIT:
                            quit()
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_p:
                                paused = False

    if current_direction == 90:
        current_coordinates[0] += speed
        pygame.draw.rect(screen, (200, 0, 0), (current_coordinates[0], current_coordinates[1] - GRID_SIZE // 6, GRID_SIZE, GRID_SIZE // 3))
    elif current_direction == 180:
        current_coordinates[1] += speed
        pygame.draw.rect(screen, (200, 0, 0), (current_coordinates[0] - GRID_SIZE // 6, current_coordinates[1], GRID_SIZE // 3, GRID_SIZE))
    elif current_direction == 270:
        current_coordinates[0] -= speed
        pygame.draw.rect(screen, (200, 0, 0), (current_coordinates[0] - GRID_SIZE, current_coordinates[1] - GRID_SIZE // 6, GRID_SIZE, GRID_SIZE // 3))
    else:
        current_coordinates[1] -= speed
        pygame.draw.rect(screen, (200, 0, 0), (current_coordinates[0] - GRID_SIZE // 6, current_coordinates[1] - GRID_SIZE, GRID_SIZE // 3, GRID_SIZE))

    if collision(current_coordinates, food_coordinates, GRID_SIZE, GRID_SIZE):
        length += 1
        coordinates.insert(-1, [coordinates[-1][0], coordinates[-1][1]])
        food_coordinates = create_food()
        current_fruit = random.choice([apple, banana, pear])
        bite.play()

    if 0 >= current_coordinates[0]:
        current_coordinates[0] += WIDTH
    if current_coordinates[0] >= WIDTH:
        current_coordinates[0] -= WIDTH
    if 0 >= current_coordinates[1]:
        current_coordinates[1] += HEIGHT
    if current_coordinates[1] >= HEIGHT:
        current_coordinates[1] -= HEIGHT

    if speed:
        coordinates.insert(0, current_coordinates.copy())
        coordinates.pop(-1)

    for i, j in enumerate(coordinates):
        pygame.draw.rect(screen, pattern[i % len(pattern)], (j[0] - GRID_SIZE // 2, j[1] - GRID_SIZE // 2, GRID_SIZE, GRID_SIZE))
    screen.blit(pygame.transform.scale(current_fruit, (int(GRID_SIZE + math.sin(timer)), int(GRID_SIZE + math.sin(timer)))), (food_coordinates[0] - GRID_SIZE // 2, food_coordinates[1] - GRID_SIZE // 2))

    screen.blit(pygame.font.Font('/System/Library/Fonts/SFNSMono.ttf', 30).render(str(length), False, (255, 255, 255)), (10, 10))
    screen.blit(corner, (WIDTH - corner.get_width(), HEIGHT - corner.get_height()))

    timer += 5
    pygame.display.update()
