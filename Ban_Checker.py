import requests
from colorama import Fore, init
import threading
import os

init(convert=True)
lines = [item.replace("\n", "") for item in open('usernames.txt', 'r').readlines()]
lines1 = lines[:len(lines)//2]
lines2 = lines[len(lines)//2:]
threads = []
title = """
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
 ██████╗ ██████╗ ██╗ ██████╗     ██████╗  █████╗ ███╗   ██╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
 ██╔══██╗██╔══██╗██║██╔═══██╗    ██╔══██╗██╔══██╗████╗  ██║    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ██████╔╝██████╔╝██║██║   ██║    ██████╔╝███████║██╔██╗ ██║    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
 ██╔═══╝ ██╔══██╗██║██║   ██║    ██╔══██╗██╔══██║██║╚██╗██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 ██║     ██║  ██║██║╚██████╔╝    ██████╔╝██║  ██║██║ ╚████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
 ╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
                                                    by BGP#0419
"""

invalid   = []
banned    = []
unbanned  = []
unchecked = []

mode = "Old"
url = "https://donate.2b2t.org/category/738999"

def category(color, colorLight, category, categoryName, max):
    print(color + categoryName + ":")
    print(color + "---------")
    if len(category) == 0:
        print(Fore.LIGHTBLACK_EX + "None")
    for i in range(len(category)):
        if i < max:
            print(colorLight + f"• {category[i]}")
        else:
            print(colorLight + f"+ {str(len(category) - max)} more")
            break
    print("\n")

def update():
    os.system('cls' if os.name=='nt' else 'clear')

    category(Fore.RED, Fore.LIGHTRED_EX, banned, "Banned", 5)
    category(Fore.GREEN, Fore.LIGHTGREEN_EX, unbanned, "Unbanned", 5)
    category(Fore.MAGENTA, Fore.LIGHTMAGENTA_EX, unchecked, "Invalid", 2)
    category(Fore.CYAN, Fore.LIGHTCYAN_EX, unchecked, "Unchecked", 2)

def check(input):
    request = requests.request('POST', url, data = f'ign={input}', headers = { 'Content-Type': 'application/x-www-form-urlencoded' })

    if 'rate limited' in request.text:
        unchecked.append(input)
        if mode == "Old":
            print(Fore.YELLOW + "RATE LIMITED!!")
    elif 'not a valid' in request.text:
        invalid.append(input)
        if mode == "Old":
            print(Fore.YELLOW + f"{input} is invalid")
    elif 'Unable' in request.text:
        invalid.append(input)
        if mode == "Old":
            print(Fore.YELLOW + f"{input} is invalid")
    elif 'banned' not in request.text:
        unbanned.append(input)
        if mode == "Old":
            print(Fore.GREEN + f"{input} is unbanned")
    else:
        banned.append(input)
        if mode == "Old":
            print(Fore.RED + f"{input} is banned")
    
    if mode == "New":
        update()

########################## START

print(Fore.LIGHTRED_EX + title)

file = open('result.txt', 'a')
file.close()
file = open('result.txt', 'r+')

if len(file.read()) > 0:
    file.close()
    delete = input("\"result.txt\" is not empty. Do you want to empty it? (Y/n) " + Fore.RESET)
    
    if "Y" in delete:
        os.remove("result.txt")

mode = input(Fore.RED + "Which mode do you want to use? (New/Old) " + Fore.RESET)
if "N" in mode or "n" in mode:
    mode = "New"
else:
    mode = "Old"

urlQ = input(Fore.RED + "Do you want to use a custom URL? (Y/n) " + Fore.RESET)
if "Y" in urlQ:
    url = input(Fore.RED + "Enter a custom URL: " + Fore.RESET)
    print(url)

def l1():
    for i in range(len(lines1)):
        check(lines1[i])
def l2():
    for i in range(len(lines2)):
        check(lines2[i])

t1 = threading.Thread(target=l1)
t2 = threading.Thread(target=l2)
threads.append(t1)
threads.append(t2)
t1.start()
t2.start()

print(("\nFinished loading all threads.\n").center(119))
for x in threads:
    x.join()

print(Fore.BLUE + "Saving file...")
file = open('result.txt', 'a')

def writeList(file, list, action):
    file.write("--" + action + "--\n")
    file.write("----")
    for i in range(len(action)):
        file.write("-")
    for i in list:
        file.write("\n• " + i)
    file.write("\n\n")

writeList(file, banned, "Banned")
writeList(file, unbanned, "Unbanned")
writeList(file, unchecked, "Unchecked")
writeList(file, invalid, "Invalid")

file.close()
print(Fore.BLUE + "Saved!")

input(Fore.RESET + 'Finished Checking!')