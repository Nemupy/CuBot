import discord
from discord.ext import commands
from discord.commands import slash_command
import random


class AppCmdPlayingDice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[825371357402759238], discription="サイコロを振ります。")
    async def dice(self, ctx):
        dice = random.randint(1, 6)
        embed = discord.Embed(
            title="サイコロ", description="[出目] " + str(dice), colour=0x3498DB)
        embed.set_thumbnail(
            url="https://smilescience.up.seesaa.net/image/E382B5E382A4E382B3E383ADE381AEE79BAEE5B08F_"
                + str(dice)
                + "-thumbnail2.png"
        )
        await ctx.respond(embed=embed)


def setup(bot):
    return bot.add_cog(AppCmdPlayingDice(bot))
