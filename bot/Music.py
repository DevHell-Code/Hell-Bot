import discord
from discord.ext import commands
import random


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.is_owner()
    async def VoiceChannelTest(self, ctx, status):
      if status == 'Connect':      
        try:
          global vc
          vc = await ctx.message.author.voice.channel.connect()
        except:
          try:
            await vc.move.to(ctx.message.author.voice.channel)
          except:
            await ctx.reply(embed=embed('음악 기능 오류', '사용자가 음성 채널에 있지 않습니다.', discord.Color.red()))
      elif status == 'DisConnect' :
        try:
          await vc.disconnect()
        except:
          await ctx.reply(embed=embed('음악 기능 오류', '이미 음성 채널 밖입니다.', discord.Color.red()))
          

def setup(bot):
    bot.add_cog(Music(bot))