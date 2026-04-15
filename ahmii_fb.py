import os, sys, time, requests, hashlib, json, re, uuid, random
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
    else:
        print(f"{R} [×] STATUS  : DEAD / EXPIRED")
    
    input(f"\n{Y} [ Press Enter To Back ]")
    main_menu()

def main_menu():
    ____banner____()
    print(f"{W} [1] GET FB TOKEN")
    print(f"{W} [2] CHECK TOKEN STATUS (REAL-TIME)")
    print(f"{W} [3] CONTACT OWNER")
    print(f"{W} [0] EXIT")
    print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    
    opt = input(f"{G} [•] SELECT OPTION : {W}")
    
    if opt == '1':
        ____banner____()
        print(f"{B} [ FB TOKEN EXTRACTOR ]")
        print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        uid = input(f"{G} [•] EMAIL/ID : {W}")
        pas = input(f"{G} [•] PASSWORD : {W}")
        print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G} [!] LOGGING IN... PLEASE WAIT")
        
        try:
            sess = requests.Session()
            ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
            head = {
                "User-Agent": ua,
                "Host": "graph.facebook.com",
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            }
            data = {
                "adid": str(uuid.uuid4()),
                "email": uid,
                "password": pas,
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "cpl": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "generate_session_cookies": "1",
                "error_detail_type": "button_with_disabled",
                "source": "login",
                "method": "auth.login"
            }
            
            res = sess.post("https://graph.facebook.com/auth/login", data=data, headers=head).json()
            
            if "access_token" in res:
                token = res["access_token"]
                print(f"{G} [✓] LOGIN SUCCESSFUL!")
                print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"{G} [>] FB TOKEN : {W}{token}")
                open("/sdcard/ahmii_token.txt", "w").write(token)
                print(f"{G} [!] Saved in /sdcard/ahmii_token.txt")
            elif "error" in res:
                print(f"{R} [×] LOGIN FAILED!")
                print(f"{R} [!] REASON: {res['error']['message']}")
            else:
                print(f"{R} [×] UNKNOWN ERROR!")
        except Exception as e:
            print(f"{R} [×] NETWORK ERROR: {e}")

        input(f"\n{Y} [ Press Enter To Back ]")
        main_menu()

    elif opt == '2':
        token_checker_menu()
    elif opt == '3':
        os.system("xdg-open https://wa.me/+923277348009")
        main_menu()
    else:
        sys.exit()

if __name__ == "__main__":
    main_menu()
