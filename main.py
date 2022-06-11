import discord
from discord.ext import commands
import os
import keep_alive


#Importing bot token and prefix

token = os.environ.get("token")
prefix = os.environ.get("prefix")



bot = commands.Bot(command_prefix=f"{prefix}")

#Start Event for Bot
@bot.event
async def on_ready():
    print("Bot Online[\]")




#Basic ping command
@bot.command()
async def ping(ctx):
    embed = discord.Embed(
        title = "Pong!",
        colour = discord.Colour.blue()
    )
    await ctx.send(embed=embed)



keep_alive.keep_alive()
bot.run(token)