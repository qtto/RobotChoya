import discord, toml
import datetime
from datetime import datetime

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

def create_lfg_embed(json, author, bot):
    name = author.nick if author.nick else author.name
    start_date = datetime.fromisoformat(json['start_date'])
    end_date = datetime.fromisoformat(json['end_date'])

    embed = discord.Embed(
        title=f"{json['event_title']} ({get_duration(end_date-start_date)})",
        description=f"Start:{start_date}\nEnd:{end_date}",
        color=COLOR)
    embed.set_author(name=name, icon_url=author.avatar_url)
    # embed.set_thumbnail(url="") maybe some raid-icon?
    embed.set_footer(icon_url=bot.user.avatar_url, text="This raid starts:")
    embed.timestamp = datetime.fromisoformat(json['start_date'])

    for activity in json['activities']:
        table = create_table(activity['participants'])
        value = "```prolog\n" + table + "\n```"
        embed.add_field(name=activity['title'], value=value, inline=False)


    return embed

def create_table(participants):
    entries = ["user_id", "role", "mechanic"]
    max_length = []
    for entry in entries:
        max_length.append(len(entry))
    for participant in participants:
        for entry in entries:
            participant[entry] = str(participant[entry])
            if (len(participant[entry]) > max_length[entries.index(entry)]):
                max_length[entries.index(entry)] = len(participant[entry])

    table = "╔" + ("═"*(max_length[0] + 4)) + \
            "╦" + ("═"*(max_length[1] + 4)) + \
            "╦" + ("═"*(max_length[2] + 4)) + "╗\n"
    table += "║  " + entries[0] + (" "*(max_length[0]-len(entries[0]))) + \
             "  ║  " + entries[1] + (" "*(max_length[1]-len(entries[1]))) + \
             "  ║  " + entries[2] + (" "*(max_length[2]-len(entries[2]))) + "  ║\n"
    table += "╠" + ("═"*(max_length[0] + 4)) + \
             "╬" + ("═"*(max_length[1] + 4)) + \
             "╬" + ("═"*(max_length[2] + 4)) + "╣\n"

    for participant in participants:
        table += "║  " + participant[entries[0]] + (" "*(max_length[0]-len(participant[entries[0]]))) + \
               "  ║  " + participant[entries[1]] + (" "*(max_length[1]-len(participant[entries[1]]))) + \
               "  ║  " + participant[entries[2]] + (" "*(max_length[2]-len(participant[entries[2]]))) + "  ║\n"

    table += "╚" + ("═"*(max_length[0] + 4)) + \
             "╩" + ("═"*(max_length[1] + 4)) + \
             "╩" + ("═"*(max_length[2] + 4)) + "╝"

    return table

def get_duration(timedelta):
    seconds = timedelta.seconds
    time = {"h": 0,
            "min": 0,
            "s": 0}
    while (seconds >= 3600):
        time[list(time.keys())[0]] = time.get(list(time.keys())[0]) + 1
        seconds-=3600
    while (seconds >= 60):
        time[list(time.keys())[1]] = time.get(list(time.keys())[1]) + 1
        seconds-=60
    time[list(time.keys())[2]] = seconds

    for index in range(0, len(time)):
        if (time.get(list(time.keys())[index]) != 0):
             string = f"{time.get(list(time.keys())[index])}{list(time.keys())[index]}"
             if (time.get(list(time.keys())[index + 1]) != 0):
                 string += f" {time.get(list(time.keys())[index + 1])}{list(time.keys())[index + 1]}"
             return string