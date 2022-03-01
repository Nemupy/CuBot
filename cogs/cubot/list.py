import discord
from discord.commands import slash_command
from discord.ext import commands, pages


class PageTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(guild_ids=[825371357402759238], description="コマンドリストを表示します。")
    async def list(self, ctx):
        embed = discord.Embed(
            title="コマンドリスト",
            description="使用可能なコマンド一覧です♪\n"
                        "各コマンドの詳細は`/help [コマンド名]`で確認できます♪",
            colour=0x3498DB
        )
        embed.add_field(
            name=":robot: 》CuBot",
            value="`help` `list` `ping`",
            inline=False
        )
        embed.add_field(
            name=":tools: 》Manage",
            value="`kick` `ban` `unban` `mute` `unmute`",
            inline=False,
        )
        embed.add_field(
            name=":video_game: 》Playing",
            value="`choyen` `coin` `dice` `neko` `slot`",
            inline=False
        )
        embed1 = discord.Embed(
            title="コマンドリスト-CuBot",
            description="使用可能なコマンド一覧です♪\n"
                        "各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪",
            colour=0x3498DB
        )
        embed1.add_field(
            name=":robot: 》CuBot",
            value="`help`：ヘルプを表示します。\n"
                  "`list`：コマンドリストを表示します。\n"
                  "`ping`：CuBotのPing値を表示します。",
        )
        embed2 = discord.Embed(
            title="コマンドリスト-Manage",
            description="使用可能なコマンド一覧です♪\n"
                        "各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪",
            colour=0x3498DB
        )
        embed2.add_field(
            name=":tools: 》Manage",
            value="`kick`：ユーザーをキックします。\n"
                  "`ban`：ユーザーをBANします。\n"
                  "`unban`：ユーザーのBANを解除します。\n"
                  "`mute`：ユーザーをミュートします。\n"
                  "`unmute`：ユーザーのミュートを解除します。",
        )
        embed3 = discord.Embed(
            title="コマンドリスト-Playing",
            description="使用可能なコマンド一覧です♪\n"
                        "各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪",
                        colour=0x3498DB
        )
        embed3.add_field(
            name=":video_game: 》Playing",
            value="`5000`：5000兆円を生成します。\n"
                  "`coin`：コイントスをします。\n"
                  "`dice`：サイコロを振ります。\n"
                  "`neko`：猫耳のイラストを生成します。"
                  "`slot`：スロットを回します。\n",
        )
        page = [embed, embed1, embed2, embed3]
        paginator = pages.Paginator(pages=page)
        paginator.add_button(pages.PaginatorButton(
            "first", label="<<", style=discord.ButtonStyle.primary))
        paginator.add_button(pages.PaginatorButton(
            "prev", label="<", style=discord.ButtonStyle.primary))
        paginator.add_button(pages.PaginatorButton(
            "page_indicator", style=discord.ButtonStyle.primary))
        paginator.add_button(pages.PaginatorButton(
            "next", label=">", style=discord.ButtonStyle.primary))
        paginator.add_button(pages.PaginatorButton(
            "last", label=">>", style=discord.ButtonStyle.primary))
        await paginator.respond(ctx.interaction, ephemeral=False)


def setup(bot):
    bot.add_cog(PageTest(bot))
