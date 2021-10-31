# Prio ban checker
 Checks a list of players to see if they are banned from the Minecraft server, 2b2t.org

![Example](https://github.com/BGP0/Prio-ban-checker/blob/main/example.gif?raw=true)

## Installation

1. Install Python3 if you don't already have it
2. I think everything should installed, but if you get an error saying can't find something (in this example requests) do:
```
pip3 install requests
```
## Usage

1. Get some usernames and put them into username.txt, each on a seperate line
2. Open a terminal in the folder and type ```python3 main.py```
3. Should take a few seconds to finish checking every name thanks to asyncio and aiohttp!

you can also enable output ban/unbanlist in main.py
