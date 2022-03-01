import discord
from discord.ext import commands
from discord.commands import slash_command


class AppCmdManageKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[825371357402759238])
    @commands.slash_command.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, reason_custom="kickコマンド"):
        reason = f"{reason_custom} 実行者：{ctx.author}"
        embed = discord.Embed(title="ユーザーがキックされました。",
                              description="", color=0x3498DB)
        embed.add_field(name="対象者", value=f"{member.mention}", inline=True)
        embed.add_field(
            name="実行者", value=f"{ctx.author.mention}", inline=True)
        embed.add_field(name="理由", value=f"```{reason}```", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await member.send(embed=embed)
        await ctx.respond(embed=embed)
        await member.kick(reason=reason)


def setup(bot):
    return bot.add_cog(AppCmdManageKick(bot))
