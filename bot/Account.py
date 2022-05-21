import discord
from discord.ext import commands
import os
import asyncio
import random
import cryptocode
import re
import pymongo

# mongodb 가져오기
client = pymongo.MongoClient("mongodb+srv://hellcode:hellcodepw@cluster0.ojd9r.mongodb.net/?retryWrites=true&w=majority")
db = client["accountdb"]
dbac = db["inf"]

# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # 정보
    @commands.command()
    @commands.dm_only()
    async def 회원가입(self, ctx):
        def check(author):
            def inner_check(message):
                return message.author == author
            return inner_check
        await ctx.reply(embed=embed("진행중","회원가입을 할 아이디를 30초 내에 입력 해 주세요!"))
        msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
        dkdlel = msg.content
        def check(author):
            def inner_check(message):
                return message.author == author
            return inner_check
        await ctx.reply(embed=embed("진행중","회원가입을 할 비밀번호를 30초 내에 입력 해 주세요! \n입력하신 비밀번호는 안전하게 보관됩니다."))
        msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
        print(msg.content)
        pwd = cryptocode.encrypt(msg.content, "pw")
        userinf = {f"{dkdlel}":f"{pwd}"}
        dbac.insert_one(userinf)

def setup(bot):
    bot.add_cog(Account(bot))