import requests
import discord
import json
import aiohttp
from discord.ext import commands

# Constants
LIST = 'list'
DEFINTION = 'definition'
EXAMPLE = 'example'
BASE_URL = 'https://api.urbandictionary.com/v0/'
BOT_TOKEN = 'MzU3NjI1MzQ3MDUyNjY2OTEw.XvZd2A.p_YNVvyw281Z5h_BYH1itjAPTuA'

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

# Create the bot
bot = commands.Bot(command_prefix='=')

# Parse the searched word and display here
@bot.command(name='search')
async def search_dictionary(ctx, *, query):
    # Gets the typed in query and parses it
    querystring = query
    definition_list = json.loads(await search_query(querystring))[LIST]

    definition = definition_list[0][DEFINTION]
    example = definition_list[0][EXAMPLE]

    await ctx.send("Definition of " + querystring + " :" + definition)
    await ctx.send("Example of " + querystring + " :" + example)

# Parse the random word and display here
@bot.command(name='random')
async def random(ctx):
    definition_list = json.loads(await search_random_word())[LIST]

    definition = definition_list[0][DEFINTION]
    example = definition_list[0][EXAMPLE]
    await ctx.send("Random word -> " +definition_list[0]['word'])
    await ctx.send(definition)
    await ctx.send(example)

# Check if the bot is running
@bot.event
async def on_ready():
    print("Nonce Bot is ready")

# Run the bot
bot.run(BOT_TOKEN)

