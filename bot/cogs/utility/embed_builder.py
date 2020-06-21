import discord
import toml

CONFIG = toml.load('./config.toml')
COLOR = CONFIG['embed']['color']

def create_embed(title, description, author, bot):
    name = author.nick if author.nick else author.name

    embed = discord.Embed(
        title=title,
        description=description,
        color=COLOR)
    embed.set_author(name=name, icon_url=author.avatar_url)
    embed.set_footer(icon_url=bot.user.avatar_url, text=f"This service is brought to you by {bot.user.name}.")

    return embed

def create_raid_embed(description, timestamp, author, bot):
    name = author.nick if author.nick else author.name

    embed = discord.Embed(
        title=f"{name} is planning a raid:",
        description=description,
        color=COLOR)
    embed.set_author(name=name, icon_url=author.avatar_url)
    # embed.set_thumbnail(url="") maybe some raid-icon?
    embed.set_footer(icon_url=bot.user.avatar_url, text="This raid starts:")
    embed.timestamp = timestamp

    return embed
