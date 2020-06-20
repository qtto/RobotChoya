import discord
from discord.ext import commands

class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_connect(self):
        presence = "to your commands. Ping @" + self.bot.user.name + " for help."
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=presence))


    @commands.Cog.listener()
    async def on_message(self, message):
        for user in message.mentions:
            if user == self.bot.user:
                await message.channel.send("I got pinged")

def setup(bot):
    bot.add_cog(About(bot))
