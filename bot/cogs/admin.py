import datetime
import discord
import os
from discord.ext import commands

"""
Some simple commands for bot maintenance.
"""

class Admin(commands.Cog):
    """Several admin commands"""
    def __init__(self, bot):
        self.bot = bot
        self.startup = datetime.datetime.now()


    def timedelta_str(self, dt):
        """Converts time to a readable string."""
        days = dt.days
        hours, r = divmod(dt.seconds, 3600)
        minutes, sec = divmod(r, 60)

        return f"{days} days, {hours} hours, {minutes} minutes and {sec} seconds."


    @commands.command()
    async def extensions(self, ctx):
        """Lists active extensions."""
        active_ext = "\n".join(tuple(self.bot.extensions))
        await ctx.send(active_ext)


    @commands.command()
    async def reload(self, ctx, extension_name: str):
        """Reloads an extension."""
        try:
            self.bot.reload_extension(extension_name)
        except Exception as e:
            await ctx.send(f"Error reloading {extension_name}: {e}.")
            return
        await ctx.send(f"Reloaded {extension_name}.")


    @commands.command()
    async def uptime(self, ctx):
        """Prints bot uptime."""
        delta = datetime.datetime.now()-self.startup
        delta_str = self.timedelta_str(delta)
        await ctx.send(f"Uptime: {delta_str}")


    @commands.command()
    async def ping(self, ctx):
        """Gives you a good ole pong!"""
        ping = int(self.bot.latency*1000)
        await ctx.send(f"Pong! (took {ping} ms)")


def setup(bot):
    bot.add_cog(Admin(bot))
    