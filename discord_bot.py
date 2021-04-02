import discord
from discord.ext import commands
import time
import datetime

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    print("Készen vagyok, mehetünk!")

token = 'ODI3NTA2MzA3OTU0MjQ1Njgy.YGcBTg.VfgUQGDPwoaEXWfrOxDuGLjQCZk'

@client.event
async def on_member_join(member):
    embed = discord.Embed(colour=0x95efcc, description=f"Üdv a szerveren! Te vagy a {len(list(member.guild.members))}. tag!",
                          )

    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp = datetime.datetime.utcnow()

    channel = client.get_channel(825078557436280832)

    await channel.send(embed=embed)



@client.command()
async def ping(ctx):
    await ctx.send(f'PONG! Amúgy ekkora a késésem: {round(client.latency * 1000)}ms')

@client.command()
async def pong(ctx):
    await ctx.send('Ez visszafele nem működik, hehe!')


@client.command()
async def takarítás(ctx, amount=5):
    await ctx.channel.purge(limit=amount)





client.run(token)