import requests

def search_query(query):

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "53d82afdb9msh5305c311469a516p173941jsna60a3ec2ae11"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

def main():
    print("What do you want to search")
    query = input()
    querystring = {"term":query}

    search_query(querystring)

main()