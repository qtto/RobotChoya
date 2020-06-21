from discord.ext import commands
from ..utility.embed_builder import create_raid_embed
from datetime import datetime


class Lfg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lfg(self, ctx):

        author = ctx.message.author
        date = ctx.message.content[5:] # some basic command parsing, pls redo
        timestamp = datetime.fromisoformat(date)

        embed = create_raid_embed("Some sample text for now", timestamp, author, self.bot)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Lfg(bot))
