import discord
from discord.ext import commands
from credentials import BOT_TOKEN
from config import (
    PING_CHAT_ID,
    EXCLUDE_CHAT_IDS,
    PING_MESSAGE_ACTION,
    PING_MESSAGE_WITH_TEXT_ACTION,
)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    pass
  

bot.run(BOT_TOKEN)