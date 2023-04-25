import unittest
import pygame

from sprites.player import Player
from play_zone import PlayZone


class TestPlayer(unittest.TestCase):
    def test_cannot_pass_left_wall(self):
        zone = PlayZone()
        zone.player1.player_moving[0] = True
        for i in range(1000):
            zone.update_player_positions()
        self.assertGreater(zone.player1.rect.x, -1)
