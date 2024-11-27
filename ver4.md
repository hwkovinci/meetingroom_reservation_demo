Certainly! Let’s design your automation project to:
	•	Use Python scripts that utilize subprocess and argparse.
	•	Place Python scripts in distinct modules (libraries) for modularity.
	•	Create a concise and flexible shell script to orchestrate the workflow.

Project Structure

Here’s the proposed project structure:

automation_project/
├── scripts/
│   ├── __init__.py
│   ├── emulator.py
│   ├── apk_installer.py
│   ├── appium_server.py
│   └── automation_runner.py
├── automation/
│   └── automation_script.py
├── workflow.sh
├── requirements.txt
└── README.md

Explanation

	•	scripts/: Contains Python modules for each task, utilizing subprocess and argparse.
	•	automation/: Contains the main automation script (automation_script.py) that performs the UI automation.
	•	workflow.sh: A concise shell script that orchestrates the workflow by calling the Python scripts.
	•	requirements.txt: Lists all Python dependencies.
	•	README.md: Project documentation.

Step-by-Step Guide

1. Create Python Modules in scripts/ Directory

Each Python module will:
	•	Use subprocess to perform its task.
	•	Use argparse to handle command-line arguments.
	•	Be designed for modularity and reusability.

a. scripts/emulator.py

Purpose: Start and stop the Android emulator.

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

b. scripts/apk_installer.py

Purpose: Install an APK onto the emulator.

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

c. scripts/appium_server.py

Purpose: Start and stop the Appium server.

#!/usr/bin/env python3

import argparse
import subprocess
import sys
import time
import os

def start_appium():
    print("Starting Appium server...")
    appium_process = subprocess.Popen(["appium"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for Appium server to start
    time.sleep(5)
    with open("appium.pid", "w") as f:
        f.write(str(appium_process.pid))
    print(f"Appium server started with PID {appium_process.pid}.")

def stop_appium():
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

def main():
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

d. scripts/automation_runner.py

Purpose: Run the automation script.

#!/usr/bin/env python3

import argparse
import subprocess
import sys

def run_automation_script(script_path, script_args):
    print(f"Running automation script '{script_path}'...")
    command = ["python", script_path] + script_args
    result = subprocess.run(command)
    if result.returncode == 0:
        print("Automation script completed successfully.")
    else:
        print("Automation script failed.")
        sys.exit(result.returncode)

def main():
    parser = argparse.ArgumentParser(description="Run the automation script.")
    parser.add_argument('--script-path', required=True, help='Path to the automation script')
    parser.add_argument('script_args', nargs=argparse.REMAINDER, help='Arguments for the automation script')

    args = parser.parse_args()
    run_automation_script(args.script_path, args.script_args)

if __name__ == "__main__":
    main()

2. Create the Automation Script in automation/automation_script.py

Purpose: Perform UI automation using Appium, utilizing argparse.

#!/usr/bin/env python3

import argparse
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def parse_arguments():
    parser = argparse.ArgumentParser(description='Automation script for the Android app.')
    parser.add_argument('--username', type=str, required=True, help='Username for login')
    parser.add_argument('--password', type=str, required=True, help='Password for login')
    parser.add_argument('--device-name', type=str, default='emulator-5554', help='Device name')
    parser.add_argument('--platform-version', type=str, default='11', help='Android platform version')
    parser.add_argument('--app-package', type=str, required=True, help='App package name')
    parser.add_argument('--app-activity', type=str, required=True, help='App activity name')
    return parser.parse_args()

def run_automation(args):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": args.platform_version,
        "deviceName": args.device_name,
        "appPackage": args.app_package,
        "appActivity": args.app_activity,
        "automationName": "UiAutomator2",
        "noReset": True
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    time.sleep(5)  # Wait for the app to load

    # Perform automation steps
    driver.find_element(AppiumBy.ID, "com.example.app:id/username_input").send_keys(args.username)
    driver.find_element(AppiumBy.ID, "com.example.app:id/password_input").send_keys(args.password)
    driver.find_element(AppiumBy.ID, "com.example.app:id/login_button").click()

    # Add more automation steps as needed

    driver.quit()

if __name__ == "__main__":
    args = parse_arguments()
    run_automation(args)

3. Create a Concise and Flexible Shell Script workflow.sh

Purpose: Orchestrate the workflow by calling the Python scripts, passing arguments as needed.

#!/bin/bash

# Configuration
AVD_NAME="my_avd"
APK_PATH="/path/to/your/application.apk"
AUTOMATION_SCRIPT="automation/automation_script.py"

# Start Emulator
python scripts/emulator.py start --avd-name "$AVD_NAME"

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

Usage:

./workflow.sh --username your_username --password your_password --app-package com.example.app --app-activity .MainActivity

	•	The "$@" in automation_runner.py ensures that all additional arguments are passed to the automation script.

4. Update requirements.txt

List all Python dependencies:

appium-python-client==2.7.1

Install dependencies with:

pip install -r requirements.txt

5. Make All Scripts Executable

Ensure that all scripts have executable permissions:

chmod +x scripts/*.py
chmod +x automation/automation_script.py
chmod +x workflow.sh

6. Running the Workflow

Execute the main workflow script, passing necessary arguments to the automation script:

./workflow.sh --username your_username --password your_password --app-package com.example.app --app-activity .MainActivity

Explanation of the Design

	•	Modular Python Scripts:
	•	Each script in scripts/ is responsible for a single task.
	•	Scripts use subprocess to execute commands and argparse to handle command-line arguments.
	•	Scripts can be used independently or combined in different workflows.
	•	Automation Script in Separate Module:
	•	The main automation script is placed in automation/ for clarity.
	•	It uses argparse to accept parameters and can be easily modified or extended.
	•	Concise and Flexible Shell Script:
	•	workflow.sh orchestrates the workflow by calling the Python scripts.
	•	It is concise, with each step clearly defined.
	•	Flexibility is achieved by passing arguments to the automation script.

Advantages of This Approach

	•	Modularity:
	•	Easy to maintain and update individual components.
	•	Encourages code reuse.
	•	Flexibility:
	•	The shell script can be easily modified to include or exclude steps.
	•	Arguments can be passed to scripts to alter behavior.
	•	Clarity:
	•	The project structure is organized and easy to understand.
	•	Each component has a clear purpose.
	•	Extensibility:
	•	New scripts can be added to the scripts/ directory for additional tasks.
	•	The automation script can be extended with more functionality.

Additional Enhancements

Error Handling and Logging

Add error handling and logging to the Python scripts.

Example in scripts/emulator.py:

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def start_emulator(avd_name):
    try:
        # Existing code...
        logging.info("Emulator started.")
    except Exception as e:
        logging.error(f"Failed to start emulator: {e}")
        sys.exit(1)

Repeat similar patterns in other scripts.

Use Configuration Files

Parameters like AVD_NAME and APK_PATH can be moved to a configuration file.

Create config.ini

[DEFAULT]
avd_name = my_avd
apk_path = /path/to/your/application.apk

Modify workflow.sh

#!/bin/bash

# Load configuration
CONFIG_FILE="config.ini"
AVD_NAME=$(awk -F' = ' '/avd_name/ {print $2}' "$CONFIG_FILE")
APK_PATH=$(awk -F' = ' '/apk_path/ {print $2}' "$CONFIG_FILE")

# Rest of the script...

Final Thoughts

This approach provides:
	•	Modular Design: Each component is isolated, promoting better code organization.
	•	Flexibility: Easy to adjust parameters and workflow steps.
	•	Maintainability: Simplifies updates and debugging.

Need Further Assistance?

If you need help with:
	•	Customizing the automation script for your specific app.
	•	Implementing advanced error handling and logging.
	•	Integrating this workflow into a CI/CD pipeline.
	•	Optimizing the scripts for performance or additional features.

Feel free to ask, and I’ll be happy to assist you further!

Disclaimer: Ensure you have the rights and permissions to automate the application you’re testing. Always comply with software licenses, terms of service, and applicable laws.
