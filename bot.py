import os
from random import randint, randrange, choice

import discord

client = discord.Client()
BOT_TOKEN = os.environ['BOT_TOKEN']


def say_hello():
    return "Hello! I am a bot. Type !help to see the available commands"


def get_help():
    description_lines = ''

    for command in possible_commands.keys():
        description_lines = description_lines + \
            f"\t**!{command}**: {possible_commands[command]['description']}" + "\n"

    return f"""The available commands are:
{description_lines}
    """


def get_random_config():
    config_dict = {
        "Map": choice(['The Skeld', 'MIRA HQ', 'Polus']),
        "Confirm Ejects": choice(["On", "Off"]),
        "Emergency Meetings": randint(0, 10),
        "Emergency Cooldown": randrange(15, 61, 5),
        "Discussion Time": randrange(30, 121, 15),
        "Voting Time": randrange(30, 151, 15),
        "Anonymous Votes": choice(["On", "Off"]),
        "Player Speed": randrange(2, 12, 1) / 4,
        "Cremate Vision": randrange(1, 16, 1) / 4,
        "Impostor Vision": randrange(1, 20, 1) / 4,
        "Kill Cooldown": randrange(30, 120, 5) / 2,
        "Kill Distance": choice(["Short", "Medium", "Long"]),
        "Visual Tasks": choice(["On", "Off"]),
        "Task Bar Updates": choice(["Always", "Meetings", "Never"]),
        "Common Tasks": randint(1, 2),
        "Long Tasks": randint(1, 3),
        "Short Tasks": randint(1, 5)
    }

    description_lines = ''

    for config in config_dict.keys():
        description_lines = description_lines + \
            f"\t**{config}**: {config_dict[config]}" + "\n"

    config_string = f"""Your random config is:
{description_lines}
    """

    return config_string


possible_commands = {
    'hello': {
        'description': "Get a salutation from the bot.",
        'execute': say_hello
    },
    'help': {
        'description': "Get the available commands with a short description",
        'execute': get_help
    },
    'random_settings': {
        'description': "Get a random set of settings for your game.",
        'execute': get_random_config
    }
}


def analyize_message(message):
    if message not in possible_commands.keys():
        return "Command not found. Type !help to see possible commands"

    return possible_commands[message]['execute']()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != 775113605363924992:
        return

    if message.content.startswith('!'):
        channel = message.channel
        response = analyize_message(message.content[1:])
        await channel.send(response)

client.run(BOT_TOKEN)
