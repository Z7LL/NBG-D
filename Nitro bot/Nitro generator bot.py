from itertools import count
from multiprocessing.connection import Client
import string
import random
import discord
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('we have logged in as {0.user}' . format(client))
 
 
Key_Len = 24
 
 
Link = 'https://discord.gift/'
 
Generator = (string.ascii_letters + string.digits)#This is generator's base
Generator1 = [random.choice(Generator)for i in range(Key_Len)]
Generator2 = (''.join(Generator1))
  

print(Generator2)
 
@client.event
async def on_message(message):
   if message.content.startswith('$'): 
     await message.channel.send(Link + Generator2)

print

@client.event
async def on_message(message):
   if message.content.startswith('$'): 
     count = 0
     while count < 1:
         await message.channel.send(Link + Generator2)






client.run('BOT-TOKEN-HERE')

                                            
                                            
#  $$$$$$\  $$$$$$$\  $$\  $$$$$$\  $$\   $$\   
# $$  __$$\ $$  __$$\ \__|$$  __$$\ $$ |  $$ |
# $$$$$$$$ |$$ |  $$ |$$\ $$ /  $$ |$$ |  $$ |
# $$   ____|$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |
# \$$$$$$$\ $$ |  $$ |$$ |\$$$$$$  |\$$$$$$$ |
#  \_______|\__|  \__|$$ | \______/  \____$$ |
#               $$\   $$ |          $$\   $$ |
#               \$$$$$$  |          \$$$$$$  |
#                \______/            \______/ 

#$$$$$$$\ $$\     $$\       $$$$$$$$\ $$$$$$$$\ $$\       $$\       
#$$  __$$\\$$\   $$  |      \____$$  |\____$$  |$$ |      $$ |      
#$$ |  $$ |\$$\ $$  /           $$  /     $$  / $$ |      $$ |      
#$$$$$$$\ | \$$$$  /           $$  /     $$  /  $$ |      $$ |      
#$$  __$$\   \$$  /           $$  /     $$  /   $$ |      $$ |      
#$$ |  $$ |   $$ |           $$  /     $$  /    $$ |      $$ |      
#$$$$$$$  |   $$ |          $$$$$$$$\ $$  /     $$$$$$$$\ $$$$$$$$\ 
#\_______/    \__|          \________|\__/      \________|\________|
                                                                   
                                                                   
                                                                   