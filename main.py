import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    await bot.change_presence()
    print(f"{bot.user.name} Login successful!")

@bot.command
async def 정보(ctx):
    await ctx.send(embed=discord.Embed(title='봇 정보', description='헬월이 1.0.0'))

bot.run(os.getenv("token"))