import discord
from discord.ext import commands
import asyncio
import random

class AppCmdBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def help(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title="困ったときは", description="お困りですか？BOTの使い方など全力でサポートいたします！", color=0x3498DB)
        embed.add_field(name="🤖》コマンド", value="`コマンドリスト`：Cu!list\n`各コマンドの詳細`：Cu!detail [コマンド名]", inline=False)
        embed.add_field(
            name="✅》公式アカウント",
            value="`公式サーバー`：[ClickHere](https://discord.gg/RFPQmRnv2j)\n"
                  "`開発者`：<@798439010594717737>\n"
                  "`招待リンク`：[ClickHere]("
                  "https://discord.com/api/oauth2/authorize?client_id=826228756657078272&permissions=8&scope=bot)",
            inline=False,
        )
        embed.set_footer(text="その他不具合があれば公式サーバーまでご気軽にお声掛けください♪")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def list(self,ctx, type=None):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title="コマンドリスト", description="使用可能なコマンド一覧です♪", colour=0x3498DB)
        embed.add_field(name=":robot: 》BOT", value="`help` `list` `prof` `ping`", inline=False)
        embed.add_field(
            name=":tools: 》ツール",
            value="`kick` `ban` `unban` `mute` `unmute` `timer` `poll` `rect` `embed` `calcu`",
            inline=False,
        )
        embed.add_field(name=":dividers: 》データ", value="`time` `detail` `invite`", inline=False)
        embed.add_field(
            name=":video_game: 》バラエティ", value="`fortune` `rps` `dice` `pun` `cquiz` `coin` `slot` `totusi`",
            inline=False
        )
        embed.set_footer(text="各コマンドの詳細は`Cu!detail [コマンド名]`で確認できます♪")
        embed1 = discord.Embed(title="コマンドリスト-BOT", description="使用可能なコマンド一覧です♪", colour=0x3498DB)
        embed1.add_field(
            name=":robot: 》BOT",
            value="`help`：困ったときはを表示します。\n`list`：コマンドリストを表示します。\n`prof`：CuBOTのプロフィールを表示します。\n`ping`：CuBOTのping値を表示します。",
        )
        embed1.set_footer(text="各コマンドの詳細は`Cu!detail [コマンド名]`で確認できます♪")
        embed2 = discord.Embed(title="コマンドリスト-ツール", description="使用可能なコマンド一覧です♪", colour=0x3498DB)
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
        embed2.set_footer(text="各コマンドの詳細は`Cu!detail [コマンド名]`で確認できます♪")
        embed3 = discord.Embed(title="コマンドリスト-データ", description="使用可能なコマンド一覧です♪", colour=0x3498DB)
        embed3.add_field(
            name=":dividers: 》データ", value="`time`：現在時刻を表示します。\n" "`detail`：各コマンドの詳細を表示します。\n`invite`：招待リンクの総使用数を算出します。"
        )
        embed3.set_footer(text="各コマンドの詳細は`Cu!detail [コマンド名]`で確認できます♪")
        embed4 = discord.Embed(title="コマンドリスト-バラエティ", description="使用可能なコマンド一覧です♪", colour=0x3498DB)
        embed4.add_field(
            name=":video_game: 》バラエティ",
            value="`fortune`：おみくじが引けます。\n"
                  "`rps`：じゃんけんができます。\n"
                  "`dice`：サイコロを振れます。\n"
                  "`pun`：ダジャレが聞けます。\n"
                  "`cquiz`：暗算クイズができます。\n"
                  "`coin`：コイントスができます。\n"
                  "`slot`：スロットができます。\n"
                  "`totusi`：突然の死AAを作成します。",
        )
        embed4.set_footer(text="各コマンドの詳細は`Cu!detail [コマンド名]`で確認できます♪")
        pages = [embed, embed1, embed2, embed3, embed4]
        page = 0
        message = await ctx.reply(embed=pages[page], mention_author=False)
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                if str(reaction.emoji) == "▶️" and page != 4:
                    page += 1
                    await message.edit(embed=pages[page])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "◀️" and page > 0:
                    page -= 1
                    await message.edit(embed=pages[page])
                    await message.remove_reaction(reaction, user)
                else:
                    await message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await message.edit(embed=embed)
                await message.clear_reactions()
                break

    @commands.command()
    async def prof(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        mame = random.choice(
            ("イメージキャラクターの本名は「金同 鈴樺」です！", "CuBOTは皆様のDiscordライフをより明るくしようと誕生しました！", "CuBOTはCuと書いてきゅーと発音します！"))
        embed = discord.Embed(title="CuBOTプロフィール", description="CuBOTの自己紹介ページです♪", color=0x3498DB)
        embed.set_thumbnail(url="https://pbs.twimg.com/media/EfWoupuUYAAwuTv?format=jpg&name=large")
        embed.add_field(name="🤔》Cuとは", value="日本生まれ日本育ちのDiscordBOTです！\n日々勉強に励み成長中！", inline=False)
        embed.add_field(name="🔧》開発者", value="<@798439010594717737> [Twitter](https://twitter.com/Nemu627)",
                        inline=False)
        embed.add_field(name="🖼》アイコン", value="Shano様 [Twitter](https://twitter.com/ShanoPirika)", inline=False)
        embed.add_field(
            name="✅》公式",
            value="`公式サーバー`：[ClickHere](https://discord.gg/RFPQmRnv2j)\n"
                  "`公式ツイッター`：[ClickHere](https://twitter.com/CubotOfficial)",
            inline=False,
        )
        embed.set_footer(text="CuBOT豆知識：" + mame)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def ping(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title="PING", description=f"ただいまのping値は**{round(self.bot.latency * 1000)}**msです！",
                              color=0x3498DB)
        await ctx.reply(embed=embed, mention_author=False)

def setup(bot):
    return bot.add_cog(AppCmdBot(bot))
