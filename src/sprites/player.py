import pygame
from load_image import load_image


class Player(pygame.sprite.Sprite):
    PLAYER_DIRECTION_LEFT = 0
    PLAYER_DIRECTION_RIGHT = 1

    def __init__(self, origin_x=0, origin_y=0, width=33, height=63):
        super().__init__()

        self.player_moving = [False]*4

        self._images = {
            "player_facing_right": load_image("player_facing_right.png"),
            "player_facing_left": load_image("player_facing_left.png")
        }

        for key, image in self._images.items():
            self._images[key] = pygame.transform.scale(image, (width, height))

        self.image = self._images["player_facing_right"]
        self.rect = self.image.get_rect()
        self.rect.x = origin_x
        self.rect.y = origin_y
        self.direction = self.PLAYER_DIRECTION_RIGHT

    def update(self):
        if self.player_moving[0]:
            self.face_to_direction(self.PLAYER_DIRECTION_LEFT)
            self.move_player(-2, 0)
        if self.player_moving[1]:
            self.move_player(0, -2)
        if self.player_moving[2]:
            self.face_to_direction(self.PLAYER_DIRECTION_RIGHT)
            self.move_player(2, 0)
        if self.player_moving[3]:
            self.move_player(0, 2)

    def move_player(self, delta_x=0, delta_y=0):
        self.rect.move_ip(delta_x, delta_y)
        window_width, window_height = pygame.display.get_surface().get_size()
        x_coord, y_coord = self.rect.x, self.rect.y

        if x_coord < 0 or x_coord + self.rect.width > window_width \
                or y_coord < 0 or y_coord + self.rect.height > window_height:
            self.rect.move_ip(-delta_x, -delta_y)

    def face_to_direction(self, direction):
        if self.direction != direction:
            if direction == self.PLAYER_DIRECTION_RIGHT:
                self.image = self._images["player_facing_right"]
            else:
                self.image = self._images["player_facing_left"]
        self.direction = direction
