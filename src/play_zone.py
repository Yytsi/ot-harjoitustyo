import pygame
from sprites.player import Player
from sprites.monster import Monster
from sprites.coin import Coin

class PlayZone:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.monster = None
        self.coins = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._initialize_sprites()
    
    def _initialize_sprites(self):
        # Place players in their own sides.
        self.player1 = Player()
        self.player2 = Player()
        self.monster = Monster()
        self.coins.add(Coin())

        self.players.add(self.player1, self.player2)
        self.all_sprites.add(self.coins, self.players, self.monster)