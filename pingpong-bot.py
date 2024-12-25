## Ping-Pong Bot

import random
import os
import subprocess
import sys

# List required packages
discord_package = "discord.py"
dotenv_package= "python-dotenv"

try:
    __import__(discord_package.split('.')[0])  # Import the base module
except ImportError:
    print(f"Package {discord_package} not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", discord_package])
try:
    __import__("dotenv")  # Import the base module
except ImportError:
    print(f"Package {dotenv_package} not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", dotenv_package])

# Import needed packages
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.messages = True  # Enable message intents
intents.message_content = True  # Allow content analysis
bot = commands.Bot(command_prefix="!", intents=intents)

allowedUsers = {204659941892554752, 139114165523447809, 160847221582069761}

@bot.event
async def on_message(message):
    # Ignore bot's own messages to avoid infinite loops
    if message.author == bot.user:
        return

    if message.author.id in allowedUsers and message.content.lower() == "ping":
        await message.channel.send("pong")

    # Allow other commands to still work
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def pinghello(ctx):
    await ctx.send(":smile:")

bot.run(TOKEN)
