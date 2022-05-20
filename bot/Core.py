import discord
from discord.ext import commands
import os
import asyncio
import random
import re


# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # 정보
    @commands.command()
    async def 정보(self, ctx):
        await ctx.reply(embed=embed('정보','헬월이 버전 1.0.0 \n Made By Dev HellCode, Github: https://github.com/DevHell-Code/Hell-Bot'))
    
    # 크레딧
    @commands.command()
    async def 크레딧(self, ctx):
        await ctx.reply(embed=embed('크레딧', 'Dev HellCode \n froggal(KeySpace), hminkoo10(Kongryeong)'))

def setup(bot):
    bot.add_cog(Core(bot))