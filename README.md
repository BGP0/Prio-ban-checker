# Prio ban checker
 Checks if a player is banned from donate.2b2t.org

![picture](https://i.imgur.com/VhdVI8R.png)

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
4. Then just look at the results, you can set outputUnbanList/outputBanList to true near the top of main.py if you want it to output them at the end.