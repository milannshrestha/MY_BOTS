#!/usr/bin/python
from discord.ext import commands

import random

import discord
import feedparser
from time import sleep
from discord_webhook import DiscordWebhook

token =('token')
bot = commands.Bot(command_prefix='?')

parse = feedparser.parse('https://www.reddit.com/r/Nepal.rss')
rss_list = []

@bot.event
async def on_ready():
        print ('Logged in as')
        print (bot.user.name)
        print (bot.user.id)
        print ('------')


@bot.command()
async def guns(ctx):
        for post in parse.entries:
                xx = (post.link)
                put_list = rss_list.append(xx)
                val = random.choice(rss_list)
        await ctx.send(val)

bot.run(token)
