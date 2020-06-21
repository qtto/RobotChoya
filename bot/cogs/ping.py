from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Gives you a good ole pong"""
        ping = int(self.bot.latency*1000)
        await ctx.send(f"Pong! ({ping} ms)")

def setup(bot):
    bot.add_cog(Ping(bot))
