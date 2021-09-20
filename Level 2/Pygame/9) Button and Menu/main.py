import ping_pong, flappy_bird, snake, tic_tac_toe
import pygame
pygame.init()


def run(name):
    global clicked
    exec(f'{name}.start()')
    clicked = 0


class Button:
    def __init__(self, surface, text, x, y, width=75, height=30, command=None, color=(0, 0, 0), text_color=(255, 255, 255), text_size=15):
        if command:
            self.command = command

        self.color = color
        self.text = text
        self.text_color = text_color
        self.text_size = text_size

        self.surface = surface
        self.rect = (x, y, width, height)

    def configure(self, mouse_x, mouse_y, mouse_down):
        pygame.draw.rect(self.surface, self.color, self.rect)
        screen.blit(pygame.font.Font('/System/Library/Fonts/Avenir.ttc', self.text_size).render(self.text, False, self.text_color), self.rect[:2])
        if self.rect[0] < mouse_x < sum(self.rect[::2]) and self.rect[1] < mouse_y < sum(self.rect[1::2]) and mouse_down:
            self.command[0](*self.command[1:])


screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Shapes!!')

mouse = [0, 0]
clicked = 0

png = Button(screen, 'Ping Pong', 100, 100, command=(run, 'ping_pong'))
brd = Button(screen, 'Flappy Bird', 300, 100, command=(run, 'flappy_bird'))
snk = Button(screen, 'Snake', 100, 300, command=(run, 'snake'))
ttt = Button(screen, 'Tic Tac Toe', 300, 300, command=(run, 'tic_tac_toe'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEMOTION:
            mouse = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            clicked = 0

    screen.fill((255, 255, 255))

    png.configure(*mouse, clicked)
    brd.configure(*mouse, clicked)
    snk.configure(*mouse, clicked)
    ttt.configure(*mouse, clicked)

    pygame.display.update()
