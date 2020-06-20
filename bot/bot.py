#!/usr/bin/python3

import discord
from discord.ext import commands
import toml

# load config and environment variables (e.g. client secret)
CONFIG = toml.load('./config.toml')
TOKEN = toml.load('./token.toml')['token']['discord_token']

GUILD = CONFIG['env']['discord_guild']

# read active extensions (cogs)
extensions = CONFIG['bot']['extensions']

# create the bot class
class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f'Logged in as {self.user.name}.')

        for guild in self.guilds:
            print(f'Connected to {guild.name}.')

# initialize an instance of the bot and set parameters
bot = Bot(command_prefix=CONFIG['bot']['prefix'],
          description=CONFIG['bot']['description'])

# load extension modules and start the bot
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print(f'Loaded extension {extension}.')
        except Exception as e:
            print(f'Failed to load extension {extension}: {e}')

    bot.run(TOKEN, bot=True, reconnect=True)
