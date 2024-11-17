from random import choice
from colorama import Fore, Back, Style
import colorama

colorama.init(autoreset=True)

print(Fore.RED + """
██╗░░░██╗██╗░██████╗░█████╗░  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░██║██║██╔════╝██╔══██╗  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚██╗░██╔╝██║╚█████╗░███████║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░╚████╔╝░██║░╚═══██╗██╔══██║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚██╔╝░░██║██████╔╝██║░░██║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░╚═╝╚═════╝░╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
                        This Tool For Visa Checker
                     [!] Coded By Makavael whatsapp: +201029107547 www.Makavael.com[!]
""")

ch = input("""
1 - Make Combo [ Visa ]
2 - Check Visa
""")

if ch == "1":
    numofvisa = 16
    filesave = 'Densor.txt'  # Instead of the name < Densor > you can add the name of your file
    nums = '123456789'
    while True:
        visa = ''.join(choice(nums) for _ in range(numofvisa))
        visacr = '123456789'
        visas = 1
        viscr = ''.join(choice(visacr) for _ in range(visas))
        visacr = '5'
        visas = 2
        vissadata = '02'.join(choice(visacr) for _ in range(visas))
        visacvcn = '123456789'
        visacvch = 3
        visacvc = ''.join(choice(visacvcn) for _ in range(visacvch))
        print(f"{visa}|{viscr}/{vissadata}|{visacvc}")
        with open(filesave, 'a') as c:
            c.write(f"{visa}|{viscr}/{vissadata}|{visacvc}\n")

elif ch == "2":
    from HamodyTools import Hamody
    filevisa = input("[+] Enter List Visa :")
    vises = [line.strip() for line in open(filevisa)]
    for visa2 in vises:
        check = Hamody.Visa(visa2)
        if not check:
            print(Fore.RED + "[!] Dead Visa")
        else:
            print(Fore.GREEN + check)
            with open('visa_true.txt', 'a') as c:
                c.write(check + '\n')
else:
    print(Fore.RED + "Invalid choice. Please select 1 or 2.")
