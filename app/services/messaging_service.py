from discord import Message

from app.helpers import generate_random_config


async def say_hello(received_message: Message):
    salutation = "Hello! I am a bot. Type !help to see the available commands"
    await received_message.channel.send(salutation)


async def get_help(received_message: Message):
    description_lines = ''

    for command in possible_commands.keys():
        description_lines = description_lines + \
            f"\t**!{command}**: {possible_commands[command]['description']}" + "\n"

    response = f"""The available commands are:
{description_lines}
    """

    await received_message.channel.send(response)


async def send_random_config(received_message: Message):
    config_string = generate_random_config()

    try:
        sent_message = await received_message.channel.send(config_string)
        await sent_message.add_reaction('🔁')
        print("Success sending random config")
    except Exception as e:
        print(str(e))


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
