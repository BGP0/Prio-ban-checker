import requests
from colorama import Fore, init
import threading

class newCheck():

    def __init__(self, usernames):
        self.usernames = str(usernames)
        init(convert=True)
        self.lines = [item.replace("\n", "") for item in open(self.usernames, 'r').readlines()]
        self.lines1 = self.lines[:len(self.lines)//2]
        self.lines2 = self.lines[len(self.lines)//2:]
        self.threads = []


    def check(self, input):
        data = f'ign={input}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }

        request = requests.request('POST', "https://donate.2b2t.org/category/738999", data=data, headers=headers)
        if 'rate limited' in request.text:
            print(Fore.LIGHTMAGENTA_EX + f"YOU'VE BEEN RATELIMITED!! :(")
        elif 'not a valid' in request.text:
            print(Fore.LIGHTRED_EX + f"{input} is not a valid username")
        elif 'Unable' in request.text:
            print(Fore.LIGHTRED_EX + f"Unable to find a player with the username: {input}")
        elif 'banned' not in request.text:
            print(Fore.LIGHTRED_EX + f"{input} is not currently banned")
        else:
            print(Fore.LIGHTGREEN_EX + f"{input} is currently banned")

    def l1(self):
        for i in range(len(self.lines1)):
            self.check(self.lines1[i])
    def l2(self):
        for i in range(len(self.lines2)):
            self.check(self.lines2[i])

    def start(self):
        self.t1 = threading.Thread(target=self.l1)
        self.t2 = threading.Thread(target=self.l2)
        self.threads.append(self.t1)
        self.threads.append(self.t2)
        self.t1.start()
        self.t2.start()

        print(('\nFinished loading all threads.\n').center(119))
        for x in self.threads:
            x.join()

        input(Fore.RESET + 'Finished Checking!')
