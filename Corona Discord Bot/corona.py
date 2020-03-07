#!/usr/bin/env python3
from discord.ext import commands
import requests
import discord

import json
import requests
from time import sleep
getCountry = ("https://corona.lmao.ninja/countries/")
getAll = ("https://corona.lmao.ninja/all/")

req = requests.get(getCountry)
intxt = req.text
data = req.json()

allreq = requests.get(getAll)
data2 = allreq.json()

token =('Token')
bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
        print ('Logged in as {}         {}'.format(bot.user.name, bot.user.id))


@bot.command()
async def h(ctx):
        await ctx.send("`?corona <country name with first letter Capital\neg.Nepal, USA, India, China`")


@bot.command()
async def corona(ctx, arg):
        if arg == "All":
                await ctx.send("`Total Case: {}\nTotal Deaths: {}\nTotal Recovered: {}`".format(data2["cases"],data2["deaths"],data2["recovered"]))
                print ("all")
        else:
                pass
        for i in data:
                if i['country'] == arg:
                        print (arg)
                        await ctx.send("`Country: {}\nCase: {}\nToday's Case:{}\nToday's Death: {}\nDeaths:{}\nRecovered: {}\nCritical: {}`".format(i["country"],i["cases"],i['todayCases'],i["todayDeaths"],i["deaths"],i["recovered"],i["critical"]))
bot.run(token)
