#!/usr/bin/env python3

import argparse
import subprocess
import sys
import time
import os
from typing import NoReturn
from dotenv import load_dotenv

load_dotenv()

def start_appium() -> None :
    print("Starting Appium server...")
    appium_process = subprocess.Popen(["appium", "--address", os.getenv("ADRESS"), "--port", os.getenv("PORT")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for Appium server to start
    time.sleep(5)
    with open("appium.pid", "w") as f:
        f.write(str(appium_process.pid))
    print(f"Appium server started with PID {appium_process.pid}.")

def stop_appium() -> None :
    if os.path.exists("appium.pid"):
        with open("appium.pid", "r") as f:
            pid = f.read()
        print(f"Stopping Appium server with PID {pid}...")
        subprocess.run(["kill", pid])
        os.remove("appium.pid")
        print("Appium server stopped.")
    else:
        print("Appium PID file not found.")
        sys.exit(1)

def main() -> None :
    parser = argparse.ArgumentParser(description="Manage Appium Server.")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Start Appium server
    parser_start = subparsers.add_parser('start', help='Start the Appium server')

    # Stop Appium server
    parser_stop = subparsers.add_parser('stop', help='Stop the Appium server')

    args = parser.parse_args()

    if args.command == 'start':
        start_appium()
    elif args.command == 'stop':
        stop_appium()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
