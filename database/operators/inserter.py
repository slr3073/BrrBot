import sqlite3
from member import Member
from rank import Rank

class Inserter(object):
    @staticmethod
    def insert_member(member: Member) -> None:
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('INSERT INTO Member VALUES (?,?)', (member.id, member.name))

    @staticmethod
    def insert_rank(rank: Rank) -> None:
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('INSERT INTO Rank VALUES (?,?)', (rank.id, rank.name))