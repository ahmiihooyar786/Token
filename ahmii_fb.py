import os, sys, time, requests, re, uuid, random
from datetime import datetime

# COLORS
G = '\x1b[38;5;46m'
Y = '\x1b[38;5;220m'
W = '\x1b[1;37m'
R = '\x1b[38;5;196m'

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
{G} [•] {W}TOOL     : {Y}FB TOKEN MASTER
{G} [•] {W}STATUS   : {Y}VIP ACCESS ✅
{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m""")

def get_token():
    ____banner____()
    print(f"{G} [ FB TOKEN EXTRACTOR ]")
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
            # Mobile storage mein save karna
            if os.path.exists('/sdcard'):
                open("/sdcard/ahmii_token.txt", "w").write(token)
                print(f"{G} [!] Token saved in /sdcard/ahmii_token.txt")
        elif "error" in res:
            print(f"{R} [×] LOGIN FAILED!")
            print(f"{R} [!] REASON: {res['error']['message']}")
        else:
            print(f"{R} [×] UNKNOWN ERROR!")
    except Exception as e:
        print(f"{R} [×] NETWORK ERROR: {e}")

    input(f"\n{Y} [ Press Enter To Back ]")
    main_menu()

def main_menu():
    ____banner____()
    print(f"{W} [1] GET FB TOKEN")
    print(f"{W} [2] CONTACT OWNER")
    print(f"{W} [0] EXIT")
    print(f"{Y}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    opt = input(f"{G} [•] SELECT : {W}")
    if opt == '1':
        get_token()
    elif opt == '2':
        os.system("xdg-open https://wa.me/+923277348009")
        main_menu()
    else:
        sys.exit()
        
