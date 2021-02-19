import sqlite3

class Deleter(object):
    @staticmethod
    def delete_rank(rank_id: int) -> None:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute("DELETE FROM Rank WHERE Rank.id = ?", (rank_id,))

    @staticmethod
    def delete_member(member_id: int) -> None:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute("DELETE FROM Member WHERE Member.id = ?", (member_id,))

