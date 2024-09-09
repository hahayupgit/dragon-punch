# TODO:
# - okay yeah i need to do this in a database

import os
import json

async def default(message):
    playerdata_file = 'you\'re not supposed to see this!'
    
    # tries to read the playerdata
    try:
        playerdata_file = open('./data/playerdata.json', 'r')
    
    # if file does not exist, creates the file and initiates the format,
    # then opens in read
    except:
        playerdata_file = open('./data/playerdata.json', 'x')
        playerdata_file.write("{\n  \"Players\":[]\n}")
        playerdata_file = open('./data/playerdata.json', 'r')
    
    # loads the playerdata json into a dictionary
    playerdata = json.load(playerdata_file)
    playerdata_file.close()
    
    # stores all current players, 
    # adds the player who invocated the action to the temp array
    temp = []
    for i in playerdata["Players"]:
        temp.append(i)
    temp.append(message.author.global_name)
    
    # sets the current player array to the temp array
    playerdata["Players"] = temp
    
    # overwrites the json file with the dictionary
    playerdata_file = open('./data/playerdata.json', 'w')
    playerdata_file.write(json.dumps(playerdata, indent=4))
    playerdata_file.close