from discord.ext import commands
import discord
import requests
import json
import random
color = 0x00FF7F

apikey = "YOUR API KEY HERE"
@commands.command()
async def gif(ctx,*args):
    
    keywords = " ".join(args)
    lmt = 20

    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (keywords, apikey, lmt))
    
    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        links = []
        for result in top_8gifs["results"]:
            links.append(result["url"])
        link = random.choice(links)
        await ctx.send(link)
        
    else:
        await ctx.send(embed=discord.Embed(title="Something Went Wrong",description="Something went wrong with Tenor API, please try with similar keywords again.",color=color))
    

