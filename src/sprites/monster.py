import pygame
from load_image import load_image


class Monster(pygame.sprite.Sprite):
    MONSTER_DIRECTION_LEFT = 0
    MONSTER_DIRECTION_RIGHT = 1
    MONSTER_SPEED = 1

    def __init__(self, origin_x=0, origin_y=0, width=48, height=60):
        super().__init__()

        self._images = {
            "monster_facing_right": load_image("monster_facing_right.png"),
            "monster_facing_left": load_image("monster_facing_left.png")
        }

        for key, image in self._images.items():
            self._images[key] = pygame.transform.scale(image, (width, height))

        self.image = self._images["monster_facing_right"]
        self.rect = self.image.get_rect()
        self.rect.x = origin_x
        self.rect.y = origin_y
        self.direction = self.MONSTER_DIRECTION_LEFT

    def chase_player(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += Monster.MONSTER_SPEED
        elif self.rect.x > player.rect.x:
            self.rect.x -= Monster.MONSTER_SPEED
        if self.rect.y < player.rect.y:
            self.rect.y += Monster.MONSTER_SPEED
        if self.rect.y > player.rect.y:
            self.rect.y -= Monster.MONSTER_SPEED

    def face_to_direction(self, direction):
        if self.direction != direction:
            if direction == self.MONSTER_DIRECTION_RIGHT:
                self.image = self._images["monster_facing_right"]
            else:
                self.image = self._images["monster_facing_left"]
        self.direction = direction
