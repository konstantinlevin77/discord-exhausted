from discord.ext import commands,tasks
import nest_asyncio
import time
import discord
from translate_command import translate,langcode
from general_commands import list,help,source,invite
from lyrics_command import lyrics
from whatis_command import whatis
from gif_command import gif
from remind_command import remind
import pickle
import nltk

nest_asyncio.apply()

nltk.download("punkt")

bot = commands.Bot(command_prefix=";",help_command=None)

@bot.command()
async def test(ctx):
    await ctx.send("Hello world!")
    

@bot.event 
async def on_ready(*args):
    await bot.change_presence(activity=discord.Game(name="| ;help for help"))
    

@tasks.loop(seconds=2)
async def checkRemind():
    try:
        with open("remindlist.pkl","rb") as F:
            user2remind = pickle.load(F)
        for userId,(entryTime,waitTime) in user2remind.items():
            
            if time.time()-entryTime > waitTime:
                user2remind = {key:value for key,value in user2remind.items() if key!=userId and value!=(entryTime,waitTime)}
                pickle.dump(user2remind,open("remindlist.pkl","wb"))
                user = await bot.get_user(int(userId)).create_dm()
               
                await user.send("You've wanted me to remind you!")
    except Exception as E:
        print(E)
            
  
checkRemind.start()

bot.add_command(translate)
bot.add_command(langcode)
bot.add_command(list)
bot.add_command(lyrics)
bot.add_command(whatis)
bot.add_command(help)
bot.add_command(gif)
bot.add_command(remind)
bot.add_command(source)
bot.add_command(invite)

print("Exhausted started to work")


bot.run("YOUR BOT TOKEN HERE")
