import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bad_words = ["fuck", "shit", "bitch", "asshole", "bastard", "slut", "nigger", "dick", "cock", "pussy"]

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"👋 Hi {member.name}, welcome to **Coca-Cola®**!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for word in bad_words:
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"⚠️ {message.author.mention}, watch your language!")
            return

    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
