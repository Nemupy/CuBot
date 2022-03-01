import discord
from discord.ext import commands
from discord.commands import slash_command
import urllib


class AppCmdPlaying5000(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[825371357402759238], name="5000", description="5000兆円を生成します。")
    async def cmd_5000(self, ctx, top="5000兆円", bottom="欲しい！"):
        embed = discord.Embed(title="5000兆円ジェネレーター",
                              description=f"{top}{bottom}", color=0x3498DB)
        embed.set_image(
            url="https://gsapi.cyberrex.jp/image?"f"top={urllib.parse.quote(top)}&bottom={urllib.parse.quote(bottom)}")
        await ctx.respond(embed=embed)


def setup(bot):
    return bot.add_cog(AppCmdPlaying5000(bot))
