import os
import subprocess
import platform
import requests
import shutil
import time

arch = platform.machine()
print("Detected architecture:", arch)

def install_rustdesk():
    if arch == "x86_64":
        dmg_url = "https://github.com/rustdesk/rustdesk/releases/download/1.4.1/rustdesk-1.4.1-x86_64.dmg"
    elif arch in ["arm64", "aarch64"]:
        dmg_url = "https://github.com/rustdesk/rustdesk/releases/download/1.4.1/rustdesk-1.4.1-aarch64.dmg"
    else:
        raise RuntimeError(f"Unsupported architecture: {arch}")

    dmg_file = "rustdesk.dmg"
    print(f"Downloading RustDesk for {arch}...")
    subprocess.run(["curl", "-fSL", "-o", dmg_file, dmg_url], check=True)

    # Mount the DMG
    mount_point = "/Volumes/RustDesk"
    subprocess.run(["hdiutil", "attach", dmg_file, "-mountpoint", mount_point], check=True)

    # Copy RustDesk.app to ~/Applications
    user_apps = os.path.expanduser("~/Applications")
    os.makedirs(user_apps, exist_ok=True)
    app_path = os.path.join(mount_point, "RustDesk.app")
    if not os.path.exists(app_path):
        raise RuntimeError("RustDesk.app not found in DMG.")
    dest_path = os.path.join(user_apps, "RustDesk.app")
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    shutil.copytree(app_path, dest_path)

    # Unmount DMG
    subprocess.run(["hdiutil", "detach", mount_point], check=True)
    print("RustDesk installed successfully to ~/Applications.")

def configure_rustdesk(password="TheDisa1a"):
    config_dir = os.path.expanduser("~/Library/Application Support/rustdesk")
    os.makedirs(config_dir, exist_ok=True)
    config_file = os.path.join(config_dir, "config.toml")
    config_content = f"""
[options]
password = "{password}"
"""
    with open(config_file, "w") as f:
        f.write(config_content)
    print(f"RustDesk password set to {password}")

def start_rustdesk():
    rustdesk_path = os.path.expanduser("~/Applications/RustDesk.app")
    if not os.path.exists(rustdesk_path):
        raise RuntimeError(f"RustDesk.app not found at {rustdesk_path}")
    print("Starting RustDesk...")
    subprocess.run(["open", "-a", rustdesk_path], check=True)

def show_id_or_ip():
    id_file = os.path.expanduser("~/Library/Application Support/rustdesk/id")
    if os.path.exists(id_file):
        with open(id_file) as f:
            rid = f.read().strip()
        print("RustDesk ID:", rid)
    else:
        try:
            ip = requests.get("https://api.ipify.org").text
            print("RustDesk ID not found. Public IP:", ip)
        except Exception as e:
            print("Could not get public IP:", e)

if __name__ == "__main__":
    install_rustdesk()
    configure_rustdesk()
    start_rustdesk()
    time.sleep(5)
    show_id_or_ip()
