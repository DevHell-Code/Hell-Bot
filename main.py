# 필요 모듈 불러오기
import discord
from discord.ext import commands
import os
import asyncio
import random
import re
from keep_alive import keep_alive

# 임배드 함수
def embed(title,description,color=random.randint(0x000000,0xFFFFFF)):
    return discord.Embed(title=title,description=description,color=color)

# 봇 변수 설정
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents,owner_ids = [906351533426356226,712290125505363980])

# 코그 로드
for file in os.listdir("bot"):
    if file.endswith(".py"):
        bot.load_extension(f"bot.{file[:-3]}")
        print(f"bot.{file[:-3]}가 로드되었습니다")
    
# 봇 준비 로그
@bot.event
async def on_ready():
    print(f"{bot.user.name} Login successful!")
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f"$도움 | {str(len(bot.guilds))}개의 서버와 함께"))
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=f"Ver. INDEV 4.0 | {str(len(bot.guilds))}개의 서버와 함께"))
        await asyncio.sleep(5)


# Error
@bot.listen()
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
			    f"이 명령어를 사용할 수 없어요! `${asdf}`는 없는 명령어에요! 다른 명령어로 변경됐 수도 있으니 `$help`로 모든 명령어 목록을 보세요!"
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

# 초대시 (With, NaruBot)
@bot.listen()
async def on_guild_join(guild):
    await guild.owner.send(f'`{bot.user.name}`를 {guild.name}에 초대해주셔서 감사드립니다!\n앞으로 {bot.user.name}는 더 발전하겠습니다. \n https://koreanbots.dev/bots/928597866870616075 여기서 하트추가를 눌러주시면 감사하겠습니다!')

@bot.command(name="리로드")
@commands.is_owner()
async def reload(ctx, module="all"):
    try:
        if module == "all":
            embeds = await ctx.reply(embed=embed("리로드중","잠시만 기다려 주세요!"))
            await asyncio.sleep(2)
            modules = []
            for file in os.listdir("bot"):
                if file.endswith(".py"):
                    modules.append(file[:-3])
                    await asyncio.sleep(1)
                    await embeds.edit(embed=embed("리로드중",f"{file[:-3]} 리로드중 <a:loading:977169862000533504>"))
                    bot.unload_extension(f"bot.{file[:-3]}")
                    bot.load_extension(f"bot.{file[:-3]}")
                    await asyncio.sleep(1)
                    await embeds.edit(embed=embed("리로드중",f"{file[:-3]} 리로드완료 <a:yes:977162736691740702>",discord.Color.green()))
            mod = ""
            for i in modules:
                mod = f"{mod}{i}\n"
            await embeds.edit(embed=embed("리로드 완료 <a:yes:977162736691740702>", f"리로드가 완료되었습니다!\n리로드한 모듈\n{mod}",discord.Color.green()))
        else:
            embeds = await ctx.reply(embed=embed("리로드중","잠시만 기다려 주세요!"))
            await asyncio.sleep(2)
            bot.unload_extension(f"bot.{module}")
            bot.load_extension(f"bot.{module}")
            await embeds.edit(embed=embed("리로드 완료 <a:yes:977162736691740702>", f"{module}모듈 리로드가 완료되었습니다!",discord.Color.green()))
    except:
        await ctx.reply(embed=embed("리로드 실패 <a:no:977162736502976513>","모듈 이름을 다시 확인 해 주세요"))
@bot.command(name="언로드")
@commands.is_owner()
async def unload(ctx, module="all"):
    try:
        if module == "all":
            embeds = await ctx.reply(embed=embed("언로드중","잠시만 기다려 주세요!"))
            await asyncio.sleep(2)
            modules = []
            for file in os.listdir("bot"):
                if file.endswith(".py"):
                    modules.append(file[:-3])
                    await asyncio.sleep(1)
                    await embeds.edit(embed=embed("언로드중",f"{file[:-3]} 언로드중 <a:loading:977169862000533504>"))
                    bot.unload_extension(f"bot.{file[:-3]}")
                    await asyncio.sleep(1)
                    await embeds.edit(embed=embed("언로드중",f"{file[:-3]} 언로드완료 <a:yes:977162736691740702>",discord.Color.green()))
            mod = ""
            for i in modules:
                mod = f"{mod}{i}\n"
            await embeds.edit(embed=embed("언로드 완료 <a:yes:977162736691740702>", f"언로드가 완료되었습니다!\n언로드한 모듈\n{mod}",discord.Color.green()))
        else:
            embeds = await ctx.reply(embed=embed("언로드중","잠시만 기다려 주세요!"))
            await asyncio.sleep(2)
            bot.unload_extension(f"bot.{module}")
            bot.load_extension(f"bot.{module}")
            await embeds.edit(embed=embed("언로드 완료 <a:yes:977162736691740702>", f"{module}모듈 언로드가 완료되었습니다!",discord.Color.green()))
    except Exception as e:
        print(str(e))
        await ctx.reply(embed=embed("언로드 실패 <a:no:977162736502976513>","모듈 이름을 다시 확인 해 주세요"))

@bot.command(name="로드")
@commands.is_owner()
async def load(ctx, module="all"):
    try:
        if module == "all":
            embeds = await ctx.reply(embed=embed("로드중","잠시만 기다려 주세요!"))
            await asyncio.sleep(2)
            modules = []
            for file in os.listdir("bot"):
                if file.endswith(".py"):
                    modules.append(file[:-3])
                    await asyncio.sleep(1)
                    await embeds.edit(embed=embed("로드중",f"{file[:-3]} 로드중 <a:loading:977169862000533504>"))
                    bot.load_extension(f"bot.{file[:-3]}")
                    await asyncio.sleep(1)
                    await embeds.edit(embed=embed("로드중",f"{file[:-3]} 로드완료 <a:yes:977162736691740702>",discord.Color.green()))
            mod = ""
            for i in modules:
                mod = f"{mod}{i}\n"
            await embeds.edit(embed=embed("로드 완료 <a:yes:977162736691740702>", f"로드가 완료되었습니다!\n로드한 모듈\n{mod}",discord.Color.green()))
        else:
            embeds = await ctx.reply(embed=embed("로드중","잠시만 기다려 주세요!"))
            await asyncio.sleep(2)
            bot.unload_extension(f"bot.{module}")
            bot.load_extension(f"bot.{module}")
            await embeds.edit(embed=embed("로드 완료 <a:yes:977162736691740702>", f"{module}모듈 로드가 완료되었습니다!",discord.Color.green()))
    except:
        await ctx.reply(embed=embed("로드 실패 <a:no:977162736502976513>","모듈 이름을 다시 확인 해 주세요"))
      
# Keep alive 서버 on
keep_alive()
# 토큰 이용 봇 구동
# token: 정식버전
# token-beta: 배타버전
# 수정: 옆의 자물쇠 클릭. .env임
bot.run(os.getenv("token-beta"))