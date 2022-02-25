import discord
from discord.ext import commands
import os

bot = commands.Bot(
    command_prefix=["Cu!", "cu!"],
    help_command=None,
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions(
        replied_user=False, everyone=False, roles=False),
    case_insensitive=True
)

token = os.environ["token"]


bot.load_extension('jishaku')

bot.load_extension("Cogs.event")
bot.load_extension("Cogs.bot")
bot.load_extension("Cogs.tool")
bot.load_extension("Cogs.data")
bot.load_extension("Cogs.variety")
bot.load_extension("Cogs.level")

bot.run(token)
