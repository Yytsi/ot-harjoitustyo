import random
import pygame
from sprites.player import Player
from sprites.monster import Monster
from sprites.coin import Coin
from sprites.line import Line


class PlayZone:
    def __init__(self, player1_name="Player 1", player2_name="Player 2"):
        self.player1 = None
        self.player2 = None
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.monster = None
        self.middle_wall = None
        self.coin = None
        self.players = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.game_over = False
        self.current_score = 0

        if pygame.display.get_surface() is None:
            self.window_width = 640
            self.window_height = 400
        else:
            self.window_width, self.window_height = pygame.display.get_surface().get_size()

        self._initialize_sprites()

    def get_score_text(self):
        font = pygame.font.Font(
            pygame.font.get_default_font(), int((self.window_width / 640)*20))
        text_surface = font.render(
            f"Score: {self.current_score}", True, (153, 255, 153))
        return (text_surface, (10, 10))

    def _initialize_sprites(self):
        # Scale the images according to the width of the game window.
        scale_factor = self.window_width / 640
        self.middle_wall = Line(self.window_width // 2,
                                0, 1, self.window_height)
        self.player1 = Player(50, 50, int(
            scale_factor * 33), int(scale_factor * 63))
        self.player2 = Player(400, 200, int(
            scale_factor * 33), int(scale_factor * 63))
        self.monster = Monster(self.window_width // 2, self.window_height // 2, int(
            scale_factor * 48), int(scale_factor * 60))

        self.monster.rect.x -= self.monster.rect.width // 2
        self.monster.rect.y -= self.monster.rect.height // 2

        self.coin = Coin(self.window_width * 2, self.window_height * 2, int(scale_factor * 32),
                         int(scale_factor * 32))

        self.replace_coin()

        self.players.add(self.player1, self.player2)
        self.all_sprites.add(self.coin, self.players,
                             self.middle_wall, self.monster)

    def replace_coin(self):
        new_box_x = random.randint(
            0, self.window_width // 2 - self.coin.rect.width)
        new_box_y = random.randint(
            0, self.window_height - self.coin.rect.height)

        if self.coin.location == Coin.COIN_LOCATION_LEFT:
            self.coin.location = Coin.COIN_LOCATION_RIGHT
            self.coin.rect.x = new_box_x + self.window_width // 2
            self.coin.rect.y = new_box_y
        else:
            self.coin.location = Coin.COIN_LOCATION_LEFT
            self.coin.rect.x = new_box_x
            self.coin.rect.y = new_box_y

    def update_player_positions(self):
        for player in self.player1, self.player2:
            prev_x, prev_y = player.rect.x, player.rect.y
            player.update()
            if pygame.sprite.collide_rect(player, self.middle_wall):
                player.rect.x = prev_x
                player.rect.y = prev_y
            elif player.rect.x < 0 or player.rect.x + player.rect.width > self.window_width \
                    or player.rect.y < 0 or player.rect.y + player.rect.height > self.window_height:
                player.rect.x = prev_x
                player.rect.y = prev_y

    def update(self):
        self.update_player_positions()

        # Check if a player hits the monster.
        if pygame.sprite.spritecollide(self.monster, self.players, False):
            self.game_over = True

        # Check if a player hits the coin.
        if pygame.sprite.spritecollide(self.coin, self.players, False):
            self.replace_coin()
            self.current_score += 1

        # Move monster.
        self.monster.chase_player(
            self.player1 if self.coin.location == Coin.COIN_LOCATION_LEFT else self.player2)
