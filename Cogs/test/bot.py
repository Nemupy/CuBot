import discord
from discord.ext import commands
import asyncio
import random
import psutil


class AppCmdBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def help(self, ctx, command=None):
        async with ctx.typing():
            await asyncio.sleep(0)
        if command == "help":
            embed = discord.Embed(title="DETAIL-help",
                                  description="困ったときはを表示します。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/859408401419599882/859409365140635688/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "list":
            embed = discord.Embed(
                title="DETAIL-list", description="コマンドリストを表示します。", colour=0x3498DB)
            embed.set_footer(text="リアクションページを使用できます。")
            embed.set_image(
                url="https://media.discordapp.net/attachments/859408401419599882/859409537252327434/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "prof":
            embed = discord.Embed(
                title="DETAIL-prof", description="CuBOTのプロフィールを表示します。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829292378241105950/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "ping":
            embed = discord.Embed(
                title="DETAIL-ping", description="CuBOTのping値を表示します。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829292685457621032/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "kick":
            embed = discord.Embed(title="DETAIL-kick",
                                  description="ユーザーをキックします。", colour=0x3498DB)
            embed.add_field(name="使い方", value="Cu!kick [ユーザー名]", inline=True)
            embed.set_footer(text="このコマンドを実行できるのは管理者のみです。")
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829293398682763284/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "ban":
            embed = discord.Embed(title="DETAIL-ban",
                                  description="ユーザーをBANします。", colour=0x3498DB)
            embed.add_field(name="使い方", value="Cu!ban [ユーザー名]", inline=True)
            embed.set_footer(text="このコマンドを実行できるのは管理者のみです。")
            embed.set_image(
                url="https://images-ext-2.discordapp.net/external/9S1B_5tzfHj-E7W1P92sT9uoMJgLyCIPoKUEWM2J338/"
                    "https/media.discordapp.net/attachments/826804140398215218/829293782284894258/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "unban":
            embed = discord.Embed(
                title="DETAIL-unban", description="ユーザーのBANを解除します。", colour=0x3498DB)
            embed.add_field(name="使い方", value="Cu!unban [ユーザーID]", inline=True)
            embed.set_footer(text="このコマンドを実行できるのは管理者のみです。")
            embed.set_image(
                url="https://media.discordapp.net/attachments/826803343669854229/859407084339986452/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "timer":
            embed = discord.Embed(title="DETAIL-timer",
                                  description="タイマーをセットします。", colour=0x3498DB)
            embed.add_field(name="使い方", value="Cu!timer [秒数]", inline=True)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829292950793879552/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "poll":
            embed = discord.Embed(title="DETAIL-poll",
                                  description="投票パネルを作成します。", colour=0x3498DB)
            embed.add_field(
                name="使い方", value="Cu!poll [議題] [項目1] [項目2] [項目3] [項目4]", inline=True)
            embed.set_footer(text="選択肢は4つまで作成できます。")
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829293852077588500/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "rect":
            embed = discord.Embed(title="DETAIL-rect",
                                  description="募集パネルを作成します。", colour=0x3498DB)
            embed.add_field(
                name="使い方", value="Cu!rect [募集内容] [募集人数] [締め切り時間]", inline=True)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829293919971967016/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "embed":
            embed = discord.Embed(
                title="DETAIL-embed", description="Embedパネルを作成します。", colour=0x3498DB)
            embed.add_field(
                name="使い方", value="Cu!embed [タイトル] [説明]", inline=True)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829294113576452096/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "calcu":
            embed = discord.Embed(title="DETAIL-calcu",
                                  description="計算をします。", colour=0x3498DB)
            embed.add_field(
                name="使い方", value="Cu!calcu [数値1] [算法] [数値2]", inline=True)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/844209477657559060/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "time":
            embed = discord.Embed(title="DETAIL-time",
                                  description="現在時刻を表示します。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829294591185256518/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "invite":
            embed = discord.Embed(
                title="DETAIL-invite", description="招待リンクの総使用数を算出します。", colour=0x3498DB)
            embed.add_field(name="使い方", value="Cu!invite [ユーザー名]", inline=True)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/844209266934939680/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "fortune":
            embed = discord.Embed(title="DETAIL-fortune",
                                  description="おみくじが引けます。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829296454110674954/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "rps":
            embed = discord.Embed(title="DETAIL-rps",
                                  description="じゃんけんができます。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829296691290308618/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "dice":
            embed = discord.Embed(title="DETAIL-dice",
                                  description="サイコロを振れます。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829296842063347742/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "pun":
            embed = discord.Embed(title="DETAIL-pun",
                                  description="ダジャレが聞けます。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829297151213043722/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "cquiz":
            embed = discord.Embed(title="DETAIL-cquiz",
                                  description="暗算クイズができます。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/829297392356556820/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "coin":
            embed = discord.Embed(title="DETAIL-coin",
                                  description="コイントスができます。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/830784293148033042/unknown.png"
            )
            await ctx.reply(embed=embed)
        elif command == "slot":
            embed = discord.Embed(title="DETAIL-slot",
                                  description="スロットができます。", colour=0x3498DB)
            embed.set_image(
                url="https://media.discordapp.net/attachments/826804140398215218/832000993205682206/unknown.png"
            )
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="ヘルプ", description="こんにちはー！\n日本生まれ日本育ちの純国産BOT！Cuです！", colour=0x3498DB)
            embed.add_field(name=":dividers:》目次",
                            value="１．`コマンド一覧`\n２．`BOTの招待方法`\n３．`よくある質問`")
            embed.set_image(
                url="https://media.discordapp.net/attachments/826812760435195904/913384084003258418/4.gif")
            embed1 = discord.Embed(title="ヘルプ-コマンドリスト",
                                   description="使用可能なコマンド一覧です♪\n各コマンドの詳細は`Cu!help [コマンド名]`で確認できます♪", colour=0x3498DB)
            embed1.add_field(name=":robot: 》BOT",
                             value="`help` `list` `prof` `ping`", inline=False)
            embed1.add_field(
                name=":tools: 》ツール",
                value="`kick` `ban` `unban` `mute` `unmute` `timer` `poll` `rect` `embed` `calcu`",
                inline=False,
            )
            embed1.add_field(name=":dividers: 》データ",
                             value="`time` `invite`", inline=False)
            embed1.add_field(
                name=":video_game: 》バラエティ", value="`fortune` `rps` `dice` `pun` `cquiz` `coin` `slot` `totusi` `5000` `neko`",
                inline=False
            )
            embed2 = discord.Embed(title="ヘルプ-BOTの招待方法",
                                   description="①[招待リンク](https://discord.com/api/oauth2/authorize?client_id=826228756657078272&permissions=8&scope=bot)を開きます。\n②追加したいサーバーを選びます。\n③付与したい権限を選びます。\n　※権限が足りないとエラーを吐きます。\n　　管理者権限付与がオススメ！\n④必要に応じて認証を済ませます。\n⑤招待完了！",
                                   colour=0x3498DB)
            embed2.add_field(name=":link:》招待リンク",
                             value="`管理者権限付きで招待`：[ClickHere](https://discord.com/api/oauth2/authorize?client_id=826228756657078272&permissions=8&scope=bot)\n`権限を選択して招待`：[ClickHere](https://discord.com/channels/825371357402759238/912244061421846598/913409445738971157)\n`権限なしで招待`：[ClickHere](https://discord.com/api/oauth2/authorize?client_id=826228756657078272&permissions=0&scope=bot)")
            embed3 = discord.Embed(title="ヘルプ-よくある質問", colour=0x3498DB)
            embed3.add_field(name=":question:》入退室メッセージはカスタマイズできますか？",
                             value="情報系に関する内容を扱っていないためカスタマイズすることはできません。ご期待に沿えるよう邁進して参りますのでよろしくお願いします。", inline=False)
            embed3.add_field(name=":question:》安全ですか？",
                             value="安全です。基本的に情報は取得していないので漏れる心配はございません。また、認証を通しているのでより強く保護されています。", inline=False)
            embed3.add_field(name=":question:》BOTがオフラインになるのはなぜですか？",
                             value="使用しているサーバーのクラッシュが原因です。8割オーナーのミスで落ちているのはナイショ。", inline=False)
            pages = [embed, embed1, embed2, embed3]
            page = 0
            message = await ctx.reply(embed=pages[page])
            await message.add_reaction("⏮")
            await message.add_reaction("◀️")
            await message.add_reaction("⏹")
            await message.add_reaction("▶️")
            await message.add_reaction("⏭")

            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) in ["⏮", "◀️", "⏹", "▶️", "⏭"]

            while True:
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                    if str(reaction.emoji) == "⏮" and page != 0:
                        page = 0
                        await message.edit(embed=pages[page])
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "◀️" and page != 0:
                        page -= 1
                        await message.edit(embed=pages[page])
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⏹":
                        await message.edit(embed=embed)
                        await message.clear_reactions()
                        break
                    elif str(reaction.emoji) == "▶️" and page != 3:
                        page += 1
                        await message.edit(embed=pages[page])
                        await message.remove_reaction(reaction, user)
                    elif str(reaction.emoji) == "⏭" and page != 3:
                        page = 3
                        await message.edit(embed=pages[page])
                        await message.remove_reaction(reaction, user)
                    else:
                        await message.remove_reaction(reaction, user)
                except asyncio.TimeoutError:
                    await message.edit(embed=embed)
                    await message.clear_reactions()
                    break

    @commands.command()
    async def list(self, ctx, type=None):
        async with ctx.typing():
            await asyncio.sleep(0)
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
        pages = [embed, embed1, embed2, embed3, embed4]
        page = 0
        message = await ctx.reply(embed=pages[page])
        await message.add_reaction("⏮")
        await message.add_reaction("◀️")
        await message.add_reaction("⏹")
        await message.add_reaction("▶️")
        await message.add_reaction("⏭")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["⏮", "◀️", "⏹", "▶️", "⏭"]

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                if str(reaction.emoji) == "⏮" and page != 0:
                    page = 0
                    await message.edit(embed=pages[page])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "◀️" and page != 0:
                    page -= 1
                    await message.edit(embed=pages[page])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "⏹":
                    await message.edit(embed=embed)
                    await message.clear_reactions()
                    break
                elif str(reaction.emoji) == "▶️" and page != 4:
                    page += 1
                    await message.edit(embed=pages[page])
                    await message.remove_reaction(reaction, user)
                elif str(reaction.emoji) == "⏭" and page != 4:
                    page = 4
                    await message.edit(embed=pages[page])
                    await message.remove_reaction(reaction, user)
                else:
                    await message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                await message.edit(embed=embed)
                await message.clear_reactions()
                break

    @commands.command()
    async def prof(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        mame = random.choice(
            ("イメージキャラクターの本名は「金同 鈴樺」です！", "CuBOTは皆様のDiscordライフをより明るくしようと誕生しました！", "CuBOTはCuと書いてきゅーと発音します！"))
        embed = discord.Embed(title="CuBOTプロフィール",
                              description="CuBOTの自己紹介ページです♪", color=0x3498DB)
        embed.set_thumbnail(
            url="https://pbs.twimg.com/media/EfWoupuUYAAwuTv?format=jpg&name=large")
        embed.add_field(
            name="🤔》Cuとは", value="日本生まれ日本育ちのDiscordBOTです！\n日々勉強に励み成長中！", inline=False)
        embed.add_field(name="🔧》開発者", value="<@798439010594717737> [Twitter](https://twitter.com/Nemu627)",
                        inline=False)
        embed.add_field(
            name="🖼》アイコン", value="Shano様 [Twitter](https://twitter.com/ShanoPirika)", inline=False)
        embed.add_field(
            name="✅》公式",
            value="`公式サーバー`：[ClickHere](https://discord.gg/RFPQmRnv2j)\n"
                  "`公式ツイッター`：[ClickHere](https://twitter.com/CubotOfficial)",
            inline=False,
        )
        embed.set_footer(text="CuBOT豆知識：" + mame)
        await ctx.reply(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title="PING", description=f"`PING`：{round(self.bot.latency * 1000)}ms",
                              color=0x3498DB)
        await ctx.reply(embed=embed)

    @commands.command()
    async def status(self, ctx):
        embed = discord.Embed(
            title="サーバーの使用状況", description=f"`CPU使用率`：{psutil.cpu_percent()}%\n`メモリ使用率`：{psutil.virtual_memory().percent}%", colour=0x3498DB)
        await ctx.send(embed=embed)


def setup(bot):
    return bot.add_cog(AppCmdBot(bot))
