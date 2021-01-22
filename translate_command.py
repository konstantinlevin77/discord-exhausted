import googletrans
from discord.ext import commands
import discord

color = 0x00FF7F

@commands.command()
async def translate(ctx,src,dest,*args):
    translator = googletrans.Translator()
    
    
    if src.strip() in googletrans.LANGUAGES.keys() and dest.strip() in googletrans.LANGUAGES.keys():
        result = translator.translate(" ".join(list(args)),dest,src).text
        source,dest = googletrans.LANGUAGES[src],googletrans.LANGUAGES[dest]
        
        
        await ctx.send(embed=discord.Embed(title=f"Translated from {source} to {dest}",description=result,color=0x00FF7F))
    
    else:
        description="""You have typed an invalid source or destination language
        please make sure that you use language codes, you can learn code of a language using **langcode** command """
        await ctx.send(embed=discord.Embed(title="Invalid Source or Destination",description=description,color=0x00FF7F))
        

@commands.command()
async def langcode(ctx,lang):
    
    if lang in googletrans.LANGCODES.keys():
    
        langcode = googletrans.LANGCODES[lang.lower()]
        message = f"Language code of **{lang}** is **{langcode}**"
        title = f"**{lang}**=>**{langcode}**"
        
        await ctx.send(embed=discord.Embed(title=title,description=message,color=color))
    
    else:
        desc = f"Language {lang} is not in Google Translate APIs Supported Language list, please try an another language"
        await ctx.send(embed=discord.Embed(title="Invalid Language",description=desc,color=color))
    
    
    
    
    
