#載入Discord 模組
import discord
from discord.ext import commands
#載入json模組
import json
#載入ranom(隨機)模組
import random
#載入setting.json檔案
#請於同格資料夾內新增setting.json
#建立資料
#{
#    "TOKEN":"your token",
#   "pic": ["圖片位置"],
#    "txt": ["泡麵","牛排","便當","小七","水餃","不要吃"]
#}
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)
bot = commands.Bot(command_prefix=">")
#bot上線顯示
@bot.event
async def on_ready():
    print(">>bot is online")
#抽圖片
#圖片位置放置於 setting pic類別
@bot.command()
async def 抽(ctx):
    random_pic = random.choice(jdata['pic'])
    pic = discord.File(random_pic)
    await ctx.send(file=pic)
#抽隨機字串
#隨機字串放置於 setting txt類別
@bot.command()   
async def 抽晚餐(ctx):
    random_txt = random.choice(jdata['txt'])
    #pic = discord.File(random_pic)
    await ctx.send(random_txt)

bot.run(jdata['TOKEN'])
