def compute_grid():
    global turn
    measure = 300 - grid_size * 3

    pygame.draw.line(screen, (0, 0, 0), (300 - grid_size, 300 - grid_size * 3), (300 - grid_size, 300 + grid_size * 3), 3)
    pygame.draw.line(screen, (0, 0, 0), (300 + grid_size, 300 - grid_size * 3), (300 + grid_size, 300 + grid_size * 3), 3)
    pygame.draw.line(screen, (0, 0, 0), (300 - grid_size * 3, 300 - grid_size), (300 + grid_size * 3, 300 - grid_size), 3)
    pygame.draw.line(screen, (0, 0, 0), (300 - grid_size * 3, 300 + grid_size), (300 + grid_size * 3, 300 + grid_size), 3)

    piece_pos = [0, 0]
    for piece in grid:
        x_measure = grid_size * piece_pos[0]
        y_measure = grid_size * piece_pos[1]
        x = measure + x_measure
        y = measure + y_measure
        if piece == 'O':
            pygame.draw.circle(screen, (0, 127, 255), (x + (piece_pos[0] + 1) * grid_size, y + (piece_pos[1] + 1) * grid_size), grid_size * 0.75, 3)
        elif piece == 'X':
            pygame.draw.line(screen, (255, 92, 89), (x + grid_size * 0.25 + x_measure, y + grid_size * 0.25 + y_measure), (x + grid_size * 1.75 + x_measure, y + grid_size * 1.75 + y_measure), 4)
            pygame.draw.line(screen, (255, 92, 89), (x + grid_size * 1.75 + x_measure, y + grid_size * 0.25 + y_measure), (x + grid_size * 0.25 + x_measure, y + grid_size * 1.75 + y_measure), 4)
        elif clicked and x + x_measure < mouse[0] < x + grid_size * 2 + x_measure and y + y_measure < mouse[1] < y + grid_size * 2 + y_measure:
            grid[piece - 1] = 'O' if turn else 'X'
            turn = 1 - turn
            if check(1 - turn):
                print(f'\'{"XO"[1 - turn]}\' Wins!')
                quit()
            if sum([1 if str(i) in 'XO' else 0 for i in grid]) == 9:
                print('XO Tie!')
                quit()

        piece_pos[0] += 1
        if piece_pos[0] == 3:
            piece_pos[0] = 0
            piece_pos[1] += 1


def check(xo):
    vertical = [all([True if grid[j - 1] == 'XO'[xo] else False for j in range(i, i + 7, 3)]) for i in range(1, 4)]
    horizontal = [all([True if grid[j - 1] == 'XO'[xo] else False for j in range(i, i + 3)]) for i in range(1, 8, 3)]
    diagonal = [all([True if grid[i - 1] == 'XO'[xo] else False for i in range(1, 10, 4)]), all([True if grid[i - 1] == 'XO'[xo] else False for i in range(3, 8, 2)])]
    return any(vertical) or any(horizontal) or any(diagonal)


import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')

turn = 0
grid = [i + 1 for i in range(9)]
clicked = 0
mouse = [0, 0]
grid_size = 75

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = 0
        elif event.type == pygame.MOUSEMOTION:
            mouse = event.pos

    screen.fill((255, 255, 255))
    screen.blit(pygame.font.Font('/System/Library/Fonts/Avenir.ttc', 25).render(f'{"XO"[turn]}\'s Turn', False, (0, 0, 0)), (10, 10))
    compute_grid()
    pygame.display.update()
