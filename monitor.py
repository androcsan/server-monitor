import psutil
import os
import time
from datetime import datetime


# Thresholds
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80


def get_system_usage():
    print("--- Server Resource Monitor ---")

    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"* CPU Usage: {cpu_usage}%")

    # RAM
    mem = psutil.virtual_memory()
    print(f"* Memory Usage: {mem.percent}%")
    print(f"  - Total: {round(mem.total / (1024**3), 2)} GB")
    print(f"  - Used: {round(mem.used / (1024**3), 2)} GB")
    print(f"  - Available: {round(mem.available / (1024**3), 2)} GB")

    # Disk
    disk = psutil.disk_usage(os.sep)
    print(f"* Disk Usage: {disk.percent}%")
    print(f"  - Total: {round(disk.total / (1024**3), 2)} GB")
    print(f"  - Used: {round(disk.used / (1024**3), 2)} GB")
    print(f"  - Free: {round(disk.free / (1024**3), 2)} GB")

    return cpu_usage, mem.percent


def alert(resource: str, usage: float, threshold: float):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'!' * 40}")
    print(f"  ⚠️  ALERT [{timestamp}]")
    print(f"  {resource} usage is at {usage}% — exceeded threshold of {threshold}%!")
    print(f"{'!' * 40}\n")


def monitor(interval: int = 5, max_checks: int = None):
    print(
        f"Monitoring started. Alerts trigger above CPU>{CPU_THRESHOLD}% / RAM>{RAM_THRESHOLD}%\n")
    checks = 0

    while True:
        cpu_usage, ram_usage = get_system_usage()

        if cpu_usage > CPU_THRESHOLD:
            alert("CPU", cpu_usage, CPU_THRESHOLD)

        if ram_usage > RAM_THRESHOLD:
            alert("RAM", ram_usage, RAM_THRESHOLD)

        checks += 1
        if max_checks is not None and checks >= max_checks:
            print("Max checks reached. Stopping monitor.")
            break

        print(f"\nNext check in {interval} seconds...\n")
        time.sleep(interval)


if __name__ == "__main__":
    monitor(interval=5)
