import unittest
import pygame

from sprites.player import Player
from play_zone import PlayZone


class TestMonster(unittest.TestCase):
    def test_catches_player1(self):
        zone = PlayZone()
        # Move coin outside the field so it can't be acquired by a player.
        zone.coin.rect.x = -100000
        for i in range(1000):
            zone.update()
            if zone.game_over:
                break

        self.assertEqual(zone.game_over,
                         True)

    def test_catches_player2(self):
        zone = PlayZone()
        # Move coin outside the field so it can't be acquired by a player.
        zone.coin.rect.x = -100000
        zone.coin.location = zone.coin.COIN_LOCATION_RIGHT  # Chase player 2.

        for i in range(1000):
            zone.update()
            if zone.game_over:
                break

        self.assertEqual(zone.game_over,
                         True)
