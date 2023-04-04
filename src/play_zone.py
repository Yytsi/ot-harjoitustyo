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
        self.game_over = False

        self._initialize_sprites()
    
    def _initialize_sprites(self):
        # Place players in their own sides.
        self.player1 = Player(x=50, y=50)
        self.player2 = Player(x=300, y=200)
        self.monster = Monster(x=200, y=200)
        self.coins.add(Coin(x=100, y=100))

        self.players.add(self.player1, self.player2)
        self.all_sprites.add(self.coins, self.players, self.monster)
    
    def update(self):
        self.player1.update()
        self.player2.update()