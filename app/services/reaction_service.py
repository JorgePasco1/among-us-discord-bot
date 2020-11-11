from discord import Reaction, User

from app.helpers import generate_random_config


async def update_random_config(reaction: Reaction):
    message = reaction.message
    config_string = generate_random_config()

    try:
        await message.edit(content=config_string)
    except Exception as e:
        print(str(e))


async def remove_reaction_after_update(reaction: Reaction, user: User):
    try:
        await reaction.remove(user)
    except Exception as e:
        print(str(e))


possible_reactions = {
    "🔁": update_random_config
}
