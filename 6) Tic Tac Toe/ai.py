# The weather outside is OK :)
# The weather outside is 0K :(

def compute_grid(size):
    global turn
    measure = 300 - size * 3

    pygame.draw.line(screen, (0, 0, 0), (300 - size, 300 - size * 3), (300 - size, 300 + size * 3), 3)
    pygame.draw.line(screen, (0, 0, 0), (300 + size, 300 - size * 3), (300 + size, 300 + size * 3), 3)
    pygame.draw.line(screen, (0, 0, 0), (300 - size * 3, 300 - size), (300 + size * 3, 300 - size), 3)
    pygame.draw.line(screen, (0, 0, 0), (300 - size * 3, 300 + size), (300 + size * 3, 300 + size), 3)

    piece_pos = [0, 0]
    original_grid = grid.copy()
    for piece in grid:
        x_measure = size * piece_pos[0]
        y_measure = size * piece_pos[1]
        x = measure + x_measure
        y = measure + y_measure
        if piece == 'O':
            pygame.draw.circle(screen, (0, 0, 0), (x + (piece_pos[0] + 1) * size, y + (piece_pos[1] + 1) * size), size * 0.75, 3)
        elif piece == 'X':
            pygame.draw.line(screen, (0, 0, 0), (x + size * 0.25 + x_measure, y + size * 0.25 + y_measure), (x + size * 1.75 + x_measure, y + size * 1.75 + y_measure), 4)
            pygame.draw.line(screen, (0, 0, 0), (x + size * 1.75 + x_measure, y + size * 0.25 + y_measure), (x + size * 0.25 + x_measure, y + size * 1.75 + y_measure), 4)
        elif clicked and x + x_measure < mouse[0] < x + size * 2 + x_measure and y + y_measure < mouse[1] < y + size * 2 + y_measure:
            grid[piece - 1] = 'O'
            if check(1, grid):
                print('O Wins!')
                quit()
            if sum([1 if str(i) in 'XO' else 0 for i in grid]) == 9:
                print('XO Tie!')
                quit()

        piece_pos[0] += 1
        if piece_pos[0] == 3:
            piece_pos[0] = 0
            piece_pos[1] += 1

    if grid != original_grid:
        wins = []
        for piece in grid:
            if piece not in 'XO':
                new_grid = grid.copy()
                new_grid[piece - 1] = 'X'
                wins.append(check(0, new_grid))
        if any(wins):
            grid[wins.index(True)] = 'X'
            print('O Wins!')
            quit()


def check(xo, pieces):
    vertical = [all([True if pieces[j - 1] == 'XO'[xo] else False for j in range(i, i + 7, 3)]) for i in range(1, 4)]
    horizontal = [all([True if pieces[j - 1] == 'XO'[xo] else False for j in range(i, i + 3)]) for i in range(1, 8, 3)]
    diagonal = [all([True if pieces[i - 1] == 'XO'[xo] else False for i in range(1, 10, 4)]), all([True if pieces[i - 1] == 'XO'[xo] else False for i in range(3, 8, 2)])]
    return any(vertical) or any(horizontal) or any(diagonal)


import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic Tac Toe')

grid = [i + 1 for i in range(9)]
clicked = 0
mouse = [0, 0]

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
    compute_grid(75)
    pygame.display.update()
