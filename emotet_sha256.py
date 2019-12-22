#!/usr/bin/env python3
from discord.ext import commands
import requests
import discord

token =(' xxxxxxxxxxxxx TOKEN xxxxxxxxxxxxxxxxxxxxxxx')
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
                        await ctx.send(":warning: Hash matched with Emotet!")
bot.run(token)




