import discord
from discord.ext import commands
from discord.commands import slash_command


class AppCmdManageUnmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        embed = discord.Embed(title="ユーザーのミュートが解除されました。",
                              description="", color=0x3498DB)
        embed.add_field(name="対象者", value=f"{member.mention}", inline=True)
        embed.add_field(
            name="実行者", value=f"{ctx.author.mention}", inline=True)
        embed.set_thumbnail(url=member.avatar.url)
        await member.send(embed=embed)
        await ctx.send(embed=embed)
        guild = ctx.guild
        for channel in guild.channels:
            await channel.set_permissions(member, send_messages=False)


def setup(bot):
    return bot.add_cog(AppCmdManageUnmute(bot))
