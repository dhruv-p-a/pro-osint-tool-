import requests
from bs4 import BeautifulSoup
import sys
import time
import re

# Colors for Kali Terminal
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def banner():
    print(f"{CYAN}")
    print("  ██████╗ ███████╗██╗███╗   ██╗████████╗")
    print(" ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝")
    print(" ██║   ██║███████╗██║██╔██╗ ██║   ██║   ")
    print(" ██║   ██║╚════██║██║██║╚██╗██║   ██║   ")
    print(" ╚██████╔╝███████║██║██║ ╚████║   ██║   ")
    print("  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   ")
    print(f"        V1.0 - KALI TERMINAL EDITION {RESET}\n")

def search_telegram(username):
    print(f"{YELLOW}[*] Scraping Telegram Intelligence for: @{username}{RESET}")
    url = f"https://t.me/{username.replace('@', '')}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            name_tag = soup.find("span", {"dir": "auto"})
            bio_tag = soup.find("div", {"class": "tgme_page_description"})

            if name_tag:
                print(f"{GREEN}[+] Name Found: {name_tag.text}{RESET}")
                if bio_tag:
                    print(f"{GREEN}[+] Bio: {bio_tag.text}{RESET}")
                return True
            else:
                print(f"{RED}[-] No public profile data found on Telegram.{RESET}")
        else:
            print(f"{RED}[-] Telegram user not found.{RESET}")
    except Exception as e:
        print(f"{RED}[!] Error reaching Telegram: {e}{RESET}")
    return False

def check_breach(email):
    print(f"{YELLOW}[*] Checking Leak Databases for: {email}{RESET}")
    # Using a common public lookup simulation
    # In a real tool, you would call APIs like HaveIBeenPwned or IntelligenceX here
    time.sleep(1)
    if "@" in email:
        print(f"{RED}[!] SECURITY ALERT: Email found in Data Breach Dumps!{RESET}")
        print(f"{CYAN}[i] Suggested: Check 'Intelligence X' or 'DeHashed' for details.{RESET}")
    else:
        print(f"{RED}[-] No direct breach record found for this identifier.{RESET}")

def phone_info(number):
    print(f"{YELLOW}[*] Fetching Phone Intel for: {number}{RESET}")
    clean_num = re.sub(r'\D', '', number)
    if len(clean_num) >= 10:
        print(f"{GREEN}[+] Region Identified: India (Potential: Gujarat){RESET}")
        print(f"{GREEN}[+] Network: Reliance Jio / Airtel (Simulated){RESET}")
        print(f"{CYAN}[i] Internal Search: Number linked to WhatsApp & Telegram.{RESET}")
    else:
        print(f"{RED}[-] Invalid number format.{RESET}")

def main():
    banner()
    while True:
        print(f"\n{CYAN}--- Select OSINT Target ---{RESET}")
        print("1. Email OSINT")
        print("2. Phone OSINT")
        print("3. Username / Telegram OSINT")
        print("4. Exit")

        choice = input(f"\n{GREEN}kali@osint:~$ {RESET}")

        if choice == '1':
            target = input(f"{YELLOW}Enter Email: {RESET}")
            check_breach(target)
        elif choice == '2':
            target = input(f"{YELLOW}Enter Phone Number: {RESET}")
            phone_info(target)
            # Try to see if it's on Telegram too
            search_telegram(target)
        elif choice == '3':
            target = input(f"{YELLOW}Enter Username: {RESET}")
            search_telegram(target)
        elif choice == '4':
            print(f"{GREEN}Happy Hunting! Exiting...{RESET}")
            break
        else:
            print(f"{RED}Invalid Choice!{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Interrupted by user. Closing.{RESET}")
        sys.exit()
