import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=["Cu!", "cu!"],
    help_command=None,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(replied_user=False, everyone=False),
    case_insensitive=True
)


token = os.environ["token"]

def restart_bot():
  os.execv(sys.executable, ['python'] + sys.argv)

@bot.event
async def on_ready():
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    await bot.change_presence(
        activity=discord.Activity(name=f"Cu!help | {str(servers)}servers | {str(members)}users", type=3)
    )

bot.load_extension("Cogs.event")
bot.load_extension("Cogs.bot")
bot.load_extension("Cogs.tool")
bot.load_extension("Cogs.data")
bot.load_extension("Cogs.variety")

bot.run(token)
