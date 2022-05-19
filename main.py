# 필요 모듈 불러오기
import discord
from discord.ext import commands
import os
import random
import re
from replit import db
from keep_alive import keep_alive

# 봇 변수 설정
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)

# 봇 준비 로그
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f"$도움 | {str(len(bot.guilds))}개의 서버와 함께"))
    print(f"{bot.user.name} Login successful!")

# 임배드 함수
def embed(title,description,color=discord.Color.purple()):
    return discord.Embed(title=title,description=description,color=color)

# 애러 핸들링
# @bot.listen()
async def on_command_error(ctx, error):
	print(error)
	m = re.search(r'You are on cooldown. Try again in (.*)s', str(error))
	if m:
		asdf = m.groups()[0]
		embed = discord.Embed(
		    title="잠시만요!",
		    description=f"쿨타임에 걸렸어요! 이 명령어를 {asdf}초 후에 다시 사용하실 수 있어요!")
		await ctx.message.reply(embed=embed)
		return
	else:
		m = re.search(r'Command "(.*)" is not found', str(error))
		if m:
			asdf = m.groups()[0]
			embed = discord.Embed(
			    title="잠시만요!",
			    description=
			    f"이 명령어를 사용할 수 없어요! `={asdf}`는 없는 명령어에요! 다른 명령어로 변경됐 수도 있으니 `=help`로 모든 명령어 목록을 보세요!"
			)
			await ctx.message.reply(embed=embed)
			return
		else:
			m = re.search(r'User "(.*)" not found.', str(error))
			if m:
				asdf = m.groups()[0]
				embed = discord.Embed(
				    title="잠시만요!",
				    description=
				    f"이 명령어를 사용할 수 없어요! `{asdf}`는 없는 사용자에요! 사용자 멘션이나 사용자의 풀 닉네임을 제시해주세요!"
				)
				await ctx.message.reply(embed=embed)
				return
			elif str(error) == "This command can only be used in private messages.":
				embed = discord.Embed(
				    title="잠시만요!",
				    description=
				    f"이 명령어를 사용할 수 없어요! 이 명령어는 제 DM으로만 사용할 수 있어요! 혹시 모르니 DM을 보내드릴게요!"
				)				
				await ctx.message.reply(embed=embed)
				await ctx.author.send("사용할 수 없던 명령어를 이곳, 제 DM에서 쳐보세요. 서버 채팅에서 친다면 누가 사용자님의 개인정보를 훔쳐갈지도 몰라요! :eyes:")
			else:
				embed = discord.Embed(
				    title="잠시만요!",
				    description=
				    f"이 명령어를 사용할 수 없어요! 발생한 오류는 다음과 같아요! \n\n```{str(error)}```"
				)
				await ctx.message.reply(embed=embed)
				return
# 정보
@bot.command()
async def 정보(ctx):
    await ctx.send(embed=embed('정보','헬월이 버전 1.0.0 \n Made By Dev HellCode, Github: https://github.com/DevHell-Code/Hell-Bot'))

# 크레딧
@bot.command()
async def 크레딧(ctx):
    await ctx.send(embed=embed('크레딧', 'Dev HellCode \n froggal(KeySpace), hminkoo10(Kongryeong)'))

# 주사위
@bot.command()
async def 주사위(ctx):
  dice = 1, 2, 3, 4, 5, 6
  await ctx.send(embed=embed('주사위', f'||{random.choice(dice)}||'))

# 가위바위보
@bot.command()
async def 가위바위보(ctx, rsp):
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
      
# 동작
keep_alive()
bot.run(os.getenv("token-beta"))