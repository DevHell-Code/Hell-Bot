import discord
from discord.ext import commands
import os
import asyncio
import random
import re

# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)

class Game(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    # 주사위
    @commands.command()
    async def 주사위(self, ctx):
      dice = 1, 2, 3, 4, 5, 6
      await ctx.send(embed=embed('주사위', f'||결과는?! {random.choice(dice)} 입니다!||'))
    
    # 가위바위보
    @commands.command()
    async def 가위바위보(self, ctx, rsp):
      rsps = '가위', '바위', '보'
      rspchoice = random.choice(rsps)
      if rspchoice == '가위':
        if rsp == '가위':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 비겼네요!'))
        elif rsp == '바위':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 제가 졌네요!'))
        elif rsp == '보':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 제가 이겼네요!'))
        else :
          await ctx.send(embed=embed('Error in \'가위바위보\'', '가위, 바위, 보 중 내주세요! 그렇지 않으면 헬월이가 인식하지 못해요 ㅠㅠ'))
      if rspchoice == '바위':
        if rsp == '가위':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 제가 이겼네요!'))
        elif rsp == '바위':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 비겼네요!'))
        elif rsp == '보':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 제가 졌네요!'))
        else :
          await ctx.send(embed=embed('Error in \'가위바위보\'', '가위, 바위, 보 중 내주세요! 그렇지 않으면 헬월이가 인식하지 못해요 ㅠㅠ'))
      if rspchoice == '보':
        if rsp == '가위':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 제가 졌네요!'))
        elif rsp == '바위':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 제가 이겼네요!'))
        elif rsp == '보':
          await ctx.send(embed=embed('가위바위보', f'사용자가 낸 것: {rsp} \n 헬월이가 낸 것: {rspchoice} \n 비겼네요!'))
        else :
          await ctx.send(embed=embed('Error in \'가위바위보\'', '가위, 바위, 보 중 내주세요! 그렇지 않으면 헬월이가 인식하지 못해요 ㅠㅠ'))

def setup(bot):
    bot.add_cog(Game(bot))