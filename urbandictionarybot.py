import requests
import discord
import json
import aiohttp
from discord.ext import commands

def perform_request(url, querystring):
    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "53d82afdb9msh5305c311469a516p173941jsna60a3ec2ae11"
    }
    response = requests.request(
    "GET", url, headers=headers, params=querystring)


    print(response.text)

    return response.text

def search_query(querystring):

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    return perform_request(url, querystring)

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
    querystring = {"term": query}
    definition_list = json.loads(search_query(querystring))['list']

    definition = definition_list[0]['definition']
    example = definition_list[0]['example']

    await ctx.send("Definition of " + querystring['term'] + " :" + definition)
    await ctx.send("Example of " + querystring['term'] + " :" + example)

@bot.command(name='random')
async def random(ctx):
    definition_list = json.loads(search_random_word())['list']

    definition = definition_list[0]['definition']
    example = definition_list[0]['example']

    await ctx.send(definition)
    await ctx.send(example)

@bot.event
async def on_ready():
    print("Nonce Bot is ready")


bot.run('MzU3NjI1MzQ3MDUyNjY2OTEw.XvZd2A.p_YNVvyw281Z5h_BYH1itjAPTuA')