import pygame
from sprites.player import Player
from sprites.monster import Monster
from sprites.coin import Coin
from sprites.line import Line


class PlayZone:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.monster = None
        self.middle_wall = None
        self.coins = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.game_over = False

        self._initialize_sprites()

    def _initialize_sprites(self):
        # Scale the images according to the width of the game window.
        window_width, window_height = pygame.display.get_surface().get_size()
        scale_factor = window_width / 640
        self.middle_wall = Line(window_width // 2, 0, 1, window_height)
        self.player1 = Player(50, 50, int(scale_factor * 33), int(scale_factor * 63))
        self.player2 = Player(400, 200, int(scale_factor * 33), int(scale_factor * 63))
        self.monster = Monster(200, 200, int(scale_factor * 48), int(scale_factor * 60))
        self.coins.add(Coin(100, 100, int(scale_factor * 32), int(scale_factor * 32)))

        self.players.add(self.player1, self.player2)
        self.all_sprites.add(self.coins, self.players, self.monster, self.middle_wall)

    def update(self):
        for player in self.player1, self.player2:
            prev_x, prev_y = player.rect.x, player.rect.y
            player.update()
            if pygame.sprite.collide_rect(player, self.middle_wall):
                player.rect.x = prev_x
                player.rect.y = prev_y

        # Check if a player hits the monster.
        if pygame.sprite.spritecollide(self.monster, self.players, False):
            self.game_over = True
