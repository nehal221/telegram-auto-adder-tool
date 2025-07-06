import os
import time
import webbrowser
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest

# Sound effect (optional)
def play_sound():
    try:
        os.system("mpv sound.mp3 --no-video > /dev/null 2>&1 &")
    except:
        pass

# Startup animation
def animate_start():
    play_sound()
    for i in range(3):
        print(f"\033[1;32m[+] Loading Tool{'.' * (i + 1)}\033[0m")
        time.sleep(1)
    os.system("clear")

# Tool banner
def banner():
    os.system("clear")
    print("\033[1;31m=============================")
    print("     TELEGRAM MEMBER ADDER")
    print("=============================")
    print("Login with phone number: +8801XXXXXXX")
    print("TOLL OWNER: NEHAL DARK TRAP")
    print("INSTA: nehal_dark_trap")
    print("YT: NEHAL DARK TRAP")
    print("=============================\033[0m")

# Open browser link
def open_link(link):
    try:
        os.system(f"xdg-open '{link}' > /dev/null 2>&1 &")
    except:
        webbrowser.open(link)

# Subscription lock
def subscription_lock():
    while True:
        banner()
        print("\033[1;32m1. Subscribe Channel")
        print("2. Already Subscribed\033[0m")
        print("\033[1;31m", end="")
        choice = input("Enter your choice (1/2): ")
        print("\033[0m", end="")

        if choice == "1":
            print("🔁 Opening YouTube Channel...")
            open_link("https://youtube.com/@nehal_dark_trap?si=CGE96-qu0BhVGHvi")
            print("📌 After subscribing, select 2 to continue.")
            time.sleep(2)
        elif choice == "2":
            break
        else:
            print("❌ Invalid input. Try again.")
            time.sleep(1)

# Main menu
def main_menu():
    while True:
        banner()
        print("\033[1;36m1. Join Telegram Group")
        print("2. Follow on Instagram")
        print("3. Add All Members Automatically\033[0m")
        print("\033[1;31m", end="")
        choice = input("Enter your choice (1/2/3): ")
        print("\033[0m", end="")

        if choice == "1":
            open_link("https://t.me/NEHAL_DARK_TRAP")
        elif choice == "2":
            open_link("https://www.instagram.com/nehal_dark_trap?igsh=b2YxMDJnbjlzcm5r")
        elif choice == "3":
            add_all_members()
        else:
            print("❌ Invalid input.")
            time.sleep(1)

# Add all members from users.txt
def add_all_members():
    api_id = int(input("Enter Telegram API ID: "))
    api_hash = input("Enter Telegram API HASH: ")
    phone = input("Enter your Telegram Phone Number: ")

    client = TelegramClient('auto-adder-session', api_id, api_hash)
    client.connect()

    if not client.is_user_authorized():
        client.send_code_request(phone)
        code = input("Enter the code you received: ")
        client.sign_in(phone, code)

    group = input("Enter Group/Channel ID (e.g., -1001234567890): ")
    userfile = input("Enter Username List File (e.g., users.txt): ")

    with open(userfile, 'r') as f:
        users = [line.strip() for line in f if line.strip()]

    success = 0
    failed = 0

    for user in users:
        try:
            print(f"[✓] Adding {user}...")
            client(InviteToChannelRequest(group, [user]))
            success += 1
            time.sleep(3)  # avoid spam
        except Exception as e:
            print(f"[✗] Failed to add {user}: {e}")
            failed += 1
            time.sleep(2)

    print(f"\n✅ All done!\nAdded: {success} users\nFailed: {failed}")
    client.disconnect()

# Run the tool
animate_start()
subscription_lock()
main_menu()
