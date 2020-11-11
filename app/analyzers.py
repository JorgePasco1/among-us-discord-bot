from discord import Message, Reaction, Client, User

from app.services.messaging_service import possible_commands
from app.services.reaction_service import possible_reactions, remove_reaction_after_update
from app.helpers import check_if_message_has_bot_reaction


async def analyze_message(received_message: Message):
    command = received_message.content[1:]

    if command not in possible_commands.keys():
        return "Command not found. Type !help to see possible commands"

    return await possible_commands[command]['execute'](received_message)


async def analyze_reaction(client: Client, received_reaction: Reaction, user: User):
    message = received_reaction.message
    emoji = received_reaction.emoji

    if emoji not in possible_reactions.keys() or not await check_if_message_has_bot_reaction(client, message, emoji):
        return

    success = await possible_reactions[emoji](received_reaction)
    if success:
        await remove_reaction_after_update(received_reaction, user)
