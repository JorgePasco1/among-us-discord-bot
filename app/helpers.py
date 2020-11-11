from random import randint, randrange, choice

from discord import Client, Message


def generate_random_config():
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


async def check_if_message_has_bot_reaction(client: Client, message: Message, emoji: str):
    has_bot_reaction = False

    for reaction in message.reactions:
        if reaction.emoji != emoji:
            continue

        users_that_reacted = await reaction.users().flatten()
        if client.user in users_that_reacted:
            has_bot_reaction = True

    return has_bot_reaction
