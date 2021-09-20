import random, time, pygame
pygame.init()


def start():
    def collision(xy1, xy2, w=30, h=30):
        return ((xy1[0] > (xy2[0] - w)) and (xy1[0] < (xy2[0] + w))) and ((xy1[1] > (xy2[1] - h)) and (xy1[1] < (xy2[1] + h)))

    WIDTH, HEIGHT = 600, 600

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')
    GRID_SIZE = 30

    coordinates = [[WIDTH / 2, HEIGHT / 2]]
    current_coordinates, current_direction = [WIDTH / 2, HEIGHT / 2], 90
    speed, length = GRID_SIZE, 1

    create_food = lambda: [random.randint(0, 600) // GRID_SIZE * GRID_SIZE, random.randint(0, 600) // GRID_SIZE * GRID_SIZE]
    food_coordinates = create_food()

    clock = pygame.time.Clock()

    screen.fill((0, 0, 0))
    while True:
        clock.tick(15)

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not current_direction == 180:
                    current_direction = 360
                if event.key == pygame.K_DOWN and not current_direction == 360:
                    current_direction = 180
                if event.key == pygame.K_LEFT and not current_direction == 90:
                    current_direction = 270
                if event.key == pygame.K_RIGHT and not current_direction == 270:
                    current_direction = 90

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

        if 0 >= current_coordinates[0]:
            current_coordinates[0] += WIDTH
        if current_coordinates[0] >= WIDTH:
            current_coordinates[0] -= WIDTH
        if 0 >= current_coordinates[1]:
            current_coordinates[1] += HEIGHT
        if current_coordinates[1] >= HEIGHT:
            current_coordinates[1] -= HEIGHT

        coordinates.insert(0, current_coordinates.copy())
        coordinates.pop(-1)

        for i, j in enumerate(coordinates):
            pygame.draw.rect(screen, (0, 200, 0), (j[0] - GRID_SIZE // 2, j[1] - GRID_SIZE // 2, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, (200, 0, 0), (food_coordinates[0] - GRID_SIZE // 2, food_coordinates[1] - GRID_SIZE // 2, GRID_SIZE, GRID_SIZE))

        pygame.display.update()
