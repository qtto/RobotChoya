import discord
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        presence = "to your commands. Use -help for more information."
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=presence))

def setup(bot):
    bot.add_cog(About(bot))
