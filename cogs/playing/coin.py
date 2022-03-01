import discord
from discord.ext import commands
from discord.commands import slash_command
import random


class AppCmdPlayingCoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="", guild_ids=[825371357402759238])
    async def coin(self, ctx):
        surface = random.choice(("表", "裏"))
        if surface == "表":
            embed = discord.Embed(
                title="コイントス", description="**表**が出ました！", color=0x3498DB)
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/830673701564317727/830771939831971860/"
                    "FavgDW3fhU7oNzgJY98FDvBsv4f8DMemdePw7rqgAAAAASUVORK5CYII.png"
            )
            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                title="コイントス", description="**裏**が出ました！", color=0x3498DB)
            embed.set_thumbnail(
                url="https://media.discordapp.net/attachments/830673701564317727/830763529005957130/toAAAAASUVORK5CYII.png"
            )
            await ctx.respond(embed=embed)


def setup(bot):
    return bot.add_cog(AppCmdPlayingCoin(bot))
