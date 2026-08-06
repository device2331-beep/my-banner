# Mehidi Bro - Cyber Security Banner

একটি সিম্পল Python স্ক্রিপ্ট যা Termux/টার্মিনালে একটি কালারফুল ASCII ব্যানার দেখায়। এটি শুধুমাত্র ডেকোরেশন/স্টাইলিং এর জন্য — এর সাথে কোনো নিরাপত্তা বা হ্যাকিং টুলের সম্পর্ক নেই।

**GitHub Repo:** https://github.com/device2331-beep/my-banner

## প্রিভিউ

```
 __  __     _    _    _ _   ___
|  \/  |___| |_ (_)__| (_) | _ )_ _ ___
| |\/| / -_) ' \| / _` | | | _ \ '_/ _ \
|_|  |_\___|_||_|_\__,_|_| |___/_| \___/

╔════════════════════════╗
║ Cyber Security Service ║
╚════════════════════════╝

[✔] System....: Online
[✔] User......: Mehidi62
[✔] Access....: Root Learner
[✔] Date......: 06 Aug 2026 | 07:27
--------------------------
🔥 MEHIDI_LINUX INFO 🔥
Developer: Mehidi Hassan
Version: 3.0
GUI: No (CLI Only)
✅ MEHIDI_LINUX loaded! Welcome Mehidi! 🔥
```

## ফিচার

- রঙিন (ANSI color) ASCII আর্ট ব্যানার
- বর্তমান তারিখ ও সময় অটোমেটিক দেখায়
- Developer info ও ভার্সন তথ্য
- Termux/Linux টার্মিনালে সরাসরি রান করা যায়

## প্রয়োজনীয়তা

- Python 3
- Git (GitHub থেকে ক্লোন/পুশ করার জন্য)

## প্যাকেজ ইনস্টল (Termux)

```bash
pkg update -y
pkg upgrade -y
pkg install python -y
pkg install git -y
```

চেক করো:

```bash
python --version
git --version
```

## ইনস্টলেশন

```bash
cd ~
git clone https://github.com/device2331-beep/my-banner.git
cd my-banner
python mehidi_banner.py
```

## Termux ওপেন করলে অটো রান করাতে চাইলে

`.bashrc` ফাইলে এই লাইনটা যোগ করো:

```bash
echo 'python ~/mehidi_banner.py' >> ~/.bashrc
```

এরপর Termux বন্ধ করে আবার খুললেই ব্যানারটি নিজে থেকে দেখাবে।

## Customization

`mehidi_banner.py` ফাইলে নিচের ভ্যারিয়েবলগুলো পরিবর্তন করে তথ্য কাস্টমাইজ করা যাবে:

| ভ্যারিয়েবল | বর্ণনা |
|---|---|
| `GREEN`, `CYAN`, `YELLOW` | টেক্সট কালার (ANSI codes) |
| `ascii_art` | মূল লোগো/আর্ট |
| User/Version/Developer লাইন | `print()` স্টেটমেন্টের ভিতরে সরাসরি এডিট করা যাবে |

## ডেভেলপার

**Mehidi Hassan** (Mehidi62) — Self-taught Android/Termux based learner

## License

ব্যক্তিগত ব্যবহারের জন্য — Free to modify.
