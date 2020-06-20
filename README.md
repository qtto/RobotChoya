# Robot Choya

Robot Choya is a Discord bot to help organize raids for [Wipe], written using [discord.py](https://github.com/Rapptz/discord.py).

## Setting up
Clone the repository
```bash
git clone https://github.com/qtto/RobotChoya.git
```

Optional: create a virtual environment and activate it.
```bash
python -m venv /path/to/venv
source /path/to/venv/bin/activate
```


Use [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip install -r requirements.txt
```

## Running the bot
[Create a bot account](https://discordpy.readthedocs.io/en/latest/discord.html) and create `config.toml`.
```bash
cp config.toml.example config.toml
```

Make sure to add your client secret to config.toml.

Finally, run the bot.
```bash
cd bot
python bot.py
```

