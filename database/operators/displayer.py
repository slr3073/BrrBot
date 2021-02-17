import sqlite3

class Displayer(object):
    @staticmethod
    def members() -> None:
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Member')
            print(f"Members : {cursor.fetchall()}")

    @staticmethod
    def ranks() -> None:
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Rank')
            print(f"Ranks : {cursor.fetchall()}")
