import discord
from discord.ext import commands
import os
import sys

class AppCmdAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command()
    async def restart(self, ctx):
        if ctx.author.id == 798439010594717737:
            await ctx.reply("再起動を実行中です・・・")
            os.execv(sys.executable, ['python'] + sys.argv)
            
def setup(bot):
    return bot.add_cog(AppCmdAdmin(bot))
