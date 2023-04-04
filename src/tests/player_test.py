import unittest
import pygame

from sprites.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.test_player = Player()

    def test_can_move_to_directions(self):
        expected = [-2, -2, 2, 2]
        for i in range(4):
            player_mov = [False] * 4
            player_mov[i] = True
            self.test_player.player_moving = list(player_mov)
            self.test_player.rect.y = 0
            self.test_player.rect.x = 0
            self.test_player.update()
            coordinate = [self.test_player.rect.y, self.test_player.rect.x][1 - i % 2]
            self.assertEqual(coordinate, expected[i])