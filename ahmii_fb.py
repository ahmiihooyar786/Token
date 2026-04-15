import os, sys, time, requests, hashlib, json, re
from datetime import datetime

# --- COLORS ---
G = '\x1b[38;5;46m' # Green
Y = '\x1b[38;5;220m' # Yellow
R = '\x1b[38;5;196m' # Red
W = '\x1b[1;37m' # White
B = '\x1b[38;5;45m' # Blue

# --- SETTINGS ---
key_url = "https://raw.githubusercontent.com/ahmiihooyar786/Token/main/key.json"
remaining_time = "Premium"

def ____banner____():
    os.system('clear')
    print(f"""{G}
 █████╗ ██╗  ██╗███╗   ███╗██╗██╗
██╔══██╗██║  ██║████╗ ████║██║██║
███████║███████║██╔████╔██║██║██║
██╔══██║██╔══██║██║╚██╔╝██║██║██║
██║  ██║██║  ██║██║ ╚═╝ ██║██║██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝
{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{G} [•] {W}OWNER    : {Y}AHMAD ALI (RDX)
{G} [•] {W}TOOL     : {Y}FB TOKEN MASTER (VIP)
{G} [•] {W}STATUS   : {Y}{remaining_time} ✅
{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m""")

def check_token_live(token):
    """Token ki live details nikalne ke liye"""
    try:
        data = requests.get(f"https://graph.facebook.com/me?access_token={token}").json()
        if 'name' in data:
            return True, data['name'], data['id']
        else:
            return False, None, None
    except:
        return False, None, None

def token_checker_menu():
    ____banner____()
    print(f"{B} [ TOKEN REAL-TIME CHECKER ]")
    print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    token = input(f"{G} [•] PASTE TOKEN : {W}")
    print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"{G} [!] CHECKING STATUS...{W}")
    time.sleep(2)
    
    is_live, name, fbid = check_token_live(token)
    
    if is_live:
        print(f"{G} [✓] STATUS  : LIVE")
        print(f"{G} [✓] NAME    : {name}")
        print(f"{G} [✓] FB ID   : {fbid}")
        print(f"{G} [✓] DETAILS : Token is active and working.")
    else:
        print(f"{R} [×] STATUS  : DEAD / EXPIRED")
        print(f"{R} [×] MESSAGE : Please generate a new token.")
    
    input(f"\n{Y} [ Press Enter To Back ]")
    main_menu()

def main_menu():
    ____banner____()
    print(f"{W} [1] GET FB TOKEN (EAAG/EAAB)")
    print(f"{W} [2] CHECK TOKEN STATUS (REAL-TIME)")
    print(f"{W} [3] TOKEN REMOVE/LOGOUT")
    print(f"{W} [4] CONTACT OWNER")
    print(f"{W} [0] EXIT")
    print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    opt = input(f"{G} [•] SELECT OPTION : {W}")
    
    if opt == '1':
        # Token nikalne wala section
        ____banner____()
        print(f"{B} [ TOKEN EXTRACTOR SECTION ]")
        uid = input(f"{G} [•] EMAIL/ID : {W}")
        pas = input(f"{G} [•] PASSWORD : {W}")
        # Yahan aap apna extraction logic daal dein
        print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G} [✓] Token Generated (Simulation)")
        main_menu()
    elif opt == '2':
        token_checker_menu()
    elif opt == '4':
        os.system("xdg-open https://wa.me/+92xxxxxxxxx")
        main_menu()
    else:
        sys.exit()

if __name__ == "__main__":
    main_menu()
    
