import pygame
from load_image import load_image


class Line(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=5, height=400):
        super().__init__()

        self.image = load_image("line.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
