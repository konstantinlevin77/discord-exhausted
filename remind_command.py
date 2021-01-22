from discord.ext import commands
import discord
import time
import pickle

color = 0x00FF7F


@commands.command()
async def remind(ctx,num,dateType):
    
    remindList = pickle.load(open("remindlist.pkl","rb"))
    
    if dateType.lower() == "days":
        waitSeconds = 86400
    
    elif dateType.lower() == "hours":
        waitSeconds = 3600
    
    elif dateType.lower() == "minutes":
        waitSeconds = 60
        
    elif dateType.lower() == "seconds":
        waitSeconds = 1
    
    else:
        desc = f"You've typed **{dateType.lower()}** as time keyword. However for now you are be able to use **seconds**,**minutes**,**hours** and **days**"
        await ctx.send(embed=discord.Embed(title="Invalid Keyword",description=desc,color=color))
        return 
    
    try:
        num = int(num)
        totalWait = waitSeconds * num
    except:
        # TODO: Invalid Number
        desc = f"You've typed {num} as number, please try an integer such as 4"
        await ctx.send(embed=discord.Embed(title="Invalid Number",description=desc,color=color))
        return
    
    try:
        remindList[ctx.message.author.id] = [time.time(),totalWait]
        with open("remindlist.pkl","wb") as F:
            pickle.dump(remindList,F)          
            
        print(remindList)
        await ctx.send(embed=discord.Embed(title="Of Course!",description="I'll remind you!",color=color))
        
    except:
        dec = """Because of the File I/O of Python I couldn't save your remind demand, please try again."""
        await ctx.send(embed=discord.Embed(title="Please Try Again",description=dec,color=color))
    
    
        
    
    