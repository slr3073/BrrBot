import discord

bot_token = 'ODA3ODgyNjUyMzA0NDA4NTg2.YB-dWg.7jeeo0sGv0ts56hlXv54353aBAI'
client = discord.Client()

channel_test = client.get_channel(482182097461575682)
channel_general = client.get_channel(807909900671385632)


@client.event
async def on_ready():
    print('Logged in as {0}'.format(client.user))


client.run(bot_token)
