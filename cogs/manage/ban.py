import discord
from discord.ext import commands
from discord.commands import slash_command


class AppCmdManageBan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[825371357402759238], description="ユーザーをBANします。")
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, reason_custom="banコマンド"):
        reason = f"{reason_custom} 実行者：{ctx.author}"
        embed = discord.Embed(title="ユーザーがBANされました。",
                              description="", color=0x3498DB)
        embed.add_field(name="対象者", value=f"{member.mention}", inline=True)
        embed.add_field(
            name="実行者", value=f"{ctx.author.mention}", inline=True)
        embed.add_field(name="理由", value=f"```{reason}```", inline=False)
        embed.set_thumbnail(url=member.avatar.url)
        await member.send(embed=embed)
        await ctx.respond(embed=embed)
        await member.ban(reason=reason)


def setup(bot):
    return bot.add_cog(AppCmdManageBan(bot))
