import discord
from discord.ext import commands
import os
import sys

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=["Cu!", "cu!"],
    help_command=None,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(replied_user=False, everyone=False, roles=False),
    case_insensitive=True
)

token = os.environ["token"]

def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)

bot.load_extension('jishaku')

bot.load_extension("Cogs.event")
bot.load_extension("Cogs.bot")
bot.load_extension("Cogs.tool")
bot.load_extension("Cogs.data")
bot.load_extension("Cogs.variety")
bot.load_extension("Cogs.activity")
bot.load_extension("Cogs.admin")

bot.run(token)
