import unittest
import pygame

from sprites.player import Player
from play_zone import PlayZone


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.zone = PlayZone()

    def test_cannot_pass_left_wall(self):
        self.zone.player1.player_moving[0] = True
        for i in range(1000):
            self.zone.update_player_positions()
        self.assertGreater(self.zone.player1.rect.x, -1)