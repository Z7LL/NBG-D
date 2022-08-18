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

import time
print('-------------------------------------------------------------------')
print('  $$$$$$\  $$$$$$$\  $$\  $$$$$$\  $$\   $$\ ')  
print('$$  __$$\ $$  __$$\ \__|$$  __$$\ $$ |  $$ |')
print('$$$$$$$$ |$$ |  $$ |$$\ $$ /  $$ |$$ |  $$ |')
print('$$   ____|$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |')
print('\$$$$$$$\ $$ |  $$ |$$ |\$$$$$$  |\$$$$$$$ |')
print(' \_______|\__|  \__|$$ | \______/  \____$$ |')
print('               $$\   $$ |          $$\   $$ |')
print('               \$$$$$$  |          \$$$$$$  |')
print('                \______/            \______/ ')

print('$$$$$$$\ $$\     $$\       $$$$$$$$\ $$$$$$$$\ $$\       $$\       ')
print('$$  __$$\\$$\   $$  |      \____$$  |\____$$  |$$ |      $$ |      ')
print('$$ |  $$ |\$$\ $$  /           $$  /     $$  / $$ |      $$ |      ')
print('$$$$$$$\ | \$$$$  /           $$  /     $$  /  $$ |      $$ |      ')
print('$$  __$$\   \$$  /           $$  /     $$  /   $$ |      $$ |      ')
print('$$ |  $$ |   $$ |           $$  /     $$  /    $$ |      $$ |      ')
print('$$$$$$$  |   $$ |          $$$$$$$$\ $$  /     $$$$$$$$\ $$$$$$$$\ ')
print('\_______/    \__|          \________|\__/      \________|\________|')
print('-------------------------------------------------------------------')
print('Discord Z7LL#9999                                             exit.')
import os
import webbrowser
name = input ('What is your name? ') 
print("welcome "+name)
Discord = input('Do you want to join my discord server?N/Later/Y :')

if Discord == 'Y':
  webbrowser.open('https://dsc.gg/Z7LL')

if Discord == ('Later'):
 Token = input('Token: ')
 print("For Support Join my Discord "+name)
 print('Loading.')
 time.sleep(1)
 print('Loading..')
 time.sleep(2)
 print('Loading...')
 time.sleep(5)  
 print ('Feel free for Runnig the Programe in the Background')
 time.sleep(1)
 print ('Runing.....')
 time.sleep(2) 
 print ('Runing....')
 time.sleep(2)
 print ('Runing...')
 time.sleep(2)
 print ('Runing..')
 time.sleep(1)
 print ('Runing.')
 time.sleep(5)
 print('ヾ(⌐■_■)ノ♪')
 client.run (Token)


if Discord == 'N':
  print('  8888888888 888     888  .d8888b.  888    d8P        .d88888b.  8888888888 8888888888')
  print('888        888     888 d88P  Y88b 888   d8P        d88P" "Y88b 888        888         ')
  print('888        888     888 888    888 888  d8P         888     888 888        888         ')
  print('8888888    888     888 888        888d88K          888     888 8888888    8888888    ')
  print('888        888     888 888        8888888b         888     888 888        888        ')
  print('888        888     888 888    888 888  Y88b        888     888 888        888        ')
  print('888        Y88b. .d88P Y88b  d88P 888   Y88b       Y88b. .d88P 888        888        ')
  print('888         "Y88888P"   "Y8888P"  888    Y88b       "Y88888P"  888        888        ')                                                                                    
  time.sleep(3)
  os.system("taskkill /f /im NGB-D.exe")
 

Token = input('Token: ')
print("For Support Join my Discord "+name)
print('Loading.')
time.sleep(1)
print('Loading..')
time.sleep(2)
print('Loading...')
time.sleep(5)  
print ('Feel free for Runnig the Programe in the Background')
time.sleep(1)
print ('Runing.....')
time.sleep(2) 
print ('Runing....')
time.sleep(2)
print ('Runing...')
time.sleep(2)
print ('Runing..')
time.sleep(1)
print ('Runing.')
time.sleep(5)
print('ヾ(⌐■_■)ノ♪')
client.run (Token)                                                            
                                                                   