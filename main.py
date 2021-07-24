import os
import discord
from keep_alive import keep_alive
secretToken = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print("Another Day, another adventure for the {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Welcome to my shop, traveler!')

keep_alive()
client.run(secretToken)