import discord
from discord.ext import commands, pages
import os
import sys

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=["Te!", "te!"],
    help_command=None,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(
        replied_user=False, everyone=False, roles=False),
    case_insensitive=True
)

@bot.event
async def on_ready():
  print("hi")

@bot.command(name= 'restart')
async def restart(ctx):
  await ctx.send("Restarting bot...")
  os.execv(sys.executable, ['python'] + sys.argv)

bot.load_extension('jishaku')

bot.load_extension("cogs.cubot.help")
bot.load_extension("cogs.cubot.ping")
bot.load_extension("cogs.manage.ban")
bot.load_extension("cogs.playing.omikuji")

bot.run("ODQ3ODE1ODM2MDYzNjI5MzIy.YLDkBg.FkYznaghSa3EfzlXFwDqPkfT5rk")
