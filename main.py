from bot.brr_bot import BrrBot
from data import env
from data.database.database import Database

Database.init()

Database.debug.display_ranks()
BrrBot().run(env.getToken())
