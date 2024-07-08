import discord
from discord.ext import commands
from utils import (
    remove_mentions,
    generate_message
    )
from credentials import BOT_TOKEN
from config import (
    ACTION,
    PING_CHAT_ID,
    EXCLUDE_CHAT_IDS,
    PING_MESSAGE_ACTION,
    PING_MESSAGE_WITH_TEXT_ACTION,
    NEW_MESSAGE_PATTERN
)

intents = discord.Intents.default()
intents.reactions = True
intents.members = True
intents.guilds = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
ping_channel = None


@bot.event
async def on_ready():
    global ping_channel
    ping_channel = bot.get_channel(PING_CHAT_ID)


@bot.event
async def on_message(message):
    channel_id = message.channel.id
    if message.mentions and channel_id != PING_CHAT_ID and channel_id not in EXCLUDE_CHAT_IDS:
        action = PING_MESSAGE_WITH_TEXT_ACTION if remove_mentions(message.content) else PING_MESSAGE_ACTION
        new_message = generate_message(NEW_MESSAGE_PATTERN, message.content, message.author.display_name)
        match action:
            case ACTION.MOVE:
                await message.delete()
                await ping_channel.send(new_message)
            case ACTION.COPY:
                await ping_channel.send(new_message)


bot.run(BOT_TOKEN)