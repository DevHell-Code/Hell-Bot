import discord
from discord.ext import commands
import random
import math


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # 삼각함수(사인, 코사인, 탄젠트)
    # 유머
    @commands.command()
    async def 삼각함수송(self, ctx):
      await ctx.reply(embed=embed('삼각합수송', 'r분의 y~ 사인 함수~ r분의 x~ 코사인함수~ x분의 y~ 탄젠트함수~ 정의를 정확하게 알아야지요~ \n https://www.youtube.com/watch?v=bTs0DcMxDT8'))
    # 사인
    @commands.command()
    async def 사인(self, ctx, annum: int):
      data = math.sin(annum)
      await ctx.reply(embed=embed('삼각함수 in 사인', f'{annum}의 사인 값은 {data}입니다.'))
    #코사인
    @commands.command()
    async def 코사인(self, ctx, annum: int):
      data = math.cos(annum)
      await ctx.reply(embed=embed('삼각함수 in 코사인', f'{annum}의 코사인 값은 {data}입니다.'))
    #코사인
    @commands.command()
    async def 탄젠트(self, ctx, annum: int):
      data = math.tan(annum)
      await ctx.reply(embed=embed('삼각함수 in 탄젠트', f'{annum}의 탄젠트 값은 {data}입니다.'))
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
