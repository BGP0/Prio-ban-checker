import asyncio
import aiohttp
import time
from colorama import Fore

# - Settings - #######
outputUnbanList = False
outputBanList   = False
######################

# Program Data
unbanList = []
banList   = []

# Checks a given username
async def check(username, session):
    async with session.get(f"https://shop.2b2t.org/checkout/packages/add/1994771/subscription?ign={username}") as request:
        output = f"{Fore.LIGHTBLACK_EX}<{Fore.LIGHTBLUE_EX}{username}{Fore.LIGHTBLACK_EX}> " + (" " * (16 - len(username)))

        if request.headers["Connection"] != "keep-alive":
            print(Fore.WHITE + f"RATE LIMITED: {username} (Connection: {request.headers['Connection']})")
            return
            
        if "Set-Cookie" in request.headers:
            response = request.headers["Set-Cookie"].split("; ")[0][8:]
            
            # TODO: Add a switch statement but need to wait for python 3.10
            if (response == "XRxlbOYKOzX5HYSsk7VO79kWPpwubYetzyPeyIphpZPxM%2BTo3%2BDuWHTzXALpQCz%2FyK8QCd0VpduRCEow0JIFDg%3D%3D"):
                output += Fore.LIGHTYELLOW_EX + "Unable to find a player with that username"
            elif (response == "AeSOVxjOOOMBhHAGYvcmCdJEE6pUQYonWMSJbkGLdUV2oNeagFeBuFUSV3NdTnIa"):
                output += Fore.YELLOW + "That is not a valid username"
            elif (response == "deleted"):
                output += Fore.RED + "That user is banned"
                banList.append(username)
        else:
            output += Fore.GREEN + "Unbanned"
            unbanList.append(username)
            print(request.headers)
    
        print(output)

# Asynchronously check the status of each username from a list
async def checkList(usernames):
    async with aiohttp.ClientSession() as session:
        tasks = []

        for username in usernames:
            tasks.append(asyncio.ensure_future(check(username, session)))
        
        await asyncio.gather(*tasks)


# Start the program
start_time = time.time()
asyncio.run(checkList([item.replace("\n", "") for item in open('usernames.txt', 'r').readlines()]))

# Additional outputs, if configured
if (outputUnbanList): print(Fore.GREEN + "\n".join(unbanList))
if   (outputBanList): print(Fore.RED   + "\n".join(  banList))

# Resets the terminal color and outputs time taken
print(Fore.RESET + f"Checked all usernames in {round(time.time() - start_time, 2)} seconds!")