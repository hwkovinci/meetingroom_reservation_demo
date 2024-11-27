#!/usr/bin/env python3

import argparse
import subprocess
import time
import os
import sys

def start_emulator(avd_name):
    print(f"Starting emulator '{avd_name}'...")
    emulator_path = os.path.expanduser("~/Android/Sdk/emulator/emulator")
    process = subprocess.Popen([emulator_path, "-avd", avd_name, "-no-snapshot-load"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for emulator to boot
    boot_completed = False
    while not boot_completed:
        result = subprocess.run(
            ["adb", "shell", "getprop", "sys.boot_completed"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.stdout.strip() == "1":
            boot_completed = True
        else:
            print("Waiting for emulator to boot...")
            time.sleep(5)
    print("Emulator started.")

def close_emulator():
    print("Closing emulator...")
    subprocess.run(["adb", "emu", "kill"])
    print("Emulator closed.")

def main():
    parser = argparse.ArgumentParser(description="Manage Android Emulator.")
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Start emulator
    parser_start = subparsers.add_parser('start', help='Start the emulator')
    parser_start.add_argument('--avd-name', required=True, help='Name of the AVD to start')

    # Close emulator
    parser_close = subparsers.add_parser('close', help='Close the emulator')

    args = parser.parse_args()

    if args.command == 'start':
        start_emulator(args.avd_name)
    elif args.command == 'close':
        close_emulator()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
