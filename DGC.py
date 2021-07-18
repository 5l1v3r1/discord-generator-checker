import random, string
import webbrowser
import time
import requests
import colorama
from colorama import Fore, init
colorama.init()

print(f"""{Fore.RED}
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝{Fore.BLUE}
░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝{Fore.RESET}""")

print()
print(f"                   {Fore.RED}Creator {Fore.RESET}| {Fore.BLUE}Doop / 7uk{Fore.RESET}")
print()

print(f'[{Fore.BLUE}+{Fore.RESET}]{Fore.BLUE} Number of codes to GEN+CHECK{Fore.RESET}')
num=input(' > ')
print()

f=open("Codes.txt","w", encoding='utf-8')

print(f"{Fore.RESET} [{Fore.BLUE}!{Fore.RESET}] {Fore.BLUE}Starting to generate + check...{Fore.RESET}")
print()

for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()


with open("Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            with open('ValidCodes.txt') as valid:
                valid = f"{Fore.RESET} Valid | {Fore.GREEN}" + " {}".format(line.strip("\n"))
                print(valid)
                f.write('VALID NITRO | https://discord.gift/')
                f.write(url)
                f.write("\n")
                break
        else:
        	print(f"{Fore.RESET} Invalid | {Fore.RED}" + " {}".format(line.strip("\n")))

print()
print(f"{Fore.RESET}[{Fore.BLUE}!{Fore.RESET}]{Fore.BLUE} Finished Checking! {Fore.RESET}")
print()

input(' Press any key to exit... ')
