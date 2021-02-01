import random
import discord

from discord.ext import commands
prefix = "/"
bot = commands.Bot(command_prefix=prefix)
token = 'ODAxMDkxMTc1ODg0NTIxNDgw.YAboSw.UtBY5bCs93-Cn2VrFJOB4LKGQas'
@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command(pass_context = True)
async def roll(ctx):
    embed = discord.Embed(title = "Random Number", description = (random.randint(1,101)), color = (0xF85252))
    await ctx.send(embed = embed)



bot.run("ODAxMDkxMTc1ODg0NTIxNDgw.YAboSw.UtBY5bCs93-Cn2VrFJOB4LKGQas")