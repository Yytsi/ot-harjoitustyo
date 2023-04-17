import pygame
from load_image import load_image


class Coin(pygame.sprite.Sprite):
    COIN_LOCATION_LEFT = 0
    COIN_LOCATION_RIGHT = 1

    def __init__(self, origin_x=0, origin_y=0, width=32, height=32, location=COIN_LOCATION_RIGHT):
        super().__init__()

        self.image = load_image("coin.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = origin_x
        self.rect.y = origin_y
        self.location = location
