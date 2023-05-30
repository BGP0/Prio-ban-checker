# Prio ban checker
Checks a list of players to see if they are banned from the 2b2t.org Minecraft "Anarchy" server.
This repo barely works, the list has become too long, it only records usernames. Maybe one day ill fix bugs and run this with 1 million usernames.

## Installation

1. Install Python3 if you don't already have it
2. If you get an error saying can't find something when running the program install the library you are missing like this:
```
pip3 install colorama
```
## Usage

1. Get some usernames and put them into username.txt, each on a seperate line
2. Open a terminal in the folder and type ```python3 main.py```
3. Wait for the list to finish checking and then check logs.txt
4. Optionally, you can put proxies in proxies.txt to speed up the process as tebex ratelimits each ip to like 1 request per second or something but we want to do 100 requests in 1 second
