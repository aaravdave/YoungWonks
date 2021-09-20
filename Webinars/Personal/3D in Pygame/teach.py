import pygame
pygame.init()


def draw(color, *points):
    pygame.draw.polygon(screen, color, [point(*prev) for prev in points], 2)


def point(x, y, z):
    pos_x, pos_y, pos_z = position
    return (view * ((x + pos_x) / (z + pos_z))) + WIDTH // 2, (view * ((y + pos_y) / (z + pos_z))) + HEIGHT // 2


def cube(color, x, y, z, radius):
    plus_x, plus_y, plus_z = x + radius, y + radius, z - radius
    negv_x, negv_y, negv_z = x - radius, y - radius, z + radius

    draw(color, (plus_x, plus_y, z), (negv_x, plus_y, z), (negv_x, negv_y, z), (plus_x, negv_y, z))
    draw(color, (plus_x, plus_y, negv_z), (negv_x, plus_y, negv_z), (negv_x, negv_y, negv_z), (plus_x, negv_y, negv_z))
    draw(color, (plus_x, plus_y, z), (negv_x, plus_y, z), (negv_x, plus_y, negv_z), (plus_x, plus_y, negv_z))
    draw(color, (plus_x, negv_y, z), (negv_x, negv_y, z), (negv_x, negv_y, negv_z), (plus_x, negv_y, negv_z))


WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('3D with Pygame')

position = [0, 0, -50]
movement = [0, 0, 0, 0, 0, 0]
view = 150

key_detections = [pygame.KEYUP, pygame.KEYDOWN]
movement_detections = [pygame.K_w, pygame.K_s, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type in key_detections:
            for index, key in enumerate(movement_detections):
                if event.key == key:
                    movement[index] = key_detections.index(event.type)

    for ind, move in enumerate(movement):
        if move:
            index = 1 if ind < 2 else 0 if ind < 4 else 2
            position[index] += -5 if ind % 2 == 0 else 5

    screen.fill((0, 0, 0))

    cube((255, 255, 255), 0, 0, 1, 50)
    cube((255, 0, 0), 100, 0, 1, 50)
    cube((0, 255, 0), 200, 0, 1, 50)
    cube((0, 0, 255), 300, 0, 1, 50)

    pygame.display.update()
