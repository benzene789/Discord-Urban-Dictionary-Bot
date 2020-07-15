import json

import asyncio
import aiohttp
import discord
import requests
from discord.ext import commands

# Constants
LIST = 'list'
DEFINTION = 'definition'
EXAMPLE = 'example'
BASE_URL = 'https://api.urbandictionary.com/v0/'
BOT_TOKEN = 'MzU3NjI1MzQ3MDUyNjY2OTEw.XvZd2A.p_YNVvyw281Z5h_BYH1itjAPTuA'
NEXT_DEFINITION = '➡️'
EMBED_COLOUR = 0xcf1e25

# Search a word the user types in
async def search_query(querystring):
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, BASE_URL+ f'define?term={querystring}')
        return data

# Fetch the URL
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

# Search up a random word
async def search_random_word():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, BASE_URL+ 'random')
        return data

async def create_embed(definitions, ctx):
    def check_reaction(reaction, user):
        return (str(reaction.emoji) == NEXT_DEFINITION
        and reaction.message.id == message.id
        and user.id != bot.user.id)

    counter = 0
    display = True
    message = None

    while display:

        definition = definitions[counter][DEFINTION]
        example = definitions[counter][EXAMPLE]
        word = definitions[counter]['word']

        embed = discord.Embed(title="Defining...", color=EMBED_COLOUR)

        embed.add_field(name='Word', value= word)
        embed.add_field(name="Definition", value= definition)
        embed.add_field(name='Example', value= example)

        if message is None:
            message = await ctx.send(embed=embed)
            # add emoji to message
            await message.add_reaction(NEXT_DEFINITION)
        else:
            await message.edit(embed=embed)
        
        try:
            reaction, user = await bot.wait_for(
                'reaction_add', check=check_reaction, timeout=60.0)
            counter = (counter + 1) % len(definitions)
        except asyncio.TimeoutError:
            await message.delete()
            break
        await reaction.remove(user)

# Create the bot
bot = commands.Bot(command_prefix='=')

# Parse the searched word and display here
@bot.command(name='search')
async def search_dictionary(ctx, *, query):

    # Gets the typed in query and parses it
    querystring = query
    definition_list = json.loads(await search_query(querystring))[LIST]

    await create_embed(definition_list, ctx)

# Parse the random word and display here
@bot.command(name='random')
async def random(ctx):
    definition_list = json.loads(await search_random_word())[LIST]

    await create_embed(definition_list, ctx)

# Check if the bot is running
@bot.event
async def on_ready():
    print("Nonce Bot is ready")

# Run the bot
bot.run(BOT_TOKEN)

