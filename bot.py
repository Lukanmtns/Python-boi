# Python-Boy by Lukanmtns

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='.')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Im ready!!")
    print ("i am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong boi!")
    print ("User has pinged")

@bot.command(pass_context=True)
async def boi(ctx):
    await bot.say("Im 'bout to roast you as hard as i roast my steaks!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The users name is: {}".format(user.name))
    await bot.say("The users ID is: {}".format(user.id))
    await bot.say("The users status is: {}".format(user.status))
    await bot.say("The users highest role is: {}".format(user.top_role))
    await bot.say("The user joined at: {}".format(user.joined_at))

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="My name jeff", color=0x00ff00)
    embed.set_footer(text="This is my foot boi!")
    embed.set_author(name="Luka")
    embed.add_field(name="DIs a field!", value="no it aint boi!", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def pingg(ctx):
    resp = await bot.say('Pong! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await bot.edit_message(resp, f'Pong! That took {1000*diff.total_seconds():.1f}ms.')

bot.run("NDQyNDY5NjY3OTkxMTkxNTU0.Dc_Rgg._Anq4ng-ZgDNTvkE4qhF3PVbB2Y")
