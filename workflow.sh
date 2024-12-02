#!/bin/bash

# Load configuration
CONFIG_FILE="config.ini"
AVD_NAME=$(awk -F' = ' '/avd_name/ {print $2}' "$CONFIG_FILE")
APK_PATH=$(awk -F' = ' '/apk_path/ {print $2}' "$CONFIG_FILE")
AUTOMATION_SCRIPT=$(awk -F' = ' '/automation_script/ {print $2}' "$CONFIG_FILE")
AVD_ROOT=$(awk -F' = ' '/avd_root/ {print $2}' "$CONFIG_FILE")
FILE_COPY=$(awk -F' = ' '/file_copy/ {print $2}' "$CONFIG_FILE")
EMULATOR_PATH=$(awk -F' = ' '/emulator_path/ {print $2}' "$CONFIG_FILE")
UIACTIONS_JSON=$(awk -F' = ' '/uiactions_json/ {print $2}' "$CONFIG_FILE")

# Start Emulator
python3 scripts/emulator.py start --avd-root "$AVD_ROOT" --avd-name "$AVD_NAME" --file-copy "$FILE_COPY" --emulator-path "$EMULATOR_PATH"   

# Install APK
python3 scripts/apk_installer.py --apk-path "$APK_PATH"

# Start Appium Server
python3 scripts/appium_server.py start

# Run Automation Script
python3 scripts/automation_runner.py --script-path "$AUTOMATION_SCRIPT" --config-file "$UIACTIONS_JSON"

# Stop Appium Server
python3 scripts/appium_server.py stop

# Close Emulator
python3 scripts/emulator.py close



# Load configuration
CONFIG_FILE="config.ini"
AVD_NAME=$(awk -F' = ' '/avd_name/ {print $2}' "$CONFIG_FILE")
APK_PATH=$(awk -F' = ' '/apk_path/ {print $2}' "$CONFIG_FILE")
AUTOMATION_SCRIPT=$(awk -F' = ' '/automation_script/ {print $2}' "$CONFIG_FILE")
AVD_ROOT=$(awk -F' = ' '/avd_root/ {print $2}' "$CONFIG_FILE")
FILE_COPY=$(awk -F' = ' '/file_copy/ {print $2}' "$CONFIG_FILE")
EMULATOR_PATH=$(awk -F' = ' '/emulator_path/ {print $2}' "$CONFIG_FILE")
UIACTIONS_JSON=$(awk -F' = ' '/uiactions_json/ {print $2}' "$CONFIG_FILE")

# Ensure virtual environment directory exists
VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Install required Python packages from requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

# Start Emulator
python3 scripts/emulator.py start --avd-root "$AVD_ROOT" --avd-name "$AVD_NAME" --file-copy "$FILE_COPY" --emulator-path "$EMULATOR_PATH"

# Install APK
python3 scripts/apk_installer.py --apk-path "$APK_PATH"

# Start Appium Server
python3 scripts/appium_server.py start

# Run Automation Script
python3 scripts/automation_runner.py --script-path "$AUTOMATION_SCRIPT" --config-file "$UIACTIONS_JSON"

# Stop Appium Server
python3 scripts/appium_server.py stop

# Close Emulator
python3 scripts/emulator.py close

# Deactivate the virtual environment
deactivate

