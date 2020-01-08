#!/usr/bin/env python3

from discord.ext import commands
import discord

import re
import requests
from time import sleep

#regex = (r"[A-Fa-f0-9]{64}")
url = requests.get('https://raw.githubusercontent.com/milannshrestha/IoC-hunts/master/all.txt')
intxt = url.text
string = str(intxt)
put_list = string.split()

r = re.compile("[A-Fa-f0-9]{64}")

emlist = []

newlist = list(filter(r.match, put_list)) # Read Note
for i in newlist:
        print ("SHA256: ",i)
        emlist.append(i)
#        sleep(0.01)


token = ('token')

bot = commands.Bot(command_prefix = '?')


@bot.event
async def on_ready():
        print ('Logged in as')
        print (bot.user.name)
        print (bot.user.id)
        print ('------')


@bot.command()
async def hash(ctx, arg):
        print ('[*] Serevr User Enterd: {}'.format(arg))
        for j in emlist:
                if arg == j:
                        embed = discord.Embed(title="I found Emotet", color=0xeee657)
                        embed.add_field(name = "Lookup?", value = "https://www.virustotal.com/gui/file/{}/detection".format(arg))
                        await ctx.send(embed = embed)
                else:
                        continue
bot.run(token)

