import discord
from discord.ext import commands, tasks
import asyncio

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="help",aliases=["h"])
    async def help(self, ctx):
        e = discord.Embed(title="Help")
        for k in self.bot.cogs:
            v = self.bot.get_cog(k)
            e.add_field(name=k, value=", ".join([c.name for c in v.get_commands()]))
        await ctx.send(embed=e)
    @commands.command(name="proflie",aliases=["prof"])
    async def profile(self, ctx, *, user:discord.User=None):
        if user is None:
            user = ctx.author
        e = discord.Embed(title=user.display_name)
