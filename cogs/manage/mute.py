import discord
from discord.ext import commands
from discord.commands import slash_command


class AppCmdManageMute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, reason_custom="muteコマンド"):
        reason = f"{reason_custom} 実行者：{ctx.author}"
        embed = discord.Embed(title="ユーザーがミュートされました。",
                              description="", color=0x3498DB)
        embed.add_field(name="対象者", value=f"{member.mention}", inline=True)
        embed.add_field(
            name="実行者", value=f"{ctx.author.mention}", inline=True)
        embed.add_field(name="理由", value=f"```{reason}```", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await member.send(embed=embed)
        await ctx.send(embed=embed)
        guild = ctx.guild
        for channel in guild.channels:
            await channel.set_permissions(member, overwrite=None)


def setup(bot):
    return bot.add_cog(AppCmdManageMute(bot))
