import discord
from discord.ext import commands
import asyncio

class AppCmdTool(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def kick(self,ctx, member: discord.Member, reason=None):
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

    @commands.command()
    async def ban(self,ctx, member: discord.Member, reason=None):
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

    @commands.command()
    async def unban(self,ctx, id: int):
        if ctx.author.guild_permissions.administrator:
            user = await self.bot.fetch_user(id)
            unban = discord.Embed(
                title="メンバーのBANを解除しました", description=f"{ctx.author.mention}さんが{user.mention}さんのBANを解除しました。",
                color=0x3498DB
            )
            unban.set_thumbnail(url=user.avatar.url)
            await ctx.reply(embed=unban)
            await ctx.guild.unban(user)
        else:
            await ctx.reply("このコマンドを実行できるのは管理者のみです！")

    @commands.command()
    async def mute(self,ctx, member: discord.Member):
        async with ctx.typing():
            await asyncio.sleep(0)
        if ctx.author.guild_permissions.administrator:
            mute = discord.Embed(
                title="メンバーをミュートしました。", description=f"{ctx.author.mention}さんが{member.mention}さんをミュートしました。",
                color=0x3498DB
            )
            mute.set_thumbnail(url=member.avatar.url)
            await ctx.reply(embed=mute)
            guild = ctx.guild
            for channel in guild.channels:
                await channel.set_permissions(member, send_messages=False)
        else:
            await ctx.reply("このコマンドを実行できるのは管理者のみです！")

    @commands.command()
    async def unmute(self,ctx, member: discord.Member):
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

    @commands.command()
    async def timer(self,ctx, number):
        async with ctx.typing():
            await asyncio.sleep(0)
        await ctx.reply(str(number) + "秒後にタイマーをセットしました！")
        await asyncio.sleep(int(number))
        await ctx.reply("ピピピピッ♪タイマーが終了しました！", mention_author=True)

    @commands.command()
    async def poll(self,ctx, about="question", *args):
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

    @commands.command()
    async def rect(self,ctx, about="募集", cnt=4, settime=10.0):
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
                reaction, user = await self.bot.wait_for("reaction_add", timeout=settime, check=check)
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

    @commands.command()
    async def embed(self,ctx, title="タイトル", text="テキスト"):
        async with ctx.typing():
            await asyncio.sleep(0)
        embed = discord.Embed(title=title, description=text, colour=0x3498DB)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.replace(format="png").url)
        await ctx.reply(embed=embed)

    @commands.command()
    async def calcu(self,ctx, left="1", way="+", right="1"):
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

def setup(bot):
    return bot.add_cog(AppCmdTool(bot))
