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
ENV_DIR=$(awk -F' = ' '/env_dir/ {print $2}' "$CONFIG_FILE")

# Ensure virtual environment directory exists
if [ ! -d "$ENV_DIR" ]; then
    python3 -m venv "$ENV_DIR"
fi

# Activate the virtual environment
source "$ENV_DIR/bin/activate"

# Install required Python packages from requirements.txt
pip install --upgrade pip
pip install -r requirements.txt

# Start Emulator
python3 scripts/emulator.py start --avd-root "$AVD_ROOT" --avd-name "$AVD_NAME" --file-copy "$FILE_COPY" --emulator-path "$EMULATOR_PATH"   

# Install APK
python3 scripts/apk_installer.py --apk-path "$APK_PATH"

# Start Appium Server
python3 scripts/appium_server.py start

messages=(
    "Did you know? Honey never spoils. We're just here waiting, not spoiling either.",
    "Why don't scientists trust atoms anymore? They make up everything, unlike this script, which is 100% real.",
    "‘I'm not superstitious, but I am a little stitious.’ – Michael Scott (Waiting, just like us.)",
    "Hang tight! Running the world's slowest countdown...",
    "Currently recalibrating the internet... Please stand by.",
    "Downloading more RAM to speed up this process...",
    "Please wait, polishing the pixels on your screen...",
    "Great things come to those who wait... like the end of this sleep command!",
    "If a program outputs in a console and no one is around to see it, does it make a sound?",
    "Debugging: Being the detective in a crime movie where you are also the murderer."
)

# Total wait time in seconds
total_wait_time=300

# Interval between messages in seconds
interval=5

# Calculate how many messages to show
number_of_messages=$((total_wait_time / interval))

for ((i=0; i<number_of_messages; i++)); do
    # Select a random message
    random_index=$(($RANDOM % ${#messages[@]}))
    echo "${messages[random_index]}"
    # Wait for interval
    sleep $interval
done

echo "Continuing with the script execution..."

# Run Automation Script
python3 scripts/automation_runner.py --script-path "$AUTOMATION_SCRIPT" --uiactions-path "$UIACTIONS_JSON" 

# Stop Appium Server
python3 scripts/appium_server.py stop

# Close Emulator
python3 scripts/emulator.py close

# Deactivate the virtual environment
deactivate
