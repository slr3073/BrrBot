import sqlite3
from data.wrappers.member import Member
from data.wrappers.rank import Rank

class Inserter(object):
    @staticmethod
    def member(member: Member) -> None:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('INSERT INTO Member VALUES (?,?)', (member.id, member.name))

    @staticmethod
    def rank(rank: Rank) -> None:
        with sqlite3.connect('data/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('INSERT INTO Rank VALUES (?,?)', (rank.id, rank.name))
