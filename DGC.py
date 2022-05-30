import random, string, os, requests, threading

THREADS = 8

class Colors:
    """ Program Colors """
    red = u"\u001b[31m"
    green  = u"\u001b[32m"
    reset  = u"\u001b[0m"

c = Colors()

class DGC(object):

    def __init__(dgc):
        dgc.checked = []
        dgc.amt = input(' [?] Number of codes to Generate and Check -> ')
        dgc.banner = f"""
        {c.red}
        ░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
        ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
        ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
        ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
        ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
        ░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝{c.green}
        ░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
        ░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
        ██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
        ╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
        ░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
        ░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
        {c.reset}
        """

        dgc.Menu()

    @staticmethod
    def StartThreads(func) -> None:
        for i in range(THREADS):
            thread = threading.Thread(target=func, args=[i])
            thread.start()

    def Menu(dgc) -> None:
        os.system('cls')
        print(dgc.banner)
        dgc.Generate()
        dgc.StartThreads(dgc.Checker)
        print(f"[{c.red}!{c.reset}]{c.red} Finished Checking!")

    def Generate(dgc):
        print(f"{c.reset} [{c.red}!{c.reset}] {c.red}Generating...")

        with open("Codes.txt","w", encoding='utf-8') as f:
            for n in range(int(dgc.amt)):
                y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
                f.write(f'https://discord.gift/{y}\n')
            f.close()
        print(f"{c.reset} [{c.red}!{c.reset}] {c.red}Checking...")

    def Checker(dgc, threadNum):
        with open("Codes.txt") as f:
            for line in f:
                nitro = line.strip("\n")
                if nitro in dgc.checked:
                    continue
                else:
                    dgc.checked.append(nitro)
                url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
                r = requests.get(url)
                
                match r.status_code:
                    case 200:
                        with open('ValidCodes.txt') as valid:
                            valid = f"{c.reset}[Thread {threadNum}] Valid | {c.green}" + " {}".format(line.strip("\n"))
                            print(valid)
                            f.write(f'VALID NITRO | https://discord.gift/{url}\n')
                            break
                    case _:
                        print(f"{c.reset} [Thread {threadNum}] Invalid | {c.red}" + " {}".format(line.strip("\n")))
            f.close()

Program = DGC()
input('>> Press any key to exit... ')
