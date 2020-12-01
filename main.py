import discord
import os
import random
from time import sleep
from clear import clear
from make_website import make_website
from commands import alwayscommands
from commands import eventcommands

client = discord.Client()


@client.event
async def on_ready():
    clear()
    sleep(1)
    print("I'm online")
    sleep(1)
    print(f"username: {client.user}")
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name="you"))

person = 1

channel = 1

server = 1

times_used = 0
@client.event
async def on_message(message):
  
    if message.content == "color":
      global times_used
      await message.channel.send(f"Whats your favorite color?")

    # This will make sure that the response will only be registered if the following
    # conditions are met:
      def check(msg):
        return msg.author == message.author and msg.channel == message.channel and \
        msg.content.lower() in ["red", "orange", "yellow", "green", "teal", "blue", "purple", "magenta", "pink"]

      msg = await client.wait_for("message", check=check)
      await message.channel.send("Awesome!")

      times_used = times_used + 1

    
    prankrand = random.randint(1, 3)
    if prankrand == 2:
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="you sleep"))
    if prankrand == 1:
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="you eat cheese at 3am"))
    if prankrand == 3:
        await client.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name="you eat"))

    if not message.author.id == 779429937559633920:
        if message.content in alwayscommands:
            await message.channel.send(alwayscommands[message.content])
        if message.content in eventcommands:
            await message.channel.send(eventcommands[message.content])
        if (message.content == "hello") or (message.content == "hi"):
            hellorand = random.randint(1, 4)
            if hellorand == 1:
                await message.channel.send("fuck off")
            elif hellorand == 2:
                await message.channel.send("get away demon")
            elif hellorand == 3:
                await message.channel.send("begon THOT")
            else:
                await message.channel.send("sup bitch")


make_website()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
