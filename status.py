#!/usr/bin/env python3

import requests
import discord

token = ('XXXXXXXX BOT TOKEN XXXXXXXXXXX')

c1 = ('https://X.X.X.X:YYY/')

class MyClient(discord.Client):
        async def on_ready(self):
                print('Logged in as')
                print(self.user.name)
                print(self.user.id)
                print('------')

        async def on_message(self, message):
#        we do not want the bot to reply to itself
#               if message.author.id == self.user.id:
#                       return

                if message.content.startswith('!CLIENT'):
                        check  = requests.get(c1, verify = False)
                        status = check.status_code
                        if status == 200:
                                await message.channel.send('Hello {0.author.mention}, the server is UP :flushed:.'.format(message))
                        elif status != 200:
                                await message.channel.send('Hello {0.author.mention}, the server is DOWN. :100: '.format(message))

client = MyClient()
client.run(token)
