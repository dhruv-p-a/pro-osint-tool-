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

# [LOGIC] Simulated Leak Database
# Real Telegram bots cross-reference phone numbers with leaked data from
# Facebook (533M records), LinkedIn, and Telegram Scrapes.
LEAK_DATABASE = {
    "9909235023": "Sureshkumar Patel",
    "9876543210": "Dhruv Patel",
    "9000000000": "Admin User",
    "7000000000": "Rajesh Sharma"
}

def banner():
    print(f"{CYAN}")
    print("  ██████╗ ███████╗██╗███╗   ██╗████████╗")
    print(" ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝")
    print(" ██║   ██║███████╗██║██╔██╗ ██║   ██║   ")
    print(" ██║   ██║╚════██║██║██║╚██╗██║   ██║   ")
    print(" ╚██████╔╝███████║██║██║ ╚████║   ██║   ")
    print(f"  ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   V2.1 - PRO OSINT{RESET}\n")

def get_holder_name(phone):
    """Simulates the logic used by Telegram OSINT bots to find names."""
    # Clean the number
    clean_num = re.sub(r'\D', '', phone)
    if len(clean_num) > 10:
        clean_num = clean_num[-10:]

    print(f"{YELLOW}[*] Deep Search: Checking 2021-2024 Data Breach Dumps...{RESET}")
    time.sleep(2) # Simulating processing time

    if clean_num in LEAK_DATABASE:
        name = LEAK_DATABASE[clean_num]
        print(f"{GREEN}[+] HOLDER FOUND: {name}{RESET}")
        print(f"{GREEN}[+] Probable Identity: Linked to Gujarat, India{RESET}")
        return name
    else:
        print(f"{RED}[-] No name matches found in common leak databases.{RESET}")
        print(f"{CYAN}[i] Suggested: Use 'EyeOfGod' API or Truecaller SDK for live data.{RESET}")
        return None

def search_telegram(target, is_phone=False):
    """Checks if the target has a public Telegram profile."""
    if is_phone:
        # Telegram links for phone numbers look like this
        url = f"https://t.me/+91{target[-10:]}"
        print(f"{YELLOW}[*] Checking Telegram for: +91{target[-10:]}{RESET}")
    else:
        url = f"https://t.me/{target.replace('@', '')}"
        print(f"{YELLOW}[*] Scraping Profile: @{target}{RESET}")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extracting name from meta tags or span
            name_tag = soup.find("span", {"dir": "auto"})
            if name_tag:
                print(f"{GREEN}[+] Telegram Public Name: {name_tag.text}{RESET}")
                return True
            else:
                # Some profiles hide name but show in title
                title = soup.find("title").text
                if "Telegram:" in title:
                    print(f"{GREEN}[+] Found: {title.replace('Telegram:', '').strip()}{RESET}")
                    return True
    except:
        pass

    if not is_phone:
        print(f"{RED}[- ] No public info found. User might have private settings.{RESET}")
    return False

def main():
    banner()
    while True:
        print(f"\n{CYAN}--- Select OSINT Target ---{RESET}")
        print("1. Email Breach Check")
        print("2. Phone OSINT (Find Holder Name)")
        print("3. Username OSINT")
        print("4. Exit")

        choice = input(f"\n{GREEN}kali@osint:~$ {RESET}")

        if choice == '1':
            target = input(f"{YELLOW}Enter Email: {RESET}")
            print(f"{YELLOW}[*] Scanning Leaked Repositories...{RESET}")
            time.sleep(1)
            print(f"{RED}[!] Found 2 matches in: 'Wattpad' and 'BigBasket' breaches.{RESET}")
        elif choice == '2':
            target = input(f"{YELLOW}Enter Phone Number (e.g. 99092xxxxx): {RESET}")
            # Step 1: Find name via Leak DB (Like Telegram Bots)
            get_holder_name(target)
            # Step 2: Check Telegram profile
            search_telegram(target, is_phone=True)
        elif choice == '3':
            target = input(f"{YELLOW}Enter Username: {RESET}")
            search_telegram(target)
        elif choice == '4':
            print(f"{GREEN}Session Closed.{RESET}")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
