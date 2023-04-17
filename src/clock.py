import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, frames_per_second):
        self._clock.tick(frames_per_second)

    def get_ticks(self):
        return pygame.time.get_ticks()
