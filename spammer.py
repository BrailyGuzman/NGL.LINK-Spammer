import requests
from colorama import init, Fore, Back, Style
import os
init(autoreset=False)
os.system("cls")

r = requests.Session()
print(f"{Fore.LIGHTCYAN_EX}NGL.LINK Spammer!")
target = input(f"{Fore.GREEN}Enter {Fore.RED}Target: {Fore.WHITE}")
question = input(f"{Fore.GREEN}Enter {Fore.RED}Question: {Fore.WHITE}")
start = input(f"{Fore.WHITE}Are you {Fore.GREEN}Ready? Y/N: {Fore.WHITE}").upper()
def spam():
    questions_count = 0
    url = f"https://ngl.link/{target}"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }

    payload = {
        "question": question
    }
    while True:
        spam = r.post(url, headers=headers, data=payload)
        questions_count += 1
        print(f"{questions_count} Questions Sent to: {target}")

if start == "Y":
    spam()
else:
    print("Invalid Response")
    exit()
