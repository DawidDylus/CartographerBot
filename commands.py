import discord
from commandCalls import cmd


bot = discord.Client()

async def onMessage(msg):

  if msg.content.startswith(cmd.HELLO.value):
    await msg.channel.send('Welcome to my shop, traveler!')

  


