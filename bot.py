import discord
from discord.ext import commands
import json
import random
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
bot = commands.Bot(command_prefix=">")

@bot.event
async def on_ready():
    print(">>bot is online")
@bot.command()
async def 抽(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)

bot.run(jdata['TOKEN'])
