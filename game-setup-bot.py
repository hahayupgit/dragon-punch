import importlib
import os

import discord
import src.setup as setup
import src.commands

# iterates through all files in ./src/commands
for file in os.listdir('./src/commands'):
    
    # if any file is a python file and it's not the init file,
    # import it as an absolute module to src.commands, and remove the ending .py
    if file.endswith('.py') and file != '__init__.py':
        importlib.import_module(f'src.commands.{file[:-3]}')

# get the bot token and the admin usernames
token = setup.get_token()
admin = setup.get_admin()

# add default intents, ensure the messaging intent is added to true,
# and generate a new client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# calls an event that happens when the bot is ready, 
# prints success message to console
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# when the bot recieves a message,
@client.event
async def on_message(message):
    
    # checks if the bot is replying to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await src.commands.hello.default(message)
    
    if message.content.startswith('$stop'):
        await src.commands.stop.default(message, admin, client)

client.run(token)
