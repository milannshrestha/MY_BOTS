#!/usr/bin/env python3
from discord.ext import commands
import requests
import discord

token =('xxxxxxxxxxxxxxxx TOKEN xxxxxxxxxxxxxxxxxxxx')
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
        print ('Logged in as')
        print (bot.user.name)
        print (bot.user.id)
        print ('------')

@bot.command()
async def hello(ctx, arg):
        print ('[*] Serevr User Enterd: {}'.format(arg))
        await ctx.send("U entered {}".format(arg))

bot.run(token)
