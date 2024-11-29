# proxy_manager.py

import os
import random
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import signal
import sys

# Dynamically construct the file path for portability
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Project root directory
PROXY_FILE = os.path.join(BASE_DIR, "utils", "proxyList.txt")

# Graceful exit function when Ctrl + C is pressed
def signal_handler(sig, frame):
    print("\nExiting gracefully...")
    sys.exit(0)

# Register signal handler for graceful exit on Ctrl + C
signal.signal(signal.SIGINT, signal_handler)

def get_random_proxy():
    """Get a working random proxy from the list."""
    with open(PROXY_FILE, "r") as file:
        proxies = [line.strip() for line in file if line.strip()]
    
    # Shuffle proxies to randomize the selection
    random.shuffle(proxies)

    # Use ThreadPoolExecutor to handle proxies concurrently and efficiently  116.203.135.164:8090
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(is_proxy_working, {"http": "http://" + proxy, "https": "http://" + proxy}) for proxy in proxies]
        
        # Check proxies as they complete
        for future in as_completed(futures):
            try:
                proxy = proxies[futures.index(future)]  # Retrieve the proxy
                if future.result():
                    print(f"Proxy is working: {proxy}")
                    return {"http": proxy, "https": proxy}
                else:
                    print(f"Proxy failed: {proxy}")
            except KeyboardInterrupt:
                print("\nReceived interrupt signal, stopping proxy checking.")
                sys.exit(0)
            except Exception as e:
                print(f"Error while checking proxy: {e}")
    
    print("No working proxy found.")
    return None  # If no working proxy is found, return None

def is_proxy_working(proxy):
    """Test if a proxy is working."""
    try:
        response = requests.get("https://www.google.com", proxies=proxy, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Proxy failed: {proxy}, Error: {e}")
        return False
    except KeyboardInterrupt:
        print("\nInterrupt received during proxy check.")
        sys.exit(0)  # Exit gracefully if interrupted
