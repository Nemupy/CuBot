import discord
from discord.commands import slash_command
from discord.ext import commands, pages


class PageTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def list(self, ctx, type=None):
        embed = discord.Embed(
            title="コマンドリスト", description="使用可能なコマンド一覧です♪\n各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪", colour=0x3498DB)
        embed.add_field(name=":robot: 》BOT",
                        value="`help` `list` `prof` `ping`", inline=False)
        embed.add_field(
            name=":tools: 》ツール",
            value="`kick` `ban` `unban` `mute` `unmute` `timer` `poll` `rect` `embed` `calcu`",
            inline=False,
        )
        embed.add_field(name=":dividers: 》データ",
                        value="`time` `invite`", inline=False)
        embed.add_field(
            name=":video_game: 》バラエティ", value="`fortune` `rps` `dice` `pun` `cquiz` `coin` `slot` `totusi` `5000` `neko`",
            inline=False
        )
        embed1 = discord.Embed(
            title="コマンドリスト-BOT", description="使用可能なコマンド一覧です♪\n各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪", colour=0x3498DB)
        embed1.add_field(
            name=":robot: 》BOT",
            value="`help`：困ったときはを表示します。\n`list`：コマンドリストを表示します。\n`prof`：CuBOTのプロフィールを表示します。\n`ping`：CuBOTのping値を表示します。",
        )
        embed2 = discord.Embed(
            title="コマンドリスト-ツール", description="使用可能なコマンド一覧です♪\n各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪", colour=0x3498DB)
        embed2.add_field(
            name=":tools: 》ツール",
            value="`timer`：タイマーをセットします。\n"
                  "`kick`：ユーザーをキックします。\n"
                  "`ban`：ユーザーをBANします。\n"
                  "`unban`：ユーザーのBANを解除します。\n"
                  "`mute`：ユーザーをミュートします。\n"
                  "`unmute`：ユーザーのミュートを解除します。\n"
                  "`poll`：投票パネルを作成します。\n"
                  "`rect`：募集パネルを作成します。\n"
                  "`embed`：Embedパネルを作成します。\n"
                  "`calcu`：計算をします。",
        )
        embed3 = discord.Embed(
            title="コマンドリスト-データ", description="使用可能なコマンド一覧です♪\n各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪", colour=0x3498DB)
        embed3.add_field(
            name=":dividers: 》データ", value="`time`：現在時刻を表示します。\n`invite`：招待リンクの総使用数を算出します。"
        )
        embed4 = discord.Embed(
            title="コマンドリスト-バラエティ", description="使用可能なコマンド一覧です♪\n各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪", colour=0x3498DB)
        embed4.add_field(
            name=":video_game: 》バラエティ",
            value="`fortune`：おみくじが引けます。\n"
                  "`rps`：じゃんけんができます。\n"
                  "`dice`：サイコロを振れます。\n"
                  "`pun`：ダジャレが聞けます。\n"
                  "`cquiz`：暗算クイズができます。\n"
                  "`coin`：コイントスができます。\n"
                  "`slot`：スロットができます。\n"
                  "`totusi`：突然の死AAを作成します。\n"
                  "`5000`：5000兆円を生成します。\n"
                  "`neko`：猫耳のイラストを生成します。",
        )
        page = [embed, embed1, embed2, embed3, embed4]
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
