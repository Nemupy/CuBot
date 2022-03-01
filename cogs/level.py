import discord
from discord.ext import commands
import sqlite3

conn = sqlite3.connect("level.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS level(userid, level, exp)")


class AppCmdLevel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        cur.execute("SELECT * FROM level WHERE userid=?", (message.author.id,))
        data = cur.fetchone()
        if data is None:
            cur.execute("INSERT INTO level VALUES(?, ?, ?)",
                        (message.author.id, 1, 0))
            conn.commit()
            return
        cur.execute("UPDATE level set exp=? WHERE userid=?",
                    (data[2] + 1, message.author.id))
        conn.commit()
        cur.execute("SELECT * FROM level WHERE userid=?", (message.author.id,))
        data = cur.fetchone()
        if data[2] >= data[1] * 5:
            cur.execute("UPDATE level set level=?,exp=? WHERE userid=?",
                        (data[1] + 1, 0, message.author.id))
            conn.commit()

    @commands.command()
    async def rank(self, ctx, member: discord.Member = None):
        if member is None:
            user = ctx.author
        else:
            user = member
        cur.execute("SELECT * FROM level WHERE userid=?", (user.id,))
        data = cur.fetchone()
        if data is None:
            await ctx.send("ユーザーが登録されていません")
        else:
            embed = discord.Embed(
                title="レベル", description=f"`Level`：{data[1]}\n`Exp`：{data[2]}", color=0x3498DB)
            embed.set_thumbnail(url=user.avatar.url)
            await ctx.reply(embed=embed)

    @commands.command()
    async def top(self, ctx):
        r = {}
        cur.execute("SELECT * FROM level")
        for i in cur.fetchall():
            user = await self.bot.fetch_user(i[0])
            r[i[1]] = user.name
        rag = [i for i in r]
        rank = sorted(rag, reverse=True)
        embed = discord.Embed(
            title="トップ３", description="\n".join(f"{r[f]}" for f in rank))
        await ctx.send(embed=embed)


def setup(bot):
    return bot.add_cog(AppCmdLevel(bot))
