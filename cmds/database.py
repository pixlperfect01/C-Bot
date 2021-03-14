import discord
from discord.ext import commands, tasks
import asyncio
from json import dumps as j_enc, loads as j_dec
from glob import glob
from types import Player

class Database(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = {}
        self.items = j_dec(open("data/items.json").read())
    def cinit(self):
        for f in glob("data/users/*.json"):
            d = j_dec(f.read())
