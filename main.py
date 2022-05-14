import discord
from discord.ext import commands
import random
import asyncio
import os
import json
from keep_alive import keep_alive
def write(file, tup):
    with open(f"{file}.json", "w+", encoding='utf-8-sig') as f:
        json_string = json.dump(tup, f, indent=2, ensure_ascii=False)
jstring = open("prefixes.json", "r", encoding='utf-8-sig').read()
prefixList = json.loads(jstring)
async def prefix(bot, message):
    return prefixList.get(str(message.author.id), ",")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix,intents=intents)
def randomcolor():
    return random.randint(0x000000,0xffffff)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Gaming("헬월이 1.0.0 - $"))
    print(f'{bot.user.name} 준비 끝!')
@bot.command(name="prefix")
async def _prefix(ctx, new_prefix):
    prefixList[str(ctx.author.id)] = new_prefix
    write('prefixes',prefixList)
    await ctx.send(embed=discord.Embed(title='완료!',description=f"프리픽스가 {new_prefix}로 설정되었습니다!",color=discord.Color.green()))
                   
bot.run(os.getenv("token"))