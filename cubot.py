import discord
from discord.ext import commands, pages
import os

bot = commands.Bot(
    command_prefix=["Cu!", "cu!"],
    help_command=None,
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions(
        replied_user=False, everyone=False, roles=False),
    case_insensitive=True
)


@bot.event
async def on_ready():
    print(f"{bot.user} is online")

bot.load_extension('jishaku')

bot.load_extension("cogs.cubot.help")
bot.load_extension("cogs.cubot.list")
bot.load_extension("cogs.cubot.ping")

bot.load_extension("cogs.manage.kick")
bot.load_extension("cogs.manage.ban")
bot.load_extension("cogs.manage.unban")
bot.load_extension("cogs.manage.mute")
bot.load_extension("cogs.manage.unmute")

bot.load_extension("cogs.playing.5000")
bot.load_extension("cogs.playing.coin")
bot.load_extension("cogs.playing.dice")
bot.load_extension("cogs.playing.neko")
bot.load_extension("cogs.playing.slot")

bot.load_extension("cogs.activity")
bot.load_extension("cogs.bot")
bot.load_extension("cogs.data")
bot.load_extension("cogs.event")
bot.load_extension("cogs.level")
bot.load_extension("cogs.tool")
bot.load_extension("cogs.variety")

token = os.environ["token"]
bot.run(token)
