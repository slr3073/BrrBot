import sqlite3

class Fetcher(object):

    @staticmethod
    def all_members() -> list:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Rank')
            return len(cursor.fetchall()) != 0

    @staticmethod
    def rank_exist(rank_id: int) -> bool:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Rank WHERE Rank.id = ?', (rank_id,))
            return len(cursor.fetchall()) != 0

    @staticmethod
    def member_exist(member_id: int) -> bool:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Member WHERE Member.id = ?', (member_id,))
            return len(cursor.fetchall()) != 0
