''# 필요 모듈 불러오기
import discord
from discord.ext import commands
import os
import random
from keep_alive import keep_alive

# 봇 변수 설정
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)

# 봇 준비 로그
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f"$도움 | {str(len(bot.guilds))}개의 서버와 함께"))
    print(f"{bot.user.name} Login successful!")

def embed(title,description,color=discord.Color.purple()):
    return discord.Embed(title=title,description=description,color=color)

# 정보 커멘드
@bot.command()
async def 정보(ctx):
    await ctx.send(embed=embed('정보','헬월이 버전 1.0.0 \n Made By Dev HellCode, Github: https://github.com/DevHell-Code/Hell-Bot'))

# 크레딧 커멘드
@bot.command()
async def 크레딧(ctx):
    await ctx.send(embed=embed('크레딧', 'Dev HellCode \n froggal(KeySpace), hminkoo10(Kongryeong)'))

# 주사위
@bot.command()
async def 주사위(ctx):
  dice = 1, 2, 3, 4, 5, 6
  await ctx.send(embed=embed('주사위', f'||{dice}||'))
  
# 동작
keep_alive()
bot.run(os.getenv("token"))