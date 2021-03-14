import discord
from discord.ext import commands, tasks
import cmds



bot = commands.Bot("//", None)

@bot.event
async def on_ready():
    global bot
    bot.get_cog('Database').cinit()

bot.add_cog(cmds.Misc(bot))
bot.add_cog(cmds.Database(bot))
bot.run(open("info.txt","r").read())
