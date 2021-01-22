from discord.ext import commands
import discord
color = 0x00FF7F

@commands.command()
async def list(ctx):
    
    desc = open("help.txt","r").read()
    title = "Command List of **Exhausted**"
    
    await ctx.send(embed=discord.Embed(title=title,description=desc,color=color))

@commands.command()
async def help(ctx):
    emb = """Hey, I am **Exhausted**, nice to meet you. I am a lightweight micro discord bot, you can send gifs using keywords, learn lyrics of a song or learn something from wikipedia. Just type **;list** to see all the commands and their usage.\n And if you encounter with a problem, please dm to \n@konstantinlevin#8630"""
    await ctx.send(embed=discord.Embed(title="Hi!",description=emb,color=color))
    

@commands.command()
async def invite(ctx):
    emb = "Here is the invite link, thanks for your attention!\n[Click to invite!](https://discord.com/api/oauth2/authorize?client_id=801477829790662696&permissions=8&scope=bot)"
    await ctx.send(embed=discord.Embed(title="Invite Link for Exhausted",description=emb,color=color))
    

@commands.command()
async def source(ctx):
    emb = "Nice to see that you liked my bot, you can display and download the source code of **Exhausted** from the link below:\n[Github Source Code](https://github.com/lauda33/discord-exhausted)"
    await ctx.send(embed=discord.Embed(title="Source Code Link of Exhausted",description=emb,color=color))