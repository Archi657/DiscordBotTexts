import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('ready')

client.run('OTQxODg0MTExOTA2Mjc1Mzg4.Ygcb7w.VGaV83IfT5gaggpLjFn_sUjztOE')