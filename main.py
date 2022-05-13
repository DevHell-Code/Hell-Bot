import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash import SlashContext
from discord_slash.utils import manage_commands
import random
import asyncio
import os
from keep_alive import keep_alive
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$",intents=intents)
slash = SlashCommand(bot, sync_commands=True)

bot.run(os.getenv("token"))