import psutil
import time
import socket
import os
import signal

threshold_percentage = 50
included_processes = ['CTFarm']  # No .exe on macOS, just the process name
computer_name = socket.gethostname()
log_file = f"{computer_name}.txt"

def log_cpu_usage():
    with open(log_file, "a") as f:
        for process in psutil.process_iter(['name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']
            if cpu_percent > threshold_percentage and process_name not in ['kernel_task', 'python3']:
                f.write(f"{process_name} : {cpu_percent}%\n")

def main():
    while True:
        processes_exceeded_threshold = False
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            process_name = process.info['name']
            cpu_percent = process.info['cpu_percent']

            # Terminate included processes
            if process_name in included_processes:
                print(f"Process to be terminated: {process_name} (CPU Usage: {cpu_percent}%)")
                try:
                    os.kill(process.info['pid'], signal.SIGKILL)  # Force kill
                    print(f"Terminated process: {process_name}")
                except Exception as e:
                    print(f"Failed to terminate process {process_name}: {e}")

            # Log if CPU usage exceeded
            if cpu_percent > threshold_percentage:
                processes_exceeded_threshold = True

        if processes_exceeded_threshold:
            log_cpu_usage()

        time.sleep(10)

if __name__ == "__main__":
    main()
