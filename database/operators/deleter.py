import sqlite3

from member import Member
from rank import Rank

class Deleter(object):
    @staticmethod
    def delete_rank(rank: Rank) -> None:
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute("DELETE FROM Rank WHERE Rank.id = ?", (rank.id,))

    @staticmethod
    def delete_member(member: Member) -> None:
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute("DELETE FROM Member WHERE Member.id = ?", (member.id,))
