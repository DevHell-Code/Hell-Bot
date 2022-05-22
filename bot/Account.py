import discord
from discord.ext import commands
import os
import asyncio
import random
import cryptocode
import re
import base64
import json
from github import Github
from github import InputGitTreeElement
import requests




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
        jstring = open("db.json", "r", encoding='utf-8-sig').read()
        db = json.loads(jstring)
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
        pwd = cryptocode.encrypt(msg.content, "pw")
        db[dkdlel] = pwd
        with open(f"db.json", "w+", encoding='utf-8-sig') as f:
            json_string = json.dump(db, f, indent=2, ensure_ascii=False)
        await ctx.send("회원가입완료")

def setup(bot):
    bot.add_cog(Account(bot))