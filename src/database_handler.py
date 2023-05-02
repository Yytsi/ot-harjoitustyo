import sqlite3
import os

# chatGPT-4 helped generate the following code.


class DatabaseHandler:
    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.db_path = os.path.join(dirname, "..", "data", "scores.db")
        self.create_table()

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
        except sqlite3.Error:
            pass
        return conn

    def create_table(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS scores (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            player1_name TEXT NOT NULL,
                            player2_name TEXT NOT NULL,
                            score INTEGER NOT NULL
                        );""")
        connection.commit()
        connection.close()

    def add_score(self, player1_name, player2_name, score):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO scores (player1_name, player2_name, score)
                          VALUES (?, ?, ?);""", (player1_name, player2_name, score))
        connection.commit()
        connection.close()

    def get_highest_score_team(self):
        connection = self.create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """SELECT player1_name, player2_name, MAX(score) FROM scores;""")
        result = cursor.fetchone()
        connection.close()
        return result
