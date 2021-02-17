from discord.ext import commands

class BrrBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=".")
    
    async def on_ready(self):
        channel_test = self.get_channel(807909900671385632)
        await channel_test.send('WeshWesh')




