import pygame
from load_image import load_image


class Coin(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, width=32, height=32):
        super().__init__()

        self.image = load_image("coin.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
