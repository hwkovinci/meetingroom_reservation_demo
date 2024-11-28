#!/bin/bash

# Load configuration
CONFIG_FILE="config.ini"
AVD_NAME=$(awk -F' = ' '/avd_name/ {print $2}' "$CONFIG_FILE")
APK_PATH=$(awk -F' = ' '/apk_path/ {print $2}' "$CONFIG_FILE")
AUTOMATION_SCRIPT=$(awk -F' = ' '/automation_script/ {print $2}' "$CONFIG_FILE")
AVD_ROOT=$(awk -F' = ' '/avd_root/ {print $2}' "$CONFIG_FILE")
FILE_COPY=$(awk -F' = ' '/file_copy/ {print $2}' "$CONFIG_FILE")
EMULATOR_PATH=$(awk -F' = ' '/emulator_path/ {print $2}' "$CONFIG_FILE")

# Start Emulator
python scripts/emulator.py start --avd-root "$AVD_ROOT" --avd-name "$AVD_NAME" --file-copy "$FILE_COPY" --emulator-path "$EMULATOR_PATH"   

# Install APK
python scripts/apk_installer.py --apk-path "$APK_PATH"

# Start Appium Server
python scripts/appium_server.py start

# Run Automation Script
python scripts/automation_runner.py --script-path "$AUTOMATION_SCRIPT" "$@"

# Stop Appium Server
python scripts/appium_server.py stop

# Close Emulator
python scripts/emulator.py close
