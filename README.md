# dragon-punch
Discord bot for managing LAN game setups.

# Installation Setup
- prerequisites: git, mongoDB, python, pip installed, created a bot account from [this](https://discordpy.readthedocs.io/en/latest/discord.html) guide.
> [!NOTE]
> I'm using [MongoDB Community Edition](https://www.mongodb.com/docs/manual/administration/install-community/) for local development.
```
# clone the repo
git clone https://github.com/hahayupgit/dragon-punch.git

# create a python virtual environment in the cloned source repo
python3 -m venv dragon-punch/

# activate the virtual environment 
source dragon-punch/bin/activate

# enter the directory
cd dragon-punch

# install/update the necessary dependencies from "requirements.txt"
pip install -Ur requirements.txt

# copy the "secrets-template.json" file and name it "secrets.json"
cp secrets-template.json secrets.json

# after doing this, replace "key" with your discord bot token,
# and the "admin1" and "admin2" strings with the usernames for your admins. 
# you can add as few or as many admins as you'd like in the array (square brackets).
```

# Current Ideas for the Bot:
- Link game setups to individual Discord IDs for easy availability on who can bring setups
- Ability to mass ping people per-game for different events/LANS
    - Schedule these pings
- Automatic management of game roles per person
- Presets for specific setups which enables quick configurations for new users (consoles, laptops, etc)
- Add accessories such as adaptors, controllers, monitors, cables, etc
- Create a custom backup chat that is read only, which can be updated as an offline backup in case of a bot outage
    - Also applicable to avoid constant use of bot commands, can just check the #setups chat
- Plug into IGDB API in order to have easy access to game titles, also add custom titles
- Add game info to your profile i.e. mains, favorite games, ping me for x game, etc
- Implement Docker

# Wider ideas:
- Cross server setup linkage


# Resources I'm using:
- https://discordpy.readthedocs.io/en/latest/index.html
- https://github.com/Whisky-App/uisuki (for minor project structuring)
- https://www.igdb.com/api
- https://www.mongodb.com/
- https://www.docker.com/