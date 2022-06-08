import discord
from discord.ext import commands
import random

# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Manage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def 삭제(ctx, *, amount=999999999999999999999):
        if ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount)
            if amount == 999999999999999999999:
                await ctx.reply(embed=embed("삭제 완료","이 채널에 있는 모든 메시지(매우 오래된 메시지 제외)가 삭제되었습니다!",discord.Color.green()))
            else:
                await ctx.reply(embed=embed("삭제 완료",f"{amount}개의 메시지가 삭제되었습니다!",colo))
        else:
            await ctx.reply('메시지 관리권한이 없습니다. https://bit.ly/joinbota를 이용해 관리 권한과 함께 초대해주세요.')
    
def setup(bot):
    bot.add_cog(Manage(bot))
