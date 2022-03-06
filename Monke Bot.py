import discord
from discord.ext import commands
from googleapiclient.discovery import build
from discord.ext import tasks
import asyncio
import random
import json
import logging
import datetime
from discord.ext import commands


client = commands.Bot(command_prefix="$")
api_key = "AIzaSyCNfFzO5VbduOrYOts-LzmgBjvk-Qy51zU"


@client.event
async def on_message(message):
    if message.channel.name == '🐵daily-monke':
        await client.process_commands(message)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="I give bananas🍌"))
    await client.change_presence(activity=discord.Streaming(name="I show my Monke Brothas🙈"))
    print("Ready")


async def ch_pr():
    await client.wait_until_ready()

    statuses = [
        "🍌I give bananas🍌", "🙈I show my Monke Brothas🙈", "🛢️Not Funny Didn't Laugh🛢️"]
    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(5)
client.loop.create_task(ch_pr())


@client.event
async def on_ready():
    print("!!! Bot Is Online !!!\n")


@client.command(pass_context=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
        messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send(f'{amount} messages have been purged by {ctx.message.author.mention}')


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="4ce75ef60702b03fc", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)

    client.run("ODc1OTU0ODYyMzg5NjI0ODQy.YRdCiQ.KDrRcUgeYDZ6lEaZ5xAC-Bq7F_c")
