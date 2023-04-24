import pygame
from play_zone import PlayZone
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock


class Game:
    def __init__(self, player1_name = "Player 1", player2_name = "Player 2"):
        self._display = pygame.display.set_mode((640, 400))

        self._play_zone = PlayZone(player1_name = player1_name, player2_name = player2_name)
        self._event_queue = EventQueue()
        self._renderer = Renderer(self._display, self._play_zone)
        self._clock = Clock()
        self._game_loop = GameLoop(
            self._play_zone,
            self._renderer,
            self._event_queue,
            self._clock
        )

    def play_game(self):
        pygame.init()
        self._game_loop.start()
