import requests
import discord
import json
import aiohttp
from discord.ext import commands

async def search_query(querystring):
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, f'https://api.urbandictionary.com/v0/define?term={querystring}')
        return data
        
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def search_random_word():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session, 'https://api.urbandictionary.com/v0/random')
        return data

bot = commands.Bot(command_prefix='=')

@bot.command(name='search')
async def search_dictionary(ctx, *, query):
    querystring = query
    definition_list = json.loads(await search_query(querystring))['list']

    definition = definition_list[0]['definition']
    example = definition_list[0]['example']

    await ctx.send("Definition of " + querystring + " :" + definition)
    await ctx.send("Example of " + querystring + " :" + example)

@bot.command(name='random')
async def random(ctx):
    definition_list = json.loads(await search_random_word())['list']

    definition = definition_list[0]['definition']
    example = definition_list[0]['example']
    await ctx.send(" WORD " +definition_list[0]['word'])
    await ctx.send(definition)
    await ctx.send(example)

@bot.event
async def on_ready():
    print("Nonce Bot is ready")


bot.run('MzU3NjI1MzQ3MDUyNjY2OTEw.XvZd2A.p_YNVvyw281Z5h_BYH1itjAPTuA')

