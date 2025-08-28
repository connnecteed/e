import os
import subprocess
import requests
import platform
arch = platform.machine()

print("arch:", arch)
def install_rustdesk():
    if arch == "x86_64":
        pkg_url = "https://github.com/rustdesk/rustdesk/releases/latest/download/rustdesk-1.3.6-x86_64.pkg"
    elif arch == "arm64" or arch == "aarch64":
        pkg_url = "https://github.com/rustdesk/rustdesk/releases/latest/download/rustdesk-1.3.6-aarch64.pkg"
    else:
        raise RuntimeError(f"Unsupported architecture: {arch}")

    pkg_file = "rustdesk.pkg"
    print(f"Downloading RustDesk for {arch}...")
    subprocess.run(["curl", "-L", "-o", pkg_file, pkg_url], check=True)
    subprocess.run(["sudo", "installer", "-pkg", pkg_file, "-target", "/"], check=True)
    print("RustDesk installed successfully.")


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
    print("Starting RustDesk...")
    subprocess.run(["open", "-a", "RustDesk"], check=True)


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
    show_id_or_ip()
