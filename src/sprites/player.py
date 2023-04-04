import pygame
from load_image import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, y=0, x=0):
        super().__init__()

        self._images = {
            "player_facing_right": load_image("player_facing_right.png"),
            "player_facing_left": load_image("player_facing_left.png")
        }

        self.image = self._images["player"]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x