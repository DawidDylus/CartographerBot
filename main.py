import os
import discord
from keep_alive import keep_alive

from commands import onMessage

secretToken = os.environ['TOKEN']

bot = discord.Client()

@bot.event
async def on_ready():
  print("Another Day, another adventure for the {0.user}".format(bot))

@bot.event
async def on_message(message):
  # Ignore messages send by bot
  if message.author == bot:
    return

  await onMessage(message)


keep_alive()
bot.run(secretToken)