import discord
from discord.ext import commands
import traceback

class AppCmdEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_ready(self):
        servers = len(self.bot.guilds)
        members = 0
        for guild in self.bot.guilds:
            members += guild.member_count - 1
        await self.bot.change_presence(
            activity=discord.Activity(name=f"Cu!help | {str(servers)}servers | {str(members)}users", type=3)
        )

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        member_count = guild.member_count
        embed = discord.Embed(title="導入してくれてありがとう！",
                              description=f"<@826228756657078272>が導入されました。\nCuは{member_count}人目のユーザーです。",
                              color=0x3498DB)
        embed.set_thumbnail(
            url="https://images-ext-1.discordapp.net/external/bi88_iGaiR-z5Oc6L0OBqkgDkY1UMe7sIPX94aZu8RE/%3Fformat%3Djpg%26name%3Dlarge/https/pbs.twimg.com/media/EfWoupuUYAAwuTv?width=473&height=473")
        await guild.system_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        orig_error = getattr(error, "original", error)
        error_msg = "".join(traceback.TracebackException.from_exception(orig_error).format())
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
            await ctx.reply(embed=embed)
        else:
            embed = discord.Embed(
                title="エラー",
                description="予期せぬエラーが発生しました。\nこのエラーが多発する場合は[公式サーバー](https://discord.gg/RFPQmRnv2j)までお問い合わせください。\n```" + error_msg + "```",
                colour=0x3498DB,
            )
            await ctx.reply(embed=embed, mention_author=False)

    @commands.Cog.listener()
    async def on_member_join(self,member):
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

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        if member.guild.system_channel:
            embed = discord.Embed(title="また来てね！", description=f"{member.mention}さんが退室しました。", colour=0x3498DB)
            embed.set_thumbnail(url=member.avatar.url)
            await member.guild.system_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        # elif message.type == discord.MessageType.new_member:
        # await message.delete()
        # return
        elif self.bot.user.id in message.raw_mentions:
            await message.reply("お呼びでしょうか！お困りの際は`Cu!help`と送信してみて下さいね♪", mention_author=False)

def setup(bot):
    return bot.add_cog(AppCmdEvent(bot))
