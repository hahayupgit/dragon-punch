import json

def get_token():
    file = open('secrets.json', 'r')
    token = json.load(file).get('DiscordKey')
    file.close()
    return token