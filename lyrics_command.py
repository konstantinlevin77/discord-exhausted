from discord.ext import commands
import discord
from lyricsgenius import Genius


color = 0x00FF7F

genius = Genius("YOUR API KEY HERE")

@commands.command()
async def lyrics(ctx,*args):
    
    songName = " ".join(args)
    
    try:
        result = genius.search_song(songName).lyrics
    
    except:
        await ctx.send(embed=discord.Embed(title="Oops.",description="Something went wrong with Genius API, please try again",color=color))
    
    songName = " ".join([word.capitalize() for word in songName.split()])
    
    if len(result)<2000:
        await ctx.send(embed=discord.Embed(title=f"Lyrics of {songName}",description=result,color=color))
        
    else:
        sentences = result.split("\n")
        midIndex = len(sentences)//2
        await ctx.send(embed=discord.Embed(title=f"Lyrics of {songName}",description="\n".join(sentences[:midIndex]),color=color))
        await ctx.send(embed=discord.Embed(description="\n".join(sentences[midIndex:]),color=color))
        
    
    
