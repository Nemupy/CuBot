import discord
from discord.ext import commands
from discord.commands import slash_command
import random


class AppCmdPlayingSlot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[825371357402759238])
    async def slot(self, ctx):
        A = random.choice((":one:", ":two:", ":three:"))
        B = random.choice((":one:", ":two:", ":three:"))
        C = random.choice((":one:", ":two:", ":three:"))
        embed = discord.Embed(title="スロット", description="| " +
                              A + " | " + B + " | " + C + " |", color=0x3498DB)
        await ctx.respond(embed=embed)
        if A == B == C:
            await ctx.respond("当選おめでとう！")


def setup(bot):
    return bot.add_cog(AppCmdPlayingSlot(bot))
