import discord
from discord.ext import commands
import os
import asyncio
import random
import qrcode
from PIL import Image
import requests
import time


# 임배드 함수
def embed(title, description, color=random.randint(0x000000, 0xFFFFFF)):
    return discord.Embed(title=title, description=description, color=color)


class Convenience(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qrcode(self, ctx, *, link):
        img = qrcode.make(link)
        img.save("qrcode.png")
        name = "qrcode.png"
        await ctx.reply(file=discord.File(name))

    # 링크 단축
    @commands.command()
    async def 링크단축(self, ctx, link):
        msg = await ctx.reply('링크 단축하는중...')
        await asyncio.sleep(5)
        await msg.delete()
        target = link
        client_id = os.getenv("client_id")
        client_secret = os.getenv("client_secret")
        header = {
            'X-Naver-Client-Id': client_id,
            'X-Naver-Client-Secret': client_secret
        }
        naver = 'https://openapi.naver.com/v1/util/shorturl'
        data = {'url': target}
        maker = requests.post(url=naver, data=data, headers=header)
        maker.close()
        output = maker.json()['result']['url']
        embed = discord.Embed(title="URL 단축기능",
                              color=random.randint(0x000000, 0xFFFFFF))
        embed.add_field(name="단축 링크", value=f'{output}', inline=False)
        embed.set_footer(text=f"{ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.reply(embed=embed)

def setup(bot):
    bot.add_cog(Convenience(bot))
