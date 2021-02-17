import sqlite3
from member import Member

class Brr_db(object):
    @staticmethod
    def init_db():
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Member (
                                id integer,
                                name text
                            )""")

    @staticmethod
    def insert_member(member: Member):
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            print(f"{member.id} et {member.name}")
            cursor.execute('INSERT INTO Member VALUES (?,?)', (member.id, member.name))

    @staticmethod
    def print_members():
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute('SELECT * FROM Member')
            print(cursor.fetchall())

