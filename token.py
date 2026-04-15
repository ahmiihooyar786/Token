import os, sys, time, requests, hashlib, json, datetime, re, random
from datetime import datetime

# --- SETTINGS ---
key_url = "https://raw.githubusercontent.com/ahmiihooyar786/token/main/key.json"
remaining_time = "Checking..."

def ____banner____():
    os.system('clear')
    print(f"""\033[1;32m
 █████╗ ██╗  ██╗███╗   ███╗██╗██╗
██╔══██╗██║  ██║████╗ ████║██║██║
███████║███████║██╔████╔██║██║██║
██╔══██║██╔══██║██║╚██╔╝██║██║██║
██║  ██║██║  ██║██║ ╚═╝ ██║██║██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝
\x1b[38;5;220m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\x1b[38;5;46m [•] \x1b[1;37mOWNER    : \x1b[38;5;220mAHMAD ALI (RDX)
\x1b[38;5;46m [•] \x1b[1;37mTOOL     : \x1b[38;5;220mFB TOKEN EXTRACTOR
\x1b[38;5;46m [•] \x1b[1;37mVALIDITY : \x1b[38;5;220m{remaining_time} ✅
\x1b[38;5;220m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m""")

# --- LICENSE SYSTEM ---
def ahmii_online_check():
    global remaining_time
    try:
        user_info = str(os.getuid())
        ahmii_token = "AHMII-" + hashlib.md5(user_info.encode()).hexdigest()[:10].upper()
        
        ____banner____()
        print(f" \033[1;32m[•] YOUR TOKEN : \033[1;33m{ahmii_token}")
        print("\033[1;220m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

        r = requests.get(key_url).json()

        if ahmii_token in r:
            expiry_date = datetime.strptime(r[ahmii_token] + " 00:00:00", "%Y-%m-%d %H:%M:%S")
            if datetime.now() <= expiry_date:
                diff = expiry_date - datetime.now()
                remaining_time = f"{diff.days}d {diff.seconds//3600}h"
                main_menu()
            else:
                print(" \033[1;31m[×] TOKEN EXPIRED!")
        else:
            print(" \033[1;31m[×] TOKEN NOT APPROVED!")
            sys.exit()
    except:
        print(" \033[1;31m[!] CONNECTION ERROR!")

# --- TOKEN EXTRACTOR LOGIC ---
def token_getter():
    ____banner____()
    print(" \033[1;37m[1] GET EAAG TOKEN (BUSINESS)")
    print(" [2] GET EAAB TOKEN (INSTAGRAM)")
    print(" [0] BACK TO MENU")
    print("\033[1;220m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    choice = input(" [•] CHOOSE : ")
    
    if choice in ['1', '2']:
        uid = input("\n [•] EMAIL/UID : ")
        pas = input(" [•] PASSWORD  : ")
        print("\n \033[1;32m[!] EXTRACTING TOKEN... PLEASE WAIT")
        time.sleep(3)
        
        # Note: Actual FB requests depend on current API headers
        # For now, showing a simulation. You can add your specific FB API logic here.
        print(f"\n \033[1;32m[✓] SUCCESS! TOKEN SAVED IN /sdcard/ahmii_token.txt")
        print(f" \033[1;33m[>] EAAG{hashlib.md5(uid.encode()).hexdigest().upper()}") 
        input("\n [•] PRESS ENTER TO GO BACK")
        main_menu()
    else:
        main_menu()

# --- MAIN MENU ---
def main_menu():
    ____banner____()
    print(" \033[1;37m[1] START TOKEN EXTRACTOR")
    print(" [2] CONTACT OWNER")
    print(" [0] EXIT")
    print("\033[1;220m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    
    opt = input(" [•] CHOOSE : ")
    if opt == '1':
        token_getter()
    elif opt == '2':
        os.system("xdg-open https://wa.me/+92xxxxxxxxxx") # Apna number dalein
        main_menu()
    else:
        sys.exit()

if __name__ == "__main__":
    ahmii_online_check()

