import discord
from discord.ext import commands
from discord.commands import slash_command
import aiohttp


class AppCmdPlayingNeko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[825371357402759238])
    async def neko(self, ctx, type="neko"):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://nekobot.xyz/api/image?type="+type
            ) as response:
                res = await response.json()
                embed = discord.Embed(color=0x3498DB)
                embed.set_image(url=res["message"])
                await ctx.respond(embed=embed)


def setup(bot):
    return bot.add_cog(AppCmdPlayingNeko(bot))
