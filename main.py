from colorama import Fore
import threading
import requests
import time
import os.path

usernames = [item.replace("\n", "") for item in open('usernames.txt', 'r').readlines()]
proxies = [item.replace("\n", "") for item in open('proxies.txt', 'r').readlines()] if os.path.exists("proxies.txt") else []

# Very fast
def check_proxy(proxy):
    req = requests.post(
        "https://shop.2b2t.org/checkout/packages/add/1994962/single?ign=CAEC64",
        allow_redirects=False,
        proxies={
            "http": "http://" + proxy,
            "https": "http://" + proxy
        }
    )

    try:
        if "XRxlbOYKOzX5HYSsk7VO72KxURUxqkzYCSTxTat" in req.headers["Set-Cookie"].split("; ")[0]:
            print(proxy + " is working")
        else:
            print(req.headers["Set-Cookie"].split("; ")[0])
    except:
        print(proxy + " is not working")
        proxies.remove(proxy)

def check_proxies():
    threads = []

    for proxy in proxies:
        thread = threading.Thread(target=check_proxy, args=(proxy,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f"There are {len(proxies)} working proxies")

def output(username, result):
    stats["Total"] += 1

    if "buycraft_basket" in result:
        res = Fore.GREEN + username + " is unbanned"
        stats["Unbanned"] += [username]
        output("Unbanned", username)
    elif "XRxlbOYKOzX5HYSsk7VO72KxURUxqkzYCSTxTat" in result:
        res = Fore.LIGHTRED_EX + username + " is banned"
        stats["Banned"] += [username]
        output("Banned", username)
    elif result == "message=XRxlbOYKOzX5HYSsk7VO79kWPpwubYetzyPeyIphpZPxM%2BTo3%2BDuWHTzXALpQCz%2FyK8QCd0VpduRCEow0JIFDg%3D%3D":
        res = Fore.BLUE + username + " is not found"
        stats["Errors"] += [username]
        output("Missing", username)
    elif result == "message=AeSOVxjOOOMBhHAGYvcmCdJEE6pUQYonWMSJbkGLdUV2oNeagFeBuFUSV3NdTnIa":
        res = Fore.BLUE + username + " is invalid"
        stats["Errors"] += [username]
        output("Invalid", username)
    elif result == "message=XRxlbOYKOzX5HYSsk7VO79kWPpwubYetzyPeyIphpZOryToGcxK9AL6pF0TwQ1EZ":
        res = Fore.BLUE + username + " is deleted"
        stats["Errors"] += [username]
        output("Deleted", username)
    else:
        stats["Errors"] += [username]
        res = "Unexpected result" + result + username
        output("Unexpected_Result", username)
    
    print(f"{res}{Fore.RESET} ({stats['Total']}/{len(usernames)})")

def check(username, proxy):
    if proxy != None:
        req = requests.post(
            "https://shop.2b2t.org/checkout/packages/add/1994962/single?ign=" + username,
            allow_redirects=False,
            proxies={
                "http": proxy,
                "https": proxy
            }
        )
    else:
        req = requests.post(
            "https://shop.2b2t.org/checkout/packages/add/1994962/single?ign=" + username,
            allow_redirects=False
        )

    if req.headers.__contains__("Retry-After"):
        print("RATE LIMITED FOR " + req.headers["Retry-After"] + "s")
        stats["Errors"] += [username]
    elif req.headers.__contains__("Set-Cookie"):
        output(username, req.headers["Set-Cookie"].split("; ")[0])
    else:
        stats["Errors"] += [username]
        stats["Total"] += 1
        print("Proxy error ?", username, proxy, req.status_code)

def check_thread(id, dim):
    proxy = proxies[id]

    for i in range(id, len(usernames), dim):
        check(usernames[i], proxy)
        time.sleep(1.5)

def check_all():
    if len(proxies) > 0:
        threads = []
        dim = len(proxies)

        for i in range(dim):
            thread = threading.Thread(target=check_thread, args=(i, dim))
            thread.start()
            threads.append(thread)
        
        print("Started all threads")

        for thread in threads:
            thread.join()
    else:
        for username in usernames:
            check(username)
            time.sleep(1.5)
        
    print("Finished")

# Save immediately
def output(category, name):
    open("output.txt", 'a+').write(f"\n{category}: {name}")

# Save when complete
def save():
    with open("logs.txt", "a+") as f:
        text = ''
        
        for i in ["Banned", "Unbanned", "Errors"]:
            text += f"\n\n{i}:\n\n"
            for j in stats[i]:
                text += j + '\n'

        f.write(text)

start_time = time.time()
check_proxies()
print(f"It took {time.time() - start_time}s to check proxies")
start_time = time.time()
check_all()
print(f"It took {time.time() - start_time}s to finish")
save()