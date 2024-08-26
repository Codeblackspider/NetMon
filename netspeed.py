import psutil
import time
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Tool details
TOOL_NAME = "NetMon"
VERSION = "1.0"
AUTHOR = "fontbees"
WEBSITE = "https://www.fontbees.store"

def print_gradient_title():
    title_lines = [
        "    _   __     __  __  ___",
        "   / | / /__  / /_/  |/  /___  ____ ",
        "  /  |/ / _ \\/ __/ /|_/ / __ \\/ __ \\",
        " / /|  /  __/ /_/ /  / / /_/ / / / /",
        "/_/ |_|\\___/\\__/_/  /_/\\____/_/ /_/"
    ]
    
    # Print each line with gradient effect
    gradient_colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN]
    
    for line in title_lines:
        # Create gradient effect by cycling through colors
        colored_line = ""
        for index, char in enumerate(line):
            color = gradient_colors[index % len(gradient_colors)]
            colored_line += color + char
        print(Style.BRIGHT + colored_line + Style.RESET_ALL)

def get_network_io():
    io_counters = psutil.net_io_counters()
    return io_counters.bytes_sent, io_counters.bytes_recv

def monitor_bandwidth(interval=1):
    # Display the gradient title
    print_gradient_title()
    
    # Display tool information with colors
    print(f"{Fore.GREEN}{TOOL_NAME} - Network Bandwidth Monitor (Version: {VERSION})")
    print(f"{Fore.YELLOW}Author: {AUTHOR}")
    print(f"{Fore.YELLOW}Website: {WEBSITE}")
    print(f"{Fore.BLUE}{'=' * 60}")
    print(f"{Fore.MAGENTA}{'Time':<8} {'Bytes Sent':<15} {'Bytes Received':<15} {'Upload Speed (bytes/s)':<25} {'Download Speed (bytes/s)':<25}")
    
    prev_sent, prev_recv = get_network_io()
    while True:
        time.sleep(interval)
        curr_sent, curr_recv = get_network_io()
        upload_speed = (curr_sent - prev_sent) / interval
        download_speed = (curr_recv - prev_recv) / interval
        print(f"{time.strftime('%H:%M:%S'):<8} {curr_sent:<15} {curr_recv:<15} {upload_speed:<25} {download_speed:<25}")
        prev_sent, prev_recv = curr_sent, curr_recv

if __name__ == "__main__":
    monitor_bandwidth()
