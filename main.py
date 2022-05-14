import discord
from discord.ext import commands
import random
import asyncio
import os
import json
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    await bot.change_presence()
    print(f'{bot.user.name} 준비 끝!')

bot.run(os.getenv("token"))