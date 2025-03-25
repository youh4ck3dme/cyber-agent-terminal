#!/data/data/com.termux/files/usr/bin/bash

echo "[*] Aktualizujem systém..."
pkg update -y && pkg upgrade -y

echo "[*] Inštalujem závislosti..."
pkg install -y python git termux-api
pip install --upgrade pip
pip install python-telegram-bot==13.15 requests

echo "[*] Klonujem CyberAgent repozitár..."
git clone https://github.com/youh4ck3dme/cyber-agent-terminal ~/cyber-agent-terminal || {
    echo "[!] Repozitár sa nepodarilo klonovať. Over URL alebo pripojenie."
    exit 1
}

cd ~/cyber-agent-terminal

echo "[*] Nastavujem oprávnenia a spúšťam agenta..."
chmod +x *.sh *.py
termux-wake-lock
nohup python3 agent.py &
nohup python3 telegram_bot.py &

echo "[+] CyberAgent TERMINAL je spustený a pripravený!"
