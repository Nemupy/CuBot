import discord
from discord.ext import commands
import asyncio
import random

class AppCmdVariety(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def fortune(self,ctx):
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
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60, check=check)
                if str(reaction.emoji) == "🎫":
                    await message.edit(embed=akekka)
                    await message.clear_reactions()
            except asyncio.TimeoutError:
                await message.clear_reactions()
                break

    @commands.command()
    async def rps(self,ctx):
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

        reply = await self.bot.wait_for("message", check=jankencheck)
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

    @commands.command()
    async def dice(self,ctx):
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

    @commands.command()
    async def pun(self,ctx):
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

    @commands.command()
    async def cquiz(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        n1 = random.randint(0, 300)
        n2 = random.randint(0, 300)
        answer = n1 + n2
        await ctx.reply(str(n1) + "+" + str(n2) + " = ?")

        def answercheck(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel and m.content.isdigit()

        try:
            waitresp = await self.bot.wait_for("message", timeout=30, check=answercheck)
        except asyncio.TimeoutError:
            await ctx.reply("時間切れ！正解は " + str(answer) + "でした！")
        else:
            if waitresp.content == str(answer):
                await ctx.reply("正解です！お見事！")
            else:
                await ctx.reply("不正解！正解は" + str(answer) + "でした！")

    @commands.command()
    async def coin(self,ctx):
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

    @commands.command()
    async def slot(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        A = random.choice((":one:", ":two:", ":three:"))
        B = random.choice((":one:", ":two:", ":three:"))
        C = random.choice((":one:", ":two:", ":three:"))
        embed = discord.Embed(title="スロット", description="| " + A + " | " + B + " | " + C + " |", color=0x3498DB)
        await ctx.reply(embed=embed)
        if A == B == C:
            await ctx.reply("当選おめでとう！")

    @commands.command()
    async def totusi(self,ctx, *, arg="突然の死"):
        async with ctx.typing():
            await asyncio.sleep(0)
        ue = "人" * len(arg)
        sita = "^Y" * len(arg)
        await ctx.reply("＿人" + ue + "人＿\n＞　" + arg + "　＜\n￣^Y" + sita + "^Y￣")

def setup(bot):
    return bot.add_cog(AppCmdVariety(bot))
