# TODO: REFACTOR
import os
from random import randint, randrange, choice

import discord

client = discord.Client()
intents = discord.Intents.reactions = True  # Needed to listen to reactions
BOT_TOKEN = os.getenv('BOT_TOKEN')
COMMAND_PREFIX = '!'


async def say_hello(received_message: discord.Message):
    salutation = "Hello! I am a bot. Type !help to see the available commands"
    await received_message.channel.send(salutation)


async def get_help(received_message: discord.Message):
    description_lines = ''

    for command in possible_commands.keys():
        description_lines = description_lines + \
            f"\t**!{command}**: {possible_commands[command]['description']}" + "\n"

    return f"""The available commands are:
{description_lines}
    """

    await received_message.channel.send(description_lines)


async def check_if_message_has_bot_reaction(message: discord.Message, emoji: str):
    has_bot_reaction = False

    for reaction in message.reactions:
        if reaction.emoji != emoji:
            continue

        users_that_reacted = await reaction.users().flatten()
        if client.user in users_that_reacted:
            has_bot_reaction = True

    return has_bot_reaction


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


async def send_random_config(received_message: discord.Message):
    config_string = get_random_config()

    try:
        sent_message = await received_message.channel.send(config_string)
        await sent_message.add_reaction('🔁')
        return "Success"
    except Exception as e:
        return str(e)


async def update_random_config(message):
    config_string = get_random_config()

    try:
        await message.edit(content=config_string)
        return "Success"
    except Exception as e:
        return str(e)


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
        'execute': send_random_config
    }
}


possible_reactions = {
    "🔁": update_random_config
}


async def analyize_message(received_message: discord.Message):
    command = received_message.content[1:]

    if command not in possible_commands.keys():
        return "Command not found. Type !help to see possible commands"

    return await possible_commands[command]['execute'](received_message)


async def analyze_reaction(received_reaction: discord.Reaction):
    if received_reaction.message.author != client.user or received_reaction.emoji not in possible_reactions.keys():
        return

    if await check_if_message_has_bot_reaction(received_reaction.message, received_reaction.emoji):
        await possible_reactions[received_reaction.emoji](received_reaction.message)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(COMMAND_PREFIX):
        await analyize_message(message)


@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    await analyze_reaction(reaction)


client.run(BOT_TOKEN)
