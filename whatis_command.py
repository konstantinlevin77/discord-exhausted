import wikipedia
from discord.ext import commands
import discord
import nltk



color = 0x00FF7F

@commands.command()
async def whatis(ctx,lang,*args):
    
    searchText = " ".join(args).lower()
    
    try:
        wikipedia.set_lang(lang)
        summary = wikipedia.summary(searchText)
        
    except:
        desc = """Something went wrong, please check the language and the title that you typed, you can learn supported languages from the official website of Wikipedia"""
        await ctx.send(embed=discord.Embed(title="Something Went Wrong :/",description=desc,color=color))
        return
    

    sentenceCount = len(nltk.sent_tokenize(summary))
    while len(summary) > 2000:   
    
        summary = nltk.sent_tokenize(summary)
        sentenceCount = sentenceCount - 1 
        summary = summary[:sentenceCount]
        summary = " ".join(summary)
    
    
    
    await ctx.send(embed=discord.Embed(title=f"Wikipedia Summary | {searchText}",description=summary,color=color))
    
    
    

        
        