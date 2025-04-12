import discord
from discord.ext import commands
from discord import app_commands

class HelpCmdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="ヘルプを表示します。")
    @app_commands.describe(command="使い方を表示したいコマンド")
    async def help(self, interaction: discord.Interaction, commmand: str =None):
        embed = discord.Embed(
            title="ヘルプ",
            description="各コマンドの詳細は`/help [コマンド名]`で確認できます。",
            colour=0x3498DB
        )
        embed.add_field(
            name="General",
            value="`help`",
            inline=False
        )
        embed.add_field(
            name="Utility",
            value="coming soon...",
            inline=False,
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(HelpCmdCog(bot))