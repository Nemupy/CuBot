import discord
from discord.ext import commands
import asyncio
import datetime

class AppCmdData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def time(self,ctx):
        async with ctx.typing():
            await asyncio.sleep(0)
        now = datetime.datetime.now()
        date_and_time = now.strftime("%m月%d日 %H:%M")
        await ctx.reply(f"現在の時刻は{date_and_time}です！")

    @commands.command()
    async def detail(self,ctx, command="コマンド名"):
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

    @commands.command()
    async def invite(self,ctx, member: discord.Member = None):
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

def setup(bot):
    return bot.add_cog(AppCmdData(bot))
