#!/usr/bin/env python3

import argparse
import subprocess
import sys

def install_apk(apk_path):
    print(f"Installing APK '{apk_path}'...")
    result = subprocess.run(["adb", "install", "-r", apk_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if "Success" in result.stdout:
        print("APK installed successfully.")
    else:
        print("Failed to install APK:")
        print(result.stdout)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Install APK on Android Emulator.")
    parser.add_argument('--apk-path', required=True, help='Path to the APK file to install')

    args = parser.parse_args()
    install_apk(args.apk_path)

if __name__ == "__main__":
    main()
