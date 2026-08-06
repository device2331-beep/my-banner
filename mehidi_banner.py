#!/usr/bin/env python3
"""
Mehidi Bro - Cyber Security Service Banner
Author: Mehidi Hassan
"""

import datetime

# ANSI color codes
GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
BOLD = "\033[1m"
RESET = "\033[0m"


def show_banner():
    ascii_art = r"""
 __  __     _    _    _ _   ___
|  \/  |___| |_ (_)__| (_) | _ )_ _ ___
| |\/| / -_) ' \| / _` | | | _ \ '_/ _ \
|_|  |_\___|_||_|_\__,_|_| |___/_| \___/
"""
    print(GREEN + ascii_art + RESET)

    print(GREEN + "╔════════════════════════╗" + RESET)
    print(GREEN + "║ Cyber Security Service ║" + RESET)
    print(GREEN + "╚════════════════════════╝" + RESET)
    print()

    now = datetime.datetime.now().strftime("%d %b %Y | %H:%M")

    print(GREEN + "[✔] System....: Online" + RESET)
    print(GREEN + "[✔] User......: Mehidi62" + RESET)
    print(GREEN + "[✔] Access....: Root Learner" + RESET)
    print(GREEN + f"[✔] Date......: {now}" + RESET)
    print(GREEN + "-" * 26 + RESET)

    print(CYAN + "🔥 MEHIDI_LINUX INFO 🔥" + RESET)
    print(GREEN + "Developer: Mehidi Hassan" + RESET)
    print(GREEN + "Version: 3.0" + RESET)
    print(GREEN + "GUI: No (CLI Only)" + RESET)
    print(GREEN + "✅ MEHIDI_LINUX loaded! Welcome Mehidi! 🔥" + RESET)
    print()


if __name__ == "__main__":
    show_banner()
