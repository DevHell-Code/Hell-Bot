import discord
from discord.ext import commands
import os
import asyncio
import random
import cryptocode
import re
import base64
import json
import requests
import replit
import urllib.request
import time

a = urllib.request.urlopen("https://dbtest.hminkoo10.repl.co/dburl").read()
db = replit.Database(a.decode('utf-8'))
db["account"] = {}
acdb = {}
# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        global acdb
        while True:
            acdb = db["account"]
            await asyncio.sleep(1)
    # 회원가입
    @commands.command()
    @commands.dm_only()
    async def 회원가입(self, ctx):
        global acdb
        def check(author):
            def inner_check(message):
                return message.author == author
            return inner_check
        await ctx.reply(embed=embed("가입 진행중","회원가입을 할 아이디를 30초 내에 입력 해 주세요!"))
        msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
        dkdlel = msg.content
        if dkdlel in acdb:
            await ctx.reply(embed=embed("회원가입 실패","이미 있는 아이디입니다."))
            return
        if ctx.author.id in dict(acdb.keys())["linkac"]:
            await ctx.reply(embed=embed("회원가입 실패","이미 만들어진 아이디가 있습니다."))
            return
        def check(author):
            def inner_check(message):
                return message.author == author
            return inner_check
        await ctx.reply(embed=embed("가입 진행중","회원가입을 할 비밀번호를 30초 내에 입력 해 주세요! \n입력하신 비밀번호는 안전하게 보관됩니다."))
        msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
        pwd = cryptocode.encrypt(msg.content, "pw")
        acdb[dkdlel] = {"pwd":pwd,"badge":["<:indev:980372692047888434>"],"grade":"normal","linkac":ctx.author.id}
        db["account"] = acdb        
        await ctx.reply(embed=embed("가입 완료",f'가입이 완료되었습니다. 헬월이를 이용해주셔서 감사합니다, {ctx.author}님.'))

    @commands.command()
    @commands.is_owner()
    @commands.dm_only()
    async def DB확인(self, ctx, db1):
      await ctx.reply(db[f"{db1}"])
def setup(bot):
    bot.add_cog(Account(bot))