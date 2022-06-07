import discord
from discord.ext import commands
import random
import os
import requests
import json
import urllib.request
import time


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Dict(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      # 국립국어원 표준국어대사전 검색
    @commands.command()
    async def 국어사전(self, ctx, search):
        kodict = os.getenv("kodict")
        data = f'https://stdict.korean.go.kr/api/search.do?key={kodict}&type_search=search&req_type=json&q={search}'
        result = requests.get(data,verify=False).json()["channel"]
        definition = result['item'][0]['sense']['definition']
        pos = result["item"][0]['pos']
        await ctx.send(embed=embed(f"{search} [{pos}] 의 대한 검색결과",f"{definition}"))
        
def setup(bot):
    bot.add_cog(Dict(bot))
