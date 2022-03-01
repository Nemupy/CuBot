import discord
from discord.ext import commands
from discord.commands import slash_command


class AppCmdManageUnban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
        member = await self.bot.fetch_user(id)
        embed = discord.Embed(title="ユーザーのBANが解除されました。",
                              description="", color=0x3498DB)
        embed.add_field(name="対象者", value=f"{member.mention}", inline=True)
        embed.add_field(
            name="実行者", value=f"{ctx.author.mention}", inline=True)
        embed.set_thumbnail(url=member.avatar.url)
        await member.send(embed=embed)
        await ctx.reply(embed=embed)
        await ctx.guild.unban(member)


def setup(bot):
    return bot.add_cog(AppCmdManageUnban(bot))