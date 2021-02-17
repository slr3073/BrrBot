import sqlite3
from database.operators.deleter import Deleter
from database.operators.displayer import Displayer
from database.operators.fetcher import Fetcher
from database.operators.inserter import Inserter
from database.operators.updater import Updater

class Brr_db(object):
    fetch = Fetcher()
    update = Updater()
    delete = Deleter()
    insert = Inserter()
    display = Displayer()

    @staticmethod
    def init_db() -> None:
        with sqlite3.connect('database/brr_bot.db') as connexion:
            cursor = connexion.cursor()
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Member (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL
                            )""")
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Rank (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL
                            )""")




