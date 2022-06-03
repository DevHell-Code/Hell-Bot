import discord
from discord.ext import commands
import random


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 사칙연산
    @commands.command()
    async def 사칙연산(self, ctx, type, left: int, right: int):
        if type == '덧셈':
            data = left + right
            await ctx.reply(
                embed=embed('사칙연산 in 덧셈', f'{left}+{right} = {data}'))
        elif type == '뺄셈':
            data = left - right
            await ctx.reply(
                embed=embed('사칙연산 in 뺄셈', f'{left}-{right} = {data}'))
        elif type == '곱셈':
            data = left * right
            await ctx.reply(
                embed=embed('사칙연산 in 곱셈', f'{left}X{right} = {data}'))
        elif type == '나눗셈':
            data = left / right
            await ctx.reply(
                embed=embed('사칙연산 in 곱셈', f'{left}/{right} = {data}'))


def setup(bot):
    bot.add_cog(Calc(bot))
