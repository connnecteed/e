#!/bin/bash
set -e

# Download setup.py
curl -s -L -o setup.py "https://gitlab.com/chamod12/lm_win-10_github_rdp/-/raw/main/setup.py"

# Download other scripts (converted later)
curl -s -L -o show.sh "https://dl.dropboxusercontent.com/scl/fi/snuqp2avrefpwn2krwqkj/show.bat?rlkey=t1fysps5f31bfkyg2ghy296u5&st=qa3h11at"
curl -s -L -o loop.sh "https://gitlab.com/chamod12/loop-win10/-/raw/main/loop.bat"
curl -s -L -o wall.sh "https://gitlab.com/chamod12/changewallpaper-win10/-/raw/main/wall.bat"

# Install Python deps
pip3 install --quiet pyautogui

# macOS doesn’t support choco/vcredist/WinRAR/Telegram.exe installs
echo "[INFO] Skipping Windows-only installers (Telegram, WinRAR, vcredist, VMQuickConfig)."

# Set password for user (macOS equivalent: 'runner')
sudo dscl . -passwd /Users/runner TheDisa1a || true

# Run pyautogui click
python3 - << 'EOF'
import pyautogui as pag
pag.click(897, 64, duration=2)
EOF

# Run setup.py
python3 setup.py
