import discord
from json import dumps as j_enc, loads as j_dec
DEFAULT_DATA = j_dec(open("data/default_profile.json").read())
class Player:
    def __init__(self, u:discord.User, data:dict=None):
        self.user = u
        if data is None:
            self.reset_data()
        else:
            self.data = data
    def reset_data(self):
        self.data = DEFAULT_DATA
