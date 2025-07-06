TELEGRAM MEMBER ADDER TOOL - NEHAL DARK TRAP

Author: NEHAL DARK TRAP

YouTube: https://youtube.com/@nehal_dark_trap?si=sjL1_iRpN7ByqneE

Instagram: https://www.instagram.com/nehal_dark_trap?igsh=b2YxMDJnbjlzcm5r

import os import time import webbrowser from telethon.sync import TelegramClient from telethon.tl.functions.channels import InviteToChannelRequest

Background Sound (Optional if installed)

def play_sound(): try: os.system("mpv sound.mp3 --no-video > /dev/null 2>&1 &") except: pass

Banner

def banner(): os.system('clear') print("\033[1;31m=============================") print("     TELEGRAM MEMBER ADDER") print("=============================") print("Login with phone number: +8801XXXXXXX") print("TOLL OWNER NEHAL DARK TRAP") print("Insta: nehal_dark_trap") print("YT: NEHAL DARK TRAP") print("=============================\033[0m")

Startup Animation

def animate_start(): play_sound() for i in range(3): print("\033[1;32m[+] Loading Tool" + "." * (i+1) + "\033[0m") time.sleep(1) os.system('clear')

Subscription Step

def subscription_check(): banner() print("\033[1;33mTo run this tool, subscribe to our YouTube channel first.\033[0m") print("1. Subscribe Channel") print("2. Already Subscribed") choice = input("Enter your choice (1/2): ") if choice == '1': webbrowser.open("https://youtube.com/@nehal_dark_trap?si=sjL1_iRpN7ByqneE") input("\nAfter subscribing, press Enter to continue...") elif choice != '2': print("\nInvalid choice. Exiting...") exit()

Main Menu

def main_menu(): while True: banner() print("\033[1;36m1. Join Telegram Group") print("2. Follow on Instagram") print("3. Add Members to Telegram Group\033[0m") choice = input("\nEnter your choice (1/2/3): ")

if choice == '1':
        webbrowser.open("https://t.me/NEHAL_DARK_TRAP")
    elif choice == '2':
        webbrowser.open("https://www.instagram.com/nehal_dark_trap?igsh=b2YxMDJnbjlzcm5r")
    elif choice == '3':
        add_members()
    else:
        print("\nInvalid choice. Try again.")
        time.sleep(1)

Add Members Function

def add_members(): api_id = int(input("Enter your Telegram API ID: ")) api_hash = input("Enter your Telegram API HASH: ") phone = input("Enter your Telegram phone number: ")

client = TelegramClient('session', api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code you received: '))

group = input("Enter Group/Channel ID (e.g., -100123456789): ")
userfile = input("Enter Username List File (e.g., users.txt): ")

users = []
with open(userfile, 'r') as f:
    users = [line.strip() for line in f if line.strip()]

for user in users:
    try:
        print(f"[✓] Adding {user}...")
        client(InviteToChannelRequest(group, [user]))
        time.sleep(3)  # sleep to avoid flood
    except Exception as e:
        print(f"[✗] Failed to add {user}: {e}")

print("\n[!] Task Completed. All possible users processed.")
client.disconnect()

Run Tool

animate_start() subscription_check() main_menu()
