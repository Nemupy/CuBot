import discord
from discord.ext import commands
import random
import datetime
import asyncio
import traceback
import sys
from mcstatus import MinecraftServer
import os
from discord.app import Option

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(
    command_prefix=["Cu!", "cu!"],
    help_command=None,
    intents=intents,
    allowed_mentions=discord.AllowedMentions(replied_user=False, everyone=False),
)
bot.load_extension("dispander")
token = os.environ["token"]

def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)


@bot.event
async def on_ready():
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1
    await bot.change_presence(
        activity=discord.Activity(name=f"Cu!help | {str(servers)}servers | {str(members)}users", type=3)
    )

@bot.event
async def on_guild_join(guild):
    member_count = guild.member_count
    embed = discord.Embed(title = "導入してくれてありがとう！", description = f"<@826228756657078272>が導入されました。\nCuは{member_count}人目のユーザーです。", color = 0x3498DB)
    embed.set_thumbnail(url = "https://images-ext-1.discordapp.net/external/bi88_iGaiR-z5Oc6L0OBqkgDkY1UMe7sIPX94aZu8RE/%3Fformat%3Djpg%26name%3Dlarge/https/pbs.twimg.com/media/EfWoupuUYAAwuTv?width=473&height=473")
    await guild.system_channel.send(embed=embed)
    

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        embed = discord.Embed(
        title="エラー-不明なコマンド",
        description="不明なコマンドです。`Cu!list`でコマンドを確認してください。\nこのエラーが多発する場合は[公式サーバー](https://discord.gg/RFPQmRnv2j)までお問い合わせください。\n```" + error_msg + "```",
        colour=0x3498DB,
        )
        await ctx.reply(embed=embed)
    elif isinstance(error, commands.errors.MissingPermissions):
        embed = discord.Embed(
        title="エラー-権限不足",
        description="権限が不足しています。権限設定をご確認ください。\nこのエラーが多発する場合は[公式サーバー](https://discord.gg/RFPQmRnv2j)までお問い合わせください。\n```" + error_msg + "```",
        colour=0x3498DB,
        )
    else:
        orig_error = getattr(error, "original", error)
        error_msg = "".join(traceback.TracebackException.from_exception(orig_error).format())
        embed = discord.Embed(
            title="エラー",
            description="予期せぬエラーが発生しました。\nこのエラーが多発する場合は[公式サーバー](https://discord.gg/RFPQmRnv2j)までお問い合わせください。\n```" + error_msg + "```",
            colour=0x3498DB,
        )
        await ctx.reply(embed=embed, mention_author=False)


@bot.event
async def on_member_join(member):
    if member.guild.system_channel:
        guild = member.guild
        guild_name = member.guild.name
        member_count = guild.member_count
        embed = discord.Embed(
            title=f"ようこそ！{guild_name}へ！",
            description=f"{member.mention}さんが入室しました。 \nあなたは{str(member_count)}人目のユーザーです。",
            color=0x3498DB,
        )
        embed.set_thumbnail(url=member.avatar.url)
        await member.guild.system_channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    if member.guild.system_channel:
        embed = discord.Embed(title="また来てね！", description=f"{member.mention}さんが退室しました。", colour=0x3498DB)
        embed.set_thumbnail(url=member.avatar.url)
        await member.guild.system_channel.send(embed=embed)


@bot.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.type == discord.MessageType.new_member:
        await message.delete()
        return
    elif bot.user.id in message.raw_mentions:
        await message.reply("お呼びでしょうか！お困りの際は`Cu!help`と送信してみて下さいね♪", mention_author=False)
    await bot.process_commands(message)


@bot.command()
async def mcserver(ctx, ip):
    server = MinecraftServer.lookup(ip)
    status = server.status()
    embed = discord.Embed(
        title="Minecraftサーバーステータス情報",
        description=f"`応答速度`：{status.latency}ms\n"
        f"`バージョン`：{status.version.name}\n"
        f"`オンライン人数`：{status.players.online} / {status.players.max}",
        color=0x3498DB,
    )
    await ctx.send(embed=embed)


# -----«コマンド-BOT»-------------------------


@bot.command("help")
async def help_command(ctx):
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


@bot.command("list")
async def command_list(ctx, type=None):
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
        name=":video_game: 》バラエティ", value="`fortune` `rps` `dice` `pun` `cquiz` `coin` `slot` `totusi`", inline=False
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
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
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


@bot.command()
async def prof(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    mame = random.choice(("イメージキャラクターの本名は「金同 鈴樺」です！", "CuBOTは皆様のDiscordライフをより明るくしようと誕生しました！", "CuBOTはCuと書いてきゅーと発音します！"))
    embed = discord.Embed(title="CuBOTプロフィール", description="CuBOTの自己紹介ページです♪", color=0x3498DB)
    embed.set_thumbnail(url="https://pbs.twimg.com/media/EfWoupuUYAAwuTv?format=jpg&name=large")
    embed.add_field(name="🤔》Cuとは", value="日本生まれ日本育ちのDiscordBOTです！\n日々勉強に励み成長中！", inline=False)
    embed.add_field(name="🔧》開発者", value="<@798439010594717737> [Twitter](https://twitter.com/Nemu627)", inline=False)
    embed.add_field(name="🖼》アイコン", value="Shano様 [Twitter](https://twitter.com/ShanoPirika)", inline=False)
    embed.add_field(
        name="✅》公式",
        value="`公式サーバー`：[ClickHere](https://discord.gg/RFPQmRnv2j)\n"
        "`公式ツイッター`：[ClickHere](https://twitter.com/CubotOfficial)",
        inline=False,
    )
    embed.set_footer(text="CuBOT豆知識：" + mame)
    await ctx.reply(embed=embed, mention_author=False)


@bot.command()
async def ping(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    embed = discord.Embed(title="PING", description=f"ただいまのping値は**{round(bot.latency *1000)}**msです！", color=0x3498DB)
    await ctx.reply(embed=embed, mention_author=False)


# -----«コマンド-ツール»-------------------------


@bot.command()
async def kick(ctx, member: discord.Member, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0)
    if ctx.author.guild_permissions.administrator:
        kick = discord.Embed(
            title="メンバーをキックしました。", description=f"{ctx.author.mention}さんが{member.mention}さんをキックしました。", color=0x3498DB
        )
        kick.set_thumbnail(url=member.avatar.url)
        await ctx.reply(embed=kick)
        await member.kick(reason=reason)
    else:
        await ctx.reply("このコマンドを実行できるのは管理者のみです！")


@bot.command()
async def ban(ctx, member: discord.Member, reason=None):
    async with ctx.typing():
        await asyncio.sleep(0)
    if ctx.author.guild_permissions.administrator:
        ban = discord.Embed(
            title="メンバーをBANしました。", description=f"{ctx.author.mention}さんが{member.mention}さんをBANしました。", color=0x3498DB
        )
        ban.set_thumbnail(url=member.avatar.url)
        await ctx.reply(embed=ban)
        await member.ban(reason=reason)
    else:
        await ctx.reply("このコマンドを実行できるのは管理者のみです！")


@bot.command()
async def unban(ctx, id: int):
    if ctx.author.guild_permissions.administrator:
        user = await bot.fetch_user(id)
        unban = discord.Embed(
            title="メンバーのBANを解除しました", description=f"{ctx.author.mention}さんが{user.mention}さんのBANを解除しました。", color=0x3498DB
        )
        unban.set_thumbnail(url=user.avatar.url)
        await ctx.reply(embed=unban)
        await ctx.guild.unban(user)
    else:
        await ctx.reply("このコマンドを実行できるのは管理者のみです！")


@bot.command()
async def mute(ctx, member: discord.Member):
    async with ctx.typing():
        await asyncio.sleep(0)
    if ctx.author.guild_permissions.administrator:
        mute = discord.Embed(
            title="メンバーをミュートしました。", description=f"{ctx.author.mention}さんが{member.mention}さんをミュートしました。", color=0x3498DB
        )
        mute.set_thumbnail(url=member.avatar.url)
        await ctx.reply(embed=mute)
        guild = ctx.guild
        for channel in guild.channels:
            await channel.set_permissions(member, send_messages=False)
    else:
        await ctx.reply("このコマンドを実行できるのは管理者のみです！")


@bot.command()
async def unmute(ctx, member: discord.Member):
    async with ctx.typing():
        await asyncio.sleep(0)
    if ctx.author.guild_permissions.administrator:
        mute = discord.Embed(
            title="メンバーのミュートを解除しました。",
            description=f"{ctx.author.mention}さんが{member.mention}さんのミュートを解除しました。",
            color=0x3498DB,
        )
        mute.set_thumbnail(url=member.avatar.url)
        await ctx.reply(embed=mute)
        guild = ctx.guild
        for channel in guild.channels:
            await channel.set_permissions(member, overwrite=None)
    else:
        await ctx.reply("このコマンドを実行できるのは管理者のみです！")


@bot.command()
async def timer(ctx, number):
    async with ctx.typing():
        await asyncio.sleep(0)
    await ctx.reply(str(number) + "秒後にタイマーをセットしました！")
    await asyncio.sleep(int(number))
    await ctx.reply("ピピピピッ♪タイマーが終了しました！", mention_author=True)


@bot.command()
async def poll(ctx, about="question", *args):
    async with ctx.typing():
        await asyncio.sleep(0)
    emojis = ["1⃣", "2⃣", "3⃣", "4⃣"]
    cnt = len(args)
    message = discord.Embed(title=":bar_chart: " + about, colour=0x3498DB)
    if cnt <= len(emojis):
        for a in range(cnt):
            message.add_field(name=f"{emojis[a]}{args[a]}", value="** **", inline=False)
        msg = await ctx.reply(embed=message)
        for i in range(cnt):
            await msg.add_reaction(emojis[i])
    else:
        await ctx.send("回答項目は４つまでしか作れないの。ごめんね・・・。")


@bot.command()
async def rect(ctx, about="募集", cnt=4, settime=10.0):
    async with ctx.typing():
        await asyncio.sleep(0)
    cnt, settime = int(cnt), float(settime)
    reaction_member = [">>>"]
    test = discord.Embed(title=about, colour=0x3498DB)
    test.add_field(name=f"あと{cnt}人 募集中！\n", value=None, inline=True)
    msg = await ctx.reply(embed=test)
    await msg.add_reaction("⏫")
    await msg.add_reaction("✖")

    def check(reaction, user):
        emoji = str(reaction.emoji)
        if not user.bot:
            return emoji == "⏫" or emoji == "✖"

    while len(reaction_member) - 1 <= cnt:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=settime, check=check)
        except asyncio.TimeoutError:
            await ctx.reply("人数が足りませんでした・・・。")
            break
        else:
            print(str(reaction.emoji))
            if str(reaction.emoji) == "⏫":
                reaction_member.append(user.name)
                cnt -= 1
                test = discord.Embed(title=about, colour=0x3498DB)
                test.add_field(name=f"あと{cnt}人 募集中！\n", value="\n".join(reaction_member), inline=True)
                await msg.edit(embed=test)
                if cnt == 0:
                    test = discord.Embed(title=about, colour=0x3498DB)
                    test.add_field(name=f"あと{cnt}人 募集中！\n", value="\n".join(reaction_member), inline=True)
                    await msg.edit(embed=test)
                    finish = discord.Embed(title=about, colour=0x3498DB)
                    finish.add_field(name="募集が完了しました！", value="\n".join(reaction_member), inline=True)
                    await ctx.reply(embed=finish)
            elif str(reaction.emoji) == "✖":
                if user.name in reaction_member:
                    reaction_member.remove(user.name)
                    cnt += 1
                    test = discord.Embed(title=about, colour=0x3498DB)
                    test.add_field(name=f"あと{cnt}人 募集中！\n", value="\n".join(reaction_member), inline=True)
                    await msg.edit(embed=test)
                else:
                    pass
        await msg.remove_reaction(str(reaction.emoji), user)


@bot.command()
async def embed(ctx, title="タイトル", text="テキスト"):
    async with ctx.typing():
        await asyncio.sleep(0)
    embed = discord.Embed(title=title, description=text, colour=0x3498DB)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.replace(format="png").url)
    await ctx.reply(embed=embed)


@bot.command()
async def calcu(ctx, left="1", way="+", right="1"):
    async with ctx.typing():
        await asyncio.sleep(0)
    if way == "+":
        answer1 = int(left) + int(right)
        await ctx.reply(answer1)
    elif way == "-":
        answer2 = int(left) - int(right)
        await ctx.reply(answer2)
    elif way == "×":
        answer3 = int(left) * int(right)
        await ctx.reply(answer3)
    elif way == "÷":
        answer4 = int(left) / int(right)
        await ctx.reply(answer4)
    else:
        answer1 = int(left) + int(right)
        await ctx.reply(answer1)


# -----«コマンド-データ»-------------------------


@bot.command()
async def time(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    now = datetime.datetime.now()
    date_and_time = now.strftime("%m月%d日 %H:%M")
    await ctx.reply(f"現在の時刻は{date_and_time}です！")


@bot.command()
async def detail(ctx, command="コマンド名"):
    async with ctx.typing():
        await asyncio.sleep(0)
    if command == "help":
        embed = discord.Embed(title="DETAIL-help", description="困ったときはを表示します。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/859408401419599882/859409365140635688/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "list":
        embed = discord.Embed(title="DETAIL-list", description="コマンドリストを表示します。", colour=0x3498DB)
        embed.set_footer(text="リアクションページを使用できます。")
        embed.set_image(
            url="https://media.discordapp.net/attachments/859408401419599882/859409537252327434/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "prof":
        embed = discord.Embed(title="DETAIL-prof", description="CuBOTのプロフィールを表示します。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829292378241105950/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "ping":
        embed = discord.Embed(title="DETAIL-ping", description="CuBOTのping値を表示します。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829292685457621032/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "kick":
        embed = discord.Embed(title="DETAIL-kick", description="ユーザーをキックします。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!kick [ユーザー名]", inline=True)
        embed.set_footer(text="このコマンドを実行できるのは管理者のみです。")
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829293398682763284/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "ban":
        embed = discord.Embed(title="DETAIL-ban", description="ユーザーをBANします。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!ban [ユーザー名]", inline=True)
        embed.set_footer(text="このコマンドを実行できるのは管理者のみです。")
        embed.set_image(
            url="https://images-ext-2.discordapp.net/external/9S1B_5tzfHj-E7W1P92sT9uoMJgLyCIPoKUEWM2J338/"
            "https/media.discordapp.net/attachments/826804140398215218/829293782284894258/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "unban":
        embed = discord.Embed(title="DETAIL-unban", description="ユーザーのBANを解除します。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!unban [ユーザーID]", inline=True)
        embed.set_footer(text="このコマンドを実行できるのは管理者のみです。")
        embed.set_image(
            url="https://media.discordapp.net/attachments/826803343669854229/859407084339986452/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "timer":
        embed = discord.Embed(title="DETAIL-timer", description="タイマーをセットします。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!timer [秒数]", inline=True)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829292950793879552/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "poll":
        embed = discord.Embed(title="DETAIL-poll", description="投票パネルを作成します。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!poll [議題] [項目1] [項目2] [項目3] [項目4]", inline=True)
        embed.set_footer(text="選択肢は4つまで作成できます。")
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829293852077588500/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "rect":
        embed = discord.Embed(title="DETAIL-rect", description="募集パネルを作成します。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!rect [募集内容] [募集人数] [締め切り時間]", inline=True)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829293919971967016/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "embed":
        embed = discord.Embed(title="DETAIL-embed", description="Embedパネルを作成します。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!embed [タイトル] [説明]", inline=True)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829294113576452096/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "calcu":
        embed = discord.Embed(title="DETAIL-calcu", description="計算をします。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!calcu [数値1] [算法] [数値2]", inline=True)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/844209477657559060/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "time":
        embed = discord.Embed(title="DETAIL-time", description="現在時刻を表示します。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829294591185256518/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "detail":
        embed = discord.Embed(title="DETAIL-detail", description="各コマンドの詳細を表示します。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!detail [コマンド名]", inline=True)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829295373410631721/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "invite":
        embed = discord.Embed(title="DETAIL-invite", description="招待リンクの総使用数を算出します。", colour=0x3498DB)
        embed.add_field(name="使い方", value="Cu!invite [ユーザー名]", inline=True)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/844209266934939680/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "fortune":
        embed = discord.Embed(title="DETAIL-fortune", description="おみくじが引けます。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829296454110674954/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "rps":
        embed = discord.Embed(title="DETAIL-rps", description="じゃんけんができます。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829296691290308618/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "dice":
        embed = discord.Embed(title="DETAIL-dice", description="サイコロを振れます。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829296842063347742/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "pun":
        embed = discord.Embed(title="DETAIL-pun", description="ダジャレが聞けます。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829297151213043722/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "cquiz":
        embed = discord.Embed(title="DETAIL-cquiz", description="暗算クイズができます。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/829297392356556820/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "coin":
        embed = discord.Embed(title="DETAIL-coin", description="コイントスができます。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/830784293148033042/unknown.png"
        )
        await ctx.reply(embed=embed)
    elif command == "slot":
        embed = discord.Embed(title="DETAIL-slot", description="スロットができます。", colour=0x3498DB)
        embed.set_image(
            url="https://media.discordapp.net/attachments/826804140398215218/832000993205682206/unknown.png"
        )
        await ctx.reply(embed=embed)


@bot.command()
async def invite(ctx, member: discord.Member = None):
    async with ctx.typing():
        await asyncio.sleep(0)
    if member is None:
        user = ctx.author
    else:
        user = member
    total_invites = 0
    for i in await ctx.guild.invites():
        if i.inviter == user:
            total_invites += i.uses
    embed = discord.Embed(
        title="招待リンクの使用数", description=f"{user.mention}さんは**{total_invites}人**のメンバーを招待しました！", color=0x3498DB
    )
    await ctx.reply(embed=embed)


# -----«コマンド-バラエティ»-------------------------


@bot.command()
async def fortune(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    taiki = discord.Embed(title="おみくじ", description="チケットをクリックしておみくじを引きましょう！", color=0x3498DB)
    taiki.set_thumbnail(url=ctx.author.avatar.url)
    unsei = random.choice(("大吉", "中吉", "小吉", "吉", "凶", "大凶"))
    luckycmd = random.choice(("fortune", "rps", "dice", "pun", "cquiz", "coin", "slot", "totusi"))
    akekka = discord.Embed(
        title="おみくじ",
        description=f"{ctx.author.mention}さんの今日の運勢は！\n`運勢`：{unsei}\n`ラッキーコマンド`：Cu!{luckycmd}",
        color=0x3498DB,
    )
    akekka.set_thumbnail(url=ctx.author.avatar.url)
    message = await ctx.reply(embed=taiki)
    await message.add_reaction("🎫")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["🎫"]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "🎫":
                await message.edit(embed=akekka)
                await message.clear_reactions()
        except asyncio.TimeoutError:
            await message.clear_reactions()
            break


@bot.command()
async def rps(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    global result, judge
    await ctx.reply("最初はぐー！じゃんけん・・・")
    jkbot = random.choice(("ぐー", "ちょき", "ぱー"))
    draw = "引き分けだよ！運命かなぁ・・・！"
    wn = "負けちゃった～・・・。君強いね～！"
    lst = "やったー！勝てた～♪"

    def jankencheck(m):
        return (m.author == ctx.author) and (m.content in ["ぐー", "ちょき", "ぱー"])

    reply = await bot.wait_for("message", check=jankencheck)
    if reply.content == jkbot:
        judge = draw
    else:
        if reply.content == "ぐー":
            if jkbot == "ちょき":
                judge = wn
            else:
                judge = lst
        elif reply.content == "ちょき":
            if jkbot == "ぱー":
                judge = wn
            else:
                judge = lst
        else:
            if jkbot == "ぐー":
                judge = wn
            else:
                judge = lst
    await ctx.reply(jkbot)
    await ctx.reply(judge)


@bot.command()
async def dice(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    dice = random.randint(1, 6)
    embed = discord.Embed(title="サイコロ", description="[出目] " + str(dice), colour=0x3498DB)
    embed.set_thumbnail(
        url="https://smilescience.up.seesaa.net/image/E382B5E382A4E382B3E383ADE381AEE79BAEE5B08F_"
        + str(dice)
        + "-thumbnail2.png"
    )
    await ctx.reply(embed=embed)


@bot.command()
async def pun(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    pun = random.choice(
        (
            "ですます口調で済ます区長",
            "象さんが増産",
            "大根持って大混乱",
            "ジャムおじさんがジャムを持参",
            "忍者は何人じゃ",
            "家康の家安い",
            "占いの本は売らない",
            "戦車を洗車する",
            "鶏肉は太りにくい",
            "明治のイメージ",
            "分かり易い和歌",
            "嫁の字が読めない",
            "校長先生絶好調",
            "モノレールにも乗れーる",
            "カツラが滑落",
            "カツオに活を入れる",
            "汗かいて焦った",
            "高3が降参",
        )
    )
    await ctx.reply(pun + "！なんつって～笑")


@bot.command()
async def cquiz(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    n1 = random.randint(0, 300)
    n2 = random.randint(0, 300)
    answer = n1 + n2
    await ctx.reply(str(n1) + "+" + str(n2) + " = ?")

    def answercheck(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel and m.content.isdigit()

    try:
        waitresp = await bot.wait_for("message", timeout=30, check=answercheck)
    except asyncio.TimeoutError:
        await ctx.reply("時間切れ！正解は " + str(answer) + "でした！")
    else:
        if waitresp.content == str(answer):
            await ctx.reply("正解です！お見事！")
        else:
            await ctx.reply("不正解！正解は" + str(answer) + "でした！")


@bot.command()
async def coin(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    surface = random.choice(("表", "裏"))
    if surface == "表":
        embed = discord.Embed(title="コイントス", description="**表**が出ました！", color=0x3498DB)
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/830673701564317727/830771939831971860/"
            "FavgDW3fhU7oNzgJY98FDvBsv4f8DMemdePw7rqgAAAAASUVORK5CYII.png"
        )
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="コイントス", description="**裏**が出ました！", color=0x3498DB)
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/830673701564317727/830763529005957130/toAAAAASUVORK5CYII.png"
        )
        await ctx.reply(embed=embed)


@bot.command()
async def slot(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    A = random.choice((":one:", ":two:", ":three:"))
    B = random.choice((":one:", ":two:", ":three:"))
    C = random.choice((":one:", ":two:", ":three:"))
    embed = discord.Embed(title="スロット", description="| " + A + " | " + B + " | " + C + " |", color=0x3498DB)
    await ctx.reply(embed=embed)
    if A == B == C:
        await ctx.reply("当選おめでとう！")


@bot.command()
async def totusi(ctx, *, arg="突然の死"):
    async with ctx.typing():
        await asyncio.sleep(0)
    ue = "人" * len(arg)
    sita = "^Y" * len(arg)
    await ctx.reply("＿人" + ue + "人＿\n＞　" + arg + "　＜\n￣^Y" + sita + "^Y￣")

#-----«コマンド-管理»-------------------------
@bot.command()
async def slist(ctx, a=None):
    if ctx.author.id == 798439010594717737:
        if a == "id":
            guild_list = "\n".join(f"{guild.name} {guild.id}" for guild in bot.guilds)
            await ctx.reply(guild_list)
        else:
            guild_list = "\n".join(f"{guild.name}" for guild in bot.guilds)
            await ctx.reply(guild_list)
            
            
@bot.command()
async def restart(ctx):
    if ctx.author.id == 798439010594717737:
        await ctx.reply("再起動を実行中です・・・")
        restart_bot()
        
#-----«コマンド-試作»-------------------------
@bot.command()
async def join(ctx):
    vc = ctx.author.voice

    if (not vc) or (not vc.channel):
        await ctx.send("ボイスチャンネルに参加してからコマンドを実行してね！")
        return
    channel = vc.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    vc = ctx.message.guild.voice_client
    if not vc:
        await ctx.send("ボイスチャンネルに参加していないよ！")
        return
    await vc.disconnect()
    await ctx.send("ボイスチャンネルから切断しました。")


@bot.command()
async def detailsisaku(ctx, dtype=None):
    async with ctx.typing():
        await asyncio.sleep(0)
    dhelp = discord.Embed(title="DETAIL-help", description="困ったときはを表示します。", colour=0x3498DB)
    dhelp.set_image(url="https://media.discordapp.net/attachments/859408401419599882/859409365140635688/unknown.png")
    dlist = discord.Embed(title="DETAIL-list", description="コマンドリストを表示します。", colour=0x3498DB)
    dlist.set_footer(text="リアクションページを使用できます。")
    dlist.set_image(url="https://media.discordapp.net/attachments/859408401419599882/859409537252327434/unknown.png")
    dprof = discord.Embed(title="DETAIL-prof", description="CuBOTのプロフィールを表示します。", colour=0x3498DB)
    dprof.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829292378241105950/unknown.png")
    dping = discord.Embed(title="DETAIL-ping", description="CuBOTのping値を表示します。", colour=0x3498DB)
    dping.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829292685457621032/unknown.png")
    dkick = discord.Embed(title="DETAIL-kick", description="ユーザーをキックします。", colour=0x3498DB)
    dkick.add_field(name="使い方", value="Cu!kick [ユーザー名]", inline=True)
    dkick.set_footer(text="このコマンドを実行できるのは管理者のみです。")
    dkick.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829293398682763284/unknown.png")
    dban = discord.Embed(title="DETAIL-ban", description="ユーザーをBANします。", colour=0x3498DB)
    dban.add_field(name="使い方", value="Cu!ban [ユーザー名]", inline=True)
    dban.set_footer(text="このコマンドを実行できるのは管理者のみです。")
    dban.set_image(
        url="https://images-ext-2.discordapp.net/external/9S1B_5tzfHj-E7W1P92sT9uoMJgLyCIPoKUEWM2J338/"
        "https/media.discordapp.net/attachments/826804140398215218/829293782284894258/unknown.png"
    )
    dunban = discord.Embed(title="DETAIL-unban", description="ユーザーのBANを解除します。", colour=0x3498DB)
    dunban.add_field(name="使い方", value="Cu!unban [ユーザーID]", inline=True)
    dunban.set_footer(text="このコマンドを実行できるのは管理者のみです。")
    dunban.set_image(url="https://media.discordapp.net/attachments/826803343669854229/859407084339986452/unknown.png")
    dmute = discord.Embed(title="DETAIL-mute", description="ユーザーをミュートします。", colour=0x3498DB)
    dmute.add_field(name="使い方", value="Cu!mute [ユーザー名]", inline=True)
    dmute.set_footer(text="このコマンドを実行できるのは管理者のみです。")
    dmute.set_image(
        url="https://images-ext-2.discordapp.net/external/9S1B_5tzfHj-E7W1P92sT9uoMJgLyCIPoKUEWM2J338/"
        "https/media.discordapp.net/attachments/826804140398215218/829293782284894258/unknown.png"
    )
    dunmute = discord.Embed(title="DETAIL-unmute", description="ユーザーのミュートを解除します。", colour=0x3498DB)
    dunmute.add_field(name="使い方", value="Cu!unmute [ユーザー名]", inline=True)
    dunmute.set_footer(text="このコマンドを実行できるのは管理者のみです。")
    dunmute.set_image(url="https://media.discordapp.net/attachments/826803343669854229/859407084339986452/unknown.png")
    dtimer = discord.Embed(title="DETAIL-timer", description="タイマーをセットします。", colour=0x3498DB)
    dtimer.add_field(name="使い方", value="Cu!timer [秒数]", inline=True)
    dtimer.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829292950793879552/unknown.png")
    dpoll = discord.Embed(title="DETAIL-poll", description="投票パネルを作成します。", colour=0x3498DB)
    dpoll.add_field(name="使い方", value="Cu!poll [議題] [項目1] [項目2] [項目3] [項目4]", inline=True)
    dpoll.set_footer(text="選択肢は4つまで作成できます。")
    dpoll.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829293852077588500/unknown.png")
    drect = discord.Embed(title="DETAIL-rect", description="募集パネルを作成します。", colour=0x3498DB)
    drect.add_field(name="使い方", value="Cu!rect [募集内容] [募集人数] [締め切り時間]", inline=True)
    drect.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829293919971967016/unknown.png")
    dembed = discord.Embed(title="DETAIL-embed", description="Embedパネルを作成します。", colour=0x3498DB)
    dembed.add_field(name="使い方", value="Cu!embed [タイトル] [説明]", inline=True)
    dembed.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829294113576452096/unknown.png")
    dcalcu = discord.Embed(title="DETAIL-calcu", description="計算をします。", colour=0x3498DB)
    dcalcu.add_field(name="使い方", value="Cu!calcu [数値1] [算法] [数値2]", inline=True)
    dcalcu.set_image(url="https://media.discordapp.net/attachments/826804140398215218/844209477657559060/unknown.png")
    dtime = discord.Embed(title="DETAIL-time", description="現在時刻を表示します。", colour=0x3498DB)
    dtime.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829294591185256518/unknown.png")
    ddetail = discord.Embed(title="DETAIL-detail", description="各コマンドの詳細を表示します。", colour=0x3498DB)
    ddetail.add_field(name="使い方", value="Cu!detail [コマンド名]", inline=True)
    ddetail.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829295373410631721/unknown.png")
    dinvite = discord.Embed(title="DETAIL-invite", description="招待リンクの総使用数を算出します。", colour=0x3498DB)
    dinvite.add_field(name="使い方", value="Cu!invite [ユーザー名]", inline=True)
    dinvite.set_image(url="https://media.discordapp.net/attachments/826804140398215218/844209266934939680/unknown.png")
    dfortune = discord.Embed(title="DETAIL-fortune", description="おみくじが引けます。", colour=0x3498DB)
    dfortune.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829296454110674954/unknown.png")
    drps = discord.Embed(title="DETAIL-rps", description="じゃんけんができます。", colour=0x3498DB)
    drps.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829296691290308618/unknown.png")
    ddice = discord.Embed(title="DETAIL-dice", description="サイコロを振れます。", colour=0x3498DB)
    ddice.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829296842063347742/unknown.png")
    dpun = discord.Embed(title="DETAIL-pun", description="ダジャレが聞けます。", colour=0x3498DB)
    dpun.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829297151213043722/unknown.png")
    dcquiz = discord.Embed(title="DETAIL-cquiz", description="暗算クイズができます。", colour=0x3498DB)
    dcquiz.set_image(url="https://media.discordapp.net/attachments/826804140398215218/829297392356556820/unknown.png")
    dcoin = discord.Embed(title="DETAIL-coin", description="コイントスができます。", colour=0x3498DB)
    dcoin.set_image(url="https://media.discordapp.net/attachments/826804140398215218/830784293148033042/unknown.png")
    dslot = discord.Embed(title="DETAIL-slot", description="スロットができます。", colour=0x3498DB)
    dslot.set_image(url="https://media.discordapp.net/attachments/826804140398215218/832000993205682206/unknown.png")
    dtotusi = discord.Embed(title="DETAIL-totusi", description="突然の死AAを作成します。", colour=0x3498DB)
    dtotusi.add_field(name="使い方", value="Cu!totusi [message]", inline=True)
    dtotusi.set_image(url="https://media.discordapp.net/attachments/826804140398215218/838268795982053406/unknown.png")
    dtotusi.set_footer(text="半角テキスト、絵文字、空白等は対応していません。")
    pages = [
        dhelp,
        dlist,
        dprof,
        dping,
        dkick,
        dban,
        dunban,
        dmute,
        dunmute,
        dtimer,
        dpoll,
        drect,
        dembed,
        dcalcu,
        dtime,
        ddetail,
        dinvite,
        dfortune,
        drps,
        ddice,
        dpun,
        dcquiz,
        dcoin,
        dslot,
        dtotusi,
    ]
    page = 0
    message = await ctx.reply(embed=pages[page])
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "▶️" and page != 22:
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


@bot.command()
async def clear(ctx, num):
    if ctx.author.guild_permissions.administrator:
        async for message in ctx.channel.history(limit=int(num) + 1):
            await message.delete(delay=1.2)
            await ctx.send("実行しました！")
    else:
        await ctx.reply("このコマンドを実行できるのは管理者のみです！")


@bot.command()
async def sinfo(ctx):
    async with ctx.typing():
        await asyncio.sleep(0)
    guild = ctx.guild
    name = str(ctx.guild.name)
    sid = str(ctx.guild.id)
    owner = str(ctx.guild.owner.id)
    # description = str(ctx.guild.description)
    region = str(ctx.guild.region)
    mcount = str(ctx.guild.member_count)
    ucount = str(sum(1 for member in guild.members if not member.bot))
    bcount = str(sum(1 for member in guild.members if member.bot))
    tchannels = len(ctx.guild.text_channels)
    vchannels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = tchannels + vchannels
    icon = str(ctx.guild.icon.url)
    embed = discord.Embed(title="サーバー情報", description="サーバーの詳細情報です♪", color=0x3498DB)
    embed.set_thumbnail(url=icon)
    embed.add_field(
        name="📋 》一般", value=f"`サーバー名`：{name}\n`サーバーID`：{sid}\n`オーナー`：<@{owner}>\n`地域`：{region}", inline=False
    )
    embed.add_field(name="👤 》メンバー", value=f"`メンバー数`：{mcount}\n`ユーザー数`：{ucount}\n`BOT数`：{bcount}", inline=False)
    embed.add_field(
        name="💬 》チャンネル",
        value=f"`チャンネル数`：{channels}\n`テキストチャンネル数`：{tchannels}\n`ボイスチャンネル数`：{vchannels}\n`カテゴリー数`：{categories}",
        inline=False,
    )
    await ctx.send(embed=embed)

    
@bot.command()
async def kusa(ctx, num):
    if ctx.author.guild_permissions.administrator:
        async for message in ctx.channel.history(limit=int(num) + 1):
            if message.content == "草":
                await message.delete(delay=1.2)
        await ctx.send("草刈りぶううううううううううんｗ")
    else:
        await ctx.reply("このコマンドを実行できるのは管理者のみです！")
        
#-----«コマンド-スラッシュコマンド»-------------------------
@bot.slash_command(description="困ったときはを表示します。")
async def help(ctx):
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
    await ctx.send(embed=embed, mention_author=False)
    
  

@bot.slash_command(description="コマンドリストを表示します。")
async def list(ctx, type=None):
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
        name=":video_game: 》バラエティ", value="`fortune` `rps` `dice` `pun` `cquiz` `coin` `slot` `totusi`", inline=False
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
    message = await ctx.send(embed=pages[page], mention_author=False)
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)
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

bot.run(token)
