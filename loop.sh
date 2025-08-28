#!/bin/bash
set -e
pip3 install --quiet psutil requests
curl -s -L -o loop.py https://gitlab.com/chamod12/loop-win10/-/raw/main/loop.py
python3 loop.py
