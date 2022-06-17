import os

try:
    import requests
    from colorama import init, Fore
except ModuleNotFoundError:
    os.system('pip3 install requests')
    os.system('pip3 install colorama')

init(autoreset=False)
os.system("cls")

r = requests.Session()
print(f"{Fore.LIGHTCYAN_EX}NGL.LINK Spammer! By @ykw/@linuxbg on IG")
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
        response = r.post(url, headers=headers, data=payload)
        questions_count += 1
        print(f"{Fore.GREEN}{questions_count} {Fore.WHITE}Questions Sent to: {Fore.RED}{target}", end='\r')
        
if start == "Y":
    spam()
else:
    print("Invalid Response")
    exit()
