import os

import discord

from app.analyzers import analyze_message, analyze_reaction

client = discord.Client()
intents = discord.Intents.reactions = True  # Needed to listen to reactions
BOT_TOKEN = os.getenv('BOT_TOKEN')
COMMAND_PREFIX = '!'


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(COMMAND_PREFIX):
        await analyze_message(message)


@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    await analyze_reaction(client, reaction, user)


def start_bot():
    client.run(BOT_TOKEN)
