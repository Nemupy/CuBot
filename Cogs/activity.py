import discord
from discord.ext import commands
from discord.http import Route

class AppCmdGeneral(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        
    @commands.command()
    async def youtube(self,ctx):
        voice = ctx.author.voice
        if not voice:
            return await ctx.send('You have to be in a voice channel to use this command.')
        r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)
        payload = {
            'max_age': 0,
            'target_type': 2,
                'target_application_id': 755600276941176913
        }
        try:
            code = (await self.bot.http.request(r, json=payload))['code']
        except discord.Forbidden:
            return await ctx.send('I Need the `Create Invite` permission.')
        await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136))
        
    @commands.command()
    async def betrayal(self,ctx):
        voice = ctx.author.voice
        if not voice:
            return await ctx.send('You have to be in a voice channel to use this command.')
        r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)
        payload = {
            'max_age': 0,
            'target_type': 2,
                'target_application_id': 773336526917861400
        }
        try:
            code = (await self.bot.http.request(r, json=payload))['code']
        except discord.Forbidden:
            return await ctx.send('I Need the `Create Invite` permission.')
        await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136)) 
        
    @commands.command()
    async def fishington(self,ctx):
        voice = ctx.author.voice
        if not voice:
            return await ctx.send('You have to be in a voice channel to use this command.')
        r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)
        payload = {
            'max_age': 0,
            'target_type': 2,
                'target_application_id': 814288819477020702
        }
        try:
            code = (await self.bot.http.request(r, json=payload))['code']
        except discord.Forbidden:
            return await ctx.send('I Need the `Create Invite` permission.')
        await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136))
        
    @commands.command()
    async def poker(self,ctx):
        voice = ctx.author.voice
        if not voice:
            return await ctx.send('You have to be in a voice channel to use this command.')
        r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)
        payload = {
            'max_age': 0,
            'target_type': 2,
                'target_application_id': 755827207812677713
        }
        try:
            code = (await self.bot.http.request(r, json=payload))['code']
        except discord.Forbidden:
            return await ctx.send('I Need the `Create Invite` permission.')
        await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136))
        
    @commands.command()
    async def chess(self,ctx):
        voice = ctx.author.voice
        if not voice:
            return await ctx.send('You have to be in a voice channel to use this command.')
        r = Route('POST', '/channels/{channel_id}/invites', channel_id=voice.channel.id)
        payload = {
            'max_age': 0,
            'target_type': 2,
                'target_application_id': 832012774040141894
        }
        try:
            code = (await self.bot.http.request(r, json=payload))['code']
        except discord.Forbidden:
            return await ctx.send('I Need the `Create Invite` permission.')
        await ctx.send(embed=discord.Embed(description=f'[Click here!](https://discord.gg/{code})', color=0x2F3136))
        
def setup(bot):
    return bot.add_cog(AppCmdGeneral(bot))
