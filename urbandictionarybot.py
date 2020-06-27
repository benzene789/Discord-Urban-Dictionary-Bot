import requests
import discord
import json
from discord.ext import commands

def search_query(querystring):

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "53d82afdb9msh5305c311469a516p173941jsna60a3ec2ae11"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    return response.text

bot = commands.Bot(command_prefix='=')


@bot.command(name='search')
async def search_dictionary(ctx, *, query):
    querystring = {"term": query}
    definition_list = json.loads(search_query(querystring))['list']

    definition = definition_list[0]['definition']
    example = definition_list[0]['example']

    await ctx.send("Definition of " + querystring + " :" + definition)
    await ctx.send("Example of " + querystring + " :" + example)


bot.run('MzU3NjI1MzQ3MDUyNjY2OTEw.XvZd2A.p_YNVvyw281Z5h_BYH1itjAPTuA')