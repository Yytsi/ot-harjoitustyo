import unittest
import pygame

from sprites.player import Player
from play_zone import PlayZone


class TestMonster(unittest.TestCase):
    def test_chases_player(self):
        zone = PlayZone()
        monster_x = zone.monster.rect.x
        zone.monster.chase_player(zone.player2)
        self.assertEqual(zone.monster.rect.x - monster_x,
                         zone.monster.MONSTER_SPEED)
