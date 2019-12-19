
#!/usr/bin/env python3

import discord
from discord.ext import commands
import os
import time

import shutil
import datetime

import requests
import discord
from pexpect import pxssh

token = ('xxxxxxxx token xxxxxxxxxxxxxxx')
server = 'server ip'
username = 'username'
password = 'password'

class MyClient(discord.Client):
	print ('im here 1')
	async def on_ready(self):
		print ('im here 2')
		total, used, free = shutil.disk_usage('/')
		print('[*] Bot Script is Logged in now ')
		used1 = (used /(2**30))
		total1 = round((total/(2**30)), 2)
		per = ((used1/total1)*100)
		a = round(per, 2)
		print ('percent {}%'.format(a))

		x = 69
#		while x < 70:
		if per < 70:
			now = datetime.datetime.now()
			heredate =  ("[+] Alert pushed at:" + now.strftime("%Y-%m-%d %H:%M:%S"))
			#print (heredate)
			channel = client.get_channel(xxxchannel idxxx)
			await channel.send("@everyone \n" +"```"+ heredate+'\n'+ 'Disk Storage Used Maximum.\nDisk Usage: {}%\nTotal Disk Size: {}GB'.format(a, total1)+"```")
			print (heredate)
		#time.sleep(13)

	#async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def on_message(self, message):
		if message.content.startswith('!disk'):
			try:
				s = pxssh.pxssh()
				s.login(server, username, password)
				s.sendline('df -h')   # run a command
				s.prompt()
				byte = s.before
				decode = byte.decode("utf-8")
				await message.channel.send('```Command: {}```'.format(decode))

			except pxssh.ExceptionPxssh as e:
        	                await message.channel.send('Hello {0.author.mention}, Server is refusing SSH :100:.'.format(message))

client = MyClient()
client.run(token)

