import discord
from discord.ext import commands
import os
import asyncio
import time
import random
import re
import json
from PIL import Image, ImageDraw, ImageFont
import textwrap

file = open("bot/sentences_kor.txt", "r")
line = file.readlines()
sentenses_kor = []
for i in line:
    sentenses_kor.append(i.strip())
file.close()

file = open("bot/sentences_eng.txt", "r")
line = file.readlines()
sentenses_eng = []
for i in line:
    sentenses_eng.append(i.strip())
file.close()

# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 주사위
    @commands.command()
    async def 주사위(self, ctx):
        dice = 1, 2, 3, 4, 5, 6
        await ctx.reply(
            embed=embed('주사위', f'||결과는?! {random.choice(dice)} 입니다!||'))

    # 뽑기
    @commands.command()
    async def 뽑기(self, ctx, nber: str):
        rannber = random.choice(['1', '2', '3 '])
        if nber == rannber:
            await ctx.reply(embed=embed(
                '뽑기', f'맞았습니다! \n 나의 선택: {nber} \n  봇의 선택: {rannber}',
                discord.Color.green()))
        else:
            await ctx.reply(embed=embed(
                '뽑기', f'틀렸습니다! \n 나의 선택: {nber} \n  봇의 선택: {rannber}',
                discord.Color.red()))

    # 홀짝
    @commands.command()
    async def 홀짝(self, ctx, hollans):
        hollrad = random.choice(['홀', '짝'])
        if hollans == hollrad:
            await ctx.reply(embed=embed(
                '홀짝', f'맞았습니다! \n 내 선택: {hollans} \n 봇의 선택: {hollrad}',
                discord.Color.green()))
        else:
            await ctx.reply(embed=embed(
                '홀짝', f'틀렸습니다! \n 내 선택: {hollans} \n 봇의 선택: {hollrad}',
                discord.Color.red()))

    # 가위바위보
    @commands.command()
    async def 가위바위보(self, ctx, rsp):
        rsps = '가위', '바위', '보'
        rspchoice = random.choice(rsps)
        if rspchoice == '가위':
            if rsp == '가위':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 비겼네요!'))
            elif rsp == '바위':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 제가 졌네요!'))
            elif rsp == '보':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 제가 이겼네요!'))
            else:
                await ctx.reply(
                    embed=embed('Error in \'가위바위보\'',
                                '가위, 바위, 보 중 내주세요! 그렇지 않으면 봇이 인식하지 못해요 ㅠㅠ'))
        if rspchoice == '바위':
            if rsp == '가위':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 제가 이겼네요!'))
            elif rsp == '바위':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 비겼네요!'))
            elif rsp == '보':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 제가 졌네요!'))
            else:
                await ctx.reply(
                    embed=embed('Error in \'가위바위보\'',
                                '가위, 바위, 보 중 내주세요! 그렇지 않으면 봇이 인식하지 못해요 ㅠㅠ'))
        if rspchoice == '보':
            if rsp == '가위':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 제가 졌네요!'))
            elif rsp == '바위':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 제가 이겼네요!'))
            elif rsp == '보':
                await ctx.reply(embed=embed(
                    '가위바위보',
                    f'사용자가 낸 것: {rsp} \n 봇이 낸 것: {rspchoice} \n 비겼네요!'))
            else:
                await ctx.reply(
                    embed=embed('Error in \'가위바위보\'',
                                '가위, 바위, 보 중 내주세요! 그렇지 않으면 봇이 인식하지 못해요 ㅠㅠ'))

    @commands.command()
    async def 타자(self, ctx, arg=None):
        if arg == "영어":
            q = random.choice(sentenses_eng)
            H = 350
        elif arg == "한글":
            q = random.choice(sentenses_kor)
            H = 250
        elif arg == None:
            arg = random.choice(["한글","영어"])
            if arg == "영어":
                q = random.choice(sentenses_eng)
                H = 350
            elif arg == "한글":
                q = random.choice(sentenses_kor)
                H = 250
        W = 550
        bg_color = 'rgb(214, 230, 245)'
        
        font = ImageFont.truetype('font.ttf', size=28)
        font_color = 'rgb(0, 0, 0)'
        image =Image.new('RGB', (W, H), color = bg_color)
        draw = ImageDraw.Draw(image)
        if arg == "한글":
            lines = textwrap.wrap(q, width=20)
        elif arg == "영어":
            lines = textwrap.wrap(q, width=30)
        x_text = 50
        y_text = 50
        for line in lines:
            width, height = font.getsize(line)
            draw.text((x_text, y_text), line, font=font, fill=font_color)
            y_text += height
        image.save("text.png")
        file = discord.File("text.png", filename="text.png")
        start_time = time.time()
        await ctx.reply(file=file, embed=embed("타자연습 시작",f"다음 문장을 100초 안에 입력해주세요!").set_image(url="attachment://text.png"))
        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        try:
            user_input = await self.bot.wait_for('message', check=check, timeout=100)
        except asyncio.TimeoutError:
            return
        else:
            pass
        end_time = time.time() - start_time
        correct = 0
    
        for i,c in enumerate(user_input.content):
            if i>=len(q):
                break
            if c == q[i]:
                correct +=1
        total_len = len(q)
        c = round((correct/total_len*100),2)
        e = round((total_len - correct)/total_len*100,2)
        speed = round(int((correct/end_time) *60))
    
        await ctx.reply(embed=embed("성공",f"타수 : {speed} 정확도 : {c}% 오타율 : {e}%"))
        

  
def setup(bot):
    bot.add_cog(Game(bot))
