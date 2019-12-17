import discord
from discord.ext import commands
import os
import time

import shutil
import datetime

bot = commands.Bot(command_prefix="dontchangethisxxx1x")
client = discord.Client()
'''
def linePrint():
	lines = open('dfh.txt').read()
	return lines
'''


@client.event
async def on_ready():
	total, used, free = shutil.disk_usage('/')
	print('[*] Bot Script is Logged in now ')
	used1 = (used /(2**30))
	total1 = round((total/(2**30)), 2)
	per = ((used1/total1)*100)
	a = round(per, 2)
	print ('percent {}%'.format(a))

	x = 69
#	while x < 70:
	if per < 70:
		now = datetime.datetime.now()
		heredate =  ("[+] Alert pushed at:" + now.strftime("%Y-%m-%d %H:%M:%S"))
		#print (heredate)
		channel = client.get_channel(646700252690251808)
		await channel.send("```"+ heredate+'\n'+ 'Disk Storage Used Maximum.\nDisk Usage: {}%\nTotal Disk Size: {}GB'.format(a, total1)+"```")
		print (heredate)
#		time.sleep(13)


client.run('NjQ2NDE')


