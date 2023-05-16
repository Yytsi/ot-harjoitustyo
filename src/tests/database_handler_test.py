import unittest
import os

from database_handler import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.db_handler = DatabaseHandler("test.db")
        self.db_handler.empty_scores()

    def test_empty_table(self):
        best_score = self.db_handler.get_highest_score_team()

        self.assertEqual(best_score, (None, None, None))

    def test_max_single_team(self):
        self.db_handler.add_score("James", "Julia", 15)

        best_score = self.db_handler.get_highest_score_team()

        self.assertEqual(best_score, ("James", "Julia", 15))

    def test_max_from_many_different_score_teams(self):
        self.db_handler.add_score("James", "Julia", 15)
        self.db_handler.add_score("Jukka", "Joonas", 14)
        self.db_handler.add_score("Jarmo", "Liisa", 16)

        best_score = self.db_handler.get_highest_score_team()

        self.assertEqual(best_score, ("Jarmo", "Liisa", 16))

    def test_same_score_teams_take_first(self):
        self.db_handler.add_score("Aaro", "Maija", 15)
        self.db_handler.add_score("Johan", "Jake", 15)

        best_score = self.db_handler.get_highest_score_team()

        self.assertEqual(best_score, ("Aaro", "Maija", 15))

    def test_weird_name(self):
        self.db_handler.add_score("!63/&%€", "'¨å239?´", 15)

        best_score = self.db_handler.get_highest_score_team()

        self.assertEqual(best_score, ("!63/&%€", "'¨å239?´", 15))
