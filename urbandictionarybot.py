import requests
from discord.ext import commands


def search_query(query):

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
    result = search_query(querystring)

    await ctx.send(result)

    