# Lithe github edition
# Lithe developer edition
# Lithe open source edition

# IMPORTS
import time
import discord #For the discord bot to... y'know, run? (look up discord.py)
from discord.ext import commands #discord bot commands
from colorama import Fore, Back, Style

# SETTINGS
bot_prefix = ''  # prefix you call your bot with
bot_token = '' # bots token from application page
bot_stream_link = '' # bot "playing" twitch link (ex.https://www.twitch.tv/lithethebot)
owner_ID = '' # ID of the user the bot owns

# SETTING ERRORS
if ' ' in bot_token or bot_token == '':
    print(Back.RED + "ERROR" + Back.RESET + ' INVALID TOKEN Please enter your discord bot TOKEN after' + Fore.CYAN + ' bot_token =  ')
    print(Back.BLUE + "INFO" + Back.RESET + ' Due to an error the program will close in' + Fore.CYAN + ' 5 ' + Fore.RESET + 'seconds')
    time.sleep(5)
    exit()
if ' ' in owner_ID or owner_ID == '':
    print(Back.RED + "ERROR" + Back.RESET + ' Please enter your discord user account ID after' + Fore.CYAN + ' owner_ID =  ')
    exit()
if ' ' in bot_stream_link or bot_stream_link == '':
    print(Back.RED + "ERROR" + Back.RESET + ' Please enter a valid twitch link' + Fore.CYAN + ' bot_stream_link =  ')
    exit()
if ' ' in bot_prefix or bot_prefix == '':
    print(Back.RED + "ERROR" + Back.RESET + ' Please enter the bot prefix' + Fore.CYAN + ' bot_prefix =  ')
    exit()


bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready():
    print(Back.BLUE + "VERSION:" + Back.RESET + " Lithe " + Fore.CYAN +" Developer Edition 1.0")
    print(Fore.RESET + Back.BLUE + "USER:" + Back.RESET + " lithe " + Fore.CYAN + bot.user.name + Fore.RESET +" edition")
    print(Back.BLUE + "BOT ID:" + Back.RESET + " " + bot.user.id)
    print(Back.BLUE + "OWNER ID:" + Back.RESET + " " + owner_ID)
    print(Back.MAGENTA + "TWITCH:" + Back.RESET + " " + bot_stream_link)
    await bot.change_presence(game=discord.Game(name="lithe: " + bot.user.name + " edition", url="https://www.twitch.tv/dithskii", type=1))







bot.run(bot_token)
