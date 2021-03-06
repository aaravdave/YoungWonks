import pygame

class Timer:
    def __init__(self):
        self.accumulated_time = 0
        self.start_time = pygame.time.get_ticks()
        self.running = True

    def pause(self):
        if not self.running:
            raise Exception('Already Paused')
        self.running = False
        self.accumulated_time += pygame.time.get_ticks() - self.start_time

    def resume(self):
        if self.running:
            raise Exception('Already Running')
        self.running = True
        self.start_time = pygame.time.get_ticks()

    def get(self):
        if self.running:
            return (self.accumulated_time + (pygame.time.get_ticks() - self.start_time))
        else:
            return self.accumulated_time
