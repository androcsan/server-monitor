import psutil
import os


def get_system_usage():
    print("--- Server Resource Monitor")

    # CPU to
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


# Pang Call ng System Usage
if __name__ == "__main__":
    get_system_usage()
