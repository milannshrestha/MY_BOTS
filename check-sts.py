#!/usr/bin/env python3

import requests
import discord

token =('xxxxxxxxxxxxxx.xxxxxxxxx.XXXXXXXXXX')

client1 = ('URL1')
client2 = ('URL2')

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

                if message.content.startswith('!client1'):
                        check  = requests.get(client1)
                        status = check.status_code
                        if status != 200:
                                await message.channel.send('Hello {0.author.mention}, the server is DOWN :flushed:.'.format(message))
                        else:
                                await message.channel.send('Hello {0.author.mention}, the server is UP. :100: '.format(message))


                elif message.content.startswith('!client2'):
                        check  = requests.get(client2)
                        status = check.status_code
                        if status != 200:
                                await message.channel.send('Hello {0.author.mention}, the server is DOWN :flushed:.'.format(message))
                        else:
                                await message.channel.send('Hello {0.author.mention}, the server is UP. :100: '.format(message))

client = MyClient()
client.run(token)
