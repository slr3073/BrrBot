import sqlite3
from data.database.operators.deleter import Deleter
from data.database.operators.debugger import Debugger
from data.database.operators.fetcher import Fetcher
from data.database.operators.inserter import Inserter
from data.database.operators.updater import Updater

class Database(object):
    fetch = Fetcher()
    update = Updater()
    delete = Deleter()
    insert = Inserter()
    debug = Debugger()

    @staticmethod
    def init() -> None:
        with sqlite3.connect('data/brr_bot.db') as connexion:
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
