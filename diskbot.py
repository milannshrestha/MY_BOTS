#!/usr/bin/env python3

import discord
from pexpect import pxssh

token = ('XXXXXXXX BOT TOKEN XXXXXXXXXXXXXX')
server = 'Server IP'
username = 'username'
password = 'pass'

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')

	async def on_message(self, message):
		if message.content.startswith('!disk'):
			try:
				s = pxssh.pxssh()
				s.login(server, username, password)
				s.sendline('df -h ')   # run a command
				s.prompt()
				byte = s.before
				decode = byte.decode("utf-8")
				await message.channel.send('```{} :flushed:.```'.format(decode))

			except pxssh.ExceptionPxssh as e:
        	                await message.channel.send('Hello {0.author.mention}, Server is refusing SSH :100:.'.format(message))

client = MyClient()
client.run(token)
