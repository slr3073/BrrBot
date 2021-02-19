import sqlite3

class Debugger(object):
    @staticmethod
    def display_members() -> None:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Member')
            for index, row in enumerate(cursor.fetchall()):
                row_id, row_name = row
                print(f"{index} - {row_name} n°{row_id}")

    @staticmethod
    def display_ranks() -> None:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Rank')
            for index, row in enumerate(cursor.fetchall()):
                row_id, row_name = row
                print(f"{index} - {row_name} n°{row_id}")
