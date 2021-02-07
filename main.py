import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    channel_test = client.get_channel(807909900671385632)
    print('Logged in as {0}'.format(client.user))
    await channel_test.send('Jsuis pret batard')


client.run(os.getenv("TOKEN"))
