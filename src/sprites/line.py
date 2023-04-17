import pygame
from load_image import load_image


class Line(pygame.sprite.Sprite):
    def __init__(self, origin_x=0, origin_y=0, width=5, height=400):
        super().__init__()

        self.image = load_image("line.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = origin_x
        self.rect.y = origin_y
