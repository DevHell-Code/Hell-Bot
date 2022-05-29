import discord
from discord.ext import commands
import random

# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)
# 각종 사이트 URL
KOWP = 'https://ko.wikipedia.org/wiki'
ENWP = 'https://en.wikipedia.org/wiki'
NAVER = 'https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query='
GOOGLE = 'https://www.google.com/search?q='

class Search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # 검색
    @commands.command()
    async def 검색(self, ctx, query):
      await ctx.reply(embed=embed('검색', f'**{query}**에 대한 검색 결과입니다. \n {KOWP}{query} \n {ENWP}{query} \n {NAVER}{query} \n {GOOGLE}{query}'))


def setup(bot):
    bot.add_cog(Search(bot))