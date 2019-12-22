#!/usr/bin/env python3
from discord.ext import commands
import requests
import discord

token =('xxxxxxxxxxxxxxxxxx TOKEN xxxxxxxxxxxxxxxxxxxxxxxx')
bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
        print ('Logged in as')
        print (bot.user.name)
        print (bot.user.id)
        print ('------')

emotet = requests.get('https://raw.githubusercontent.com/milannshrestha/IoC-hunts/master/emotet.txt')
intxt = emotet.text
string = str(intxt)
put_list = string.split()

@bot.command()
async def hash(ctx, arg):
        print ('[*] Serevr User Enterd: {}'.format(arg))
        for j in put_list:
                if arg == j:
                        embed = discord.Embed(title="I found Emotet", color=0xeee657)
                        embed.add_field(name = "Lookup?", value = "https://www.virustotal.com/gui/file/{}/detection".format(arg))
                        await ctx.send(embed = embed)
                else:
                        continue
bot.run(token)






