from discord.ext import commands
from ..utility.embed_builder import create_lfg_embed
import base64, zlib, json

class Lfg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lfg(self, ctx):

        compressed_decoded_string = ctx.message.content.split()[-1]
        json = zlib_parse(compressed_decoded_string)

        author = ctx.message.author
        embed = create_lfg_embed(json, author, self.bot)
        await ctx.send(embed = embed)

        #author = ctx.message.author
        #date = ctx.message.content[5:] # some basic command parsing, pls redo
        #timestamp = datetime.fromisoformat(date)

        #embed = create_lfg_embed("Some sample text for now", timestamp, author, self.bot)
        #await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Lfg(bot))

def zlib_parse(data):
    compressed_string = base64.b64decode(data)
    json_string = zlib.decompress(compressed_string)
    return json.loads(json_string)
