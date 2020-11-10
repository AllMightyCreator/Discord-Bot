import discord
from discord.ext import commands

client = commands.Bot(command_prefix="Cr")

@client.event
async def on_ready():
    print("Bot Is Ready")
    
@client.command()
async def hello(ctx):
    await ctx,send("Hi!")

client.run("YourBotToken")
