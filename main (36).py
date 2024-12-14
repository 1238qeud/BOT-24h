import discord
from discord.ext import commands
import keep_alive
import os

intents = discord.Intents.default()
intents.members = True  # Enable the 'members' intent to access member information

bot = commands.Bot(command_prefix='!', intents=intents, self_bot=True, help_command=None)

ICE_SHOP1 = 1268863392341299230 # ไอดี เซิฟเวอร์ดิสคอส
#---------------------------------------------------------------------------
ICE_SHOP2 = 1269653338782437488# ไอดี ห้องที่จะให้บอทลง
#---------------------------------------------------------------------------
@bot.event
async def on_ready():#---------------------------------------------------------------------------
    await bot.change_presence(activity=discord.Streaming(
    name="OPI SHOP", url="https://www.twitch.tv/Zxaicas_ice"))#---------------------------------------------------------------------------
    vc = discord.utils.get(bot.get_guild(ICE_SHOP1).channels, id=ICE_SHOP2)
    await vc.guild.change_voice_state(channel=vc,#---------------------------------------------------------------------------
                                      self_mute=False,
                                      self_deaf=True)
    print('''    
  ██ ▄████▄ ▓█████      ██████   ██░ ██  ▒█████   ██▓███  
▒▓██▒██▀ ▀█ ▓█   ▀    ▒██    ▒ ▒▓██░ ██ ▒██▒  ██▒▓██░  ██ 
░▒██▒▓█    ▄▒███      ░ ▓██▄   ░▒██▀▀██ ▒██░  ██▒▓██░ ██▓▒
 ░██▒▓▓▄ ▄██▒▓█  ▄      ▒   ██▒ ░▓█ ░██ ▒██   ██░▒██▄█▓▒ ▒
 ░██▒ ▓███▀ ░▒████    ▒██████▒▒ ░▓█▒░██▓░ ████▓▒░▒██▒ ░  ░
 ░▓ ░ ░▒ ▒  ░░ ▒░     ▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░ ▒░▒░▒░ ▒▓▒░ ░  ░
  ▒   ░  ▒   ░ ░      ░ ░▒  ░    ▒ ░▒░ ░  ░ ▒ ▒░ ░▒ ░     
  ▒ ░          ░      ░  ░  ░    ░  ░░ ░░ ░ ░ ▒  ░░       
  ░ ░ ░        ░            ░    ░  ░  ░    ░ ░           
''')

#---------------------------------------------------------------------------
keep_alive.keep_alive() #---------------------------------------------------------------------------
token = os.getenv("TOKEN")
if token is None:
    print("Error: Discord bot token not found. Please set the 'TOKEN' environment variable.")
    exit(1)  # Or handle the error in a different way
