from bot.brr_bot import BrrBot
from managers import env_manager
from database.brr_db import Brr_db

Brr_db.init_db()

BrrBot().run(env_manager.getToken())
