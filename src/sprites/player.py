import pygame
from load_image import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, y=0, x=0, height=64, width=64):
        super().__init__()

        self.player_moving = [False]*4

        self._images = {
            "player_facing_right": load_image("player_facing_right.png"),
            "player_facing_left": load_image("player_facing_left.png")
        }

        self.image = self._images["player_facing_right"]
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    
    def update(self):
        if self.player_moving[0]:
            self.rect.x -= 2
        if self.player_moving[1]:
            self.rect.y -= 2
        if self.player_moving[2]:
            self.rect.x += 2
        if self.player_moving[3]:
            self.rect.y += 2