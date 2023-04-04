import pygame
from load_image import load_image

class Coin(pygame.sprite.Sprite):
    def __init__(self, y=0, x=0):
        super().__init__()
        
        self.image = load_image("coin.png")
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x