import discord
from discord.ext import commands
import random
import datetime
import requests


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)

async def timeout_user(bot, *, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    session = requests.patch(url, json=json, headers=headers)
    if session.status_code in range(200, 299):
        return session.json()

async def remove_timeout_user(bot, *, user_id: int, guild_id: int):
    headers = {"Authorization": f"Bot {bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    json = {'communication_disabled_until': None}
    session = requests.patch(url, json=json, headers=headers)
    if session.status_code in range(200, 299):
        return session.json()

class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 삭제(self, ctx, *, amount=999999999999999999999):
        if ctx.author.guild_permissions.manage_messages:
            try:
                await ctx.channel.purge(limit=amount)
            except:
                await ctx.reply(embed=embed("삭제 실패","http://hellcode.cf를 이용해 메시지 관리 권한과 함께 초대해주세요.",discord.Color.red()))
            if amount == 999999999999999999999:
                await ctx.reply(embed=embed("삭제 완료","이 채널에 있는 모든 메시지(매우 오래된 메시지 제외)가 삭제되었습니다!",discord.Color.green()))
            else:
                await ctx.reply(embed=embed("삭제 완료",f"{amount}개의 메시지가 삭제되었습니다!",discord.Color.green()))
        else:
            await ctx.reply(embed=embed("삭제 실패",'메시지 관리권한이 없습니다.',discord.Color.red()))
    @commands.command()
    async def timeout(self, ctx, user:discord.Member, min:int):
        handshake = await timeout_user(bot=self.bot, user_id=user.id, guild_id=ctx.guild.id, until=min)
        if handshake:
             return await ctx.send(embed=embed("타임아웃 완료",f"{user}님을 {min}분동안 타임아웃 시켰습니다.",discord.Color.green()))
    @commands.command()
    async def removetimeout(self, ctx, user:discord.Member):
        handshake = await remove_timeout_user(bot=self.bot, user_id=user.id, guild_id=ctx.guild.id)
        if handshake:
             return await ctx.send(embed=embed("타임아웃 해제 완료",f"{user}님의 타임아웃을 해제시켰습니다.",discord.Color.green()))
def setup(bot):
    bot.add_cog(Manage(bot))
