import discord
import base64
from discord.ext import commands
import random

# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)
  
class code(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 암호화(self, ctx, text):
      data = ascii_encrypt(text)
      ctx.reply(embed=embed(f'암호화', '아스키 코드 기반의 암호화입니다. \n ||{data}||'))

def setup(bot):
    bot.add_cog(code(bot))