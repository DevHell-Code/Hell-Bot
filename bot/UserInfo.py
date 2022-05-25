import discord
from discord.ext import commands
import os
import random

# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 사용자정보(self, ctx, member: discord.Member):
      await ctx.reply(embed=embed('사용자 정보', f'{member} \n {member.avatar_url}'))
      
def setup(bot):
    bot.add_cog(UserInfo(bot))