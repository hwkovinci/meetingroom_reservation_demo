Certainly! Let’s help you set up an automated workflow where you:
	1.	Launch an Android Virtual Device (AVD) emulator on your desktop.
	2.	Install the APK into the emulator.
	3.	Run an automation script against the emulator.
	4.	Disconnect and close the emulator.
	5.	Automate all these steps using Python’s subprocess library.

Overview

We’ll proceed with the following steps:
	1.	Set Up the Android Development Environment
	•	Install Android SDK and necessary tools.
	•	Create an Android Virtual Device (AVD).
	2.	Prepare the Automation Script
	•	Use Appium or uiautomator2 for automation.
	•	Ensure the script can interact with the emulator.
	3.	Automate the Workflow with Python
	•	Use subprocess to:
	•	Start the emulator.
	•	Install the APK.
	•	Run the automation script.
	•	Close the emulator.
	4.	Provide Example Code
	•	Show how to implement each step in Python.
	•	Organize the code for readability and reusability.

Prerequisites

	•	Operating System: Windows, macOS, or Linux desktop.
	•	Python: Version 3.x installed on your desktop.
	•	Android SDK: Installed with command-line tools.
	•	Java Development Kit (JDK): Required for Android SDK tools.
	•	Appium: For automation scripts (optional if using uiautomator2).

Step-by-Step Guide

1. Set Up the Android Development Environment

a. Install Java Development Kit (JDK)

	•	Download JDK: Oracle JDK Downloads or OpenJDK.
	•	Install JDK: Follow the installation instructions for your OS.
	•	Set JAVA_HOME Environment Variable: Point it to your JDK installation directory.

b. Install Android SDK Command-Line Tools

	•	Download Command-Line Tools:
	•	Visit Android Studio Downloads.
	•	Scroll down to Command line tools only and download the package for your OS.
	•	Install SDK Tools:

# Create a directory for Android SDK
mkdir -p ~/Android/Sdk/cmdline-tools/latest

# Extract the downloaded zip file
unzip commandlinetools-*.zip -d ~/Android/Sdk/cmdline-tools/latest


	•	Set Environment Variables:

export ANDROID_SDK_ROOT=~/Android/Sdk
export PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/latest/bin
export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools


	•	Accept Licenses and Install Packages:

sdkmanager --sdk_root=$ANDROID_SDK_ROOT --licenses
sdkmanager --sdk_root=$ANDROID_SDK_ROOT "platform-tools" "platforms;android-30" "system-images;android-30;google_apis;x86_64" "emulator"



c. Create an Android Virtual Device (AVD)

	•	List Available System Images:

sdkmanager --list | grep "system-images"


	•	Create an AVD:

avdmanager create avd -n my_avd -k "system-images;android-30;google_apis;x86_64" --device "pixel"

	•	-n my_avd: Names the AVD as “my_avd”.
	•	-k: Specifies the system image to use.
	•	--device "pixel": Uses a predefined device configuration.

2. Prepare the Automation Script

We’ll use Appium for automation, but you can also use uiautomator2 if you prefer.

a. Install Appium

	•	Install Node.js (if not already installed):

# On macOS
brew install node

# On Ubuntu/Debian
sudo apt-get install -y nodejs npm

# On Windows
# Download and install from https://nodejs.org/


	•	Install Appium Server:

npm install -g appium


	•	Install Appium Python Client:

pip install Appium-Python-Client



b. Write the Automation Script

Example Script: automation_script.py

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

def run_automation():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",  # Adjust based on your emulator's API level
        "deviceName": "my_avd",
        "app": "/path/to/your/application.apk",  # Replace with your APK path
        "automationName": "UiAutomator2",
        "noReset": True
    }

    # Connect to Appium server
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    # Add your automation steps here
    time.sleep(5)  # Wait for the app to load

    # Example: Find and click a button
    # Replace with actual resource IDs or other locators
    driver.find_element(AppiumBy.ID, "com.example.app:id/button_login").click()

    # Quit the driver
    driver.quit()

if __name__ == "__main__":
    run_automation()

Notes:
	•	Replace "/path/to/your/application.apk" with the actual path to your APK.
	•	Adjust platformVersion to match your emulator’s Android version.
	•	Replace locators in the automation steps with actual IDs from your app.

3. Automate the Workflow with Python’s subprocess

We’ll create a Python script that:
	1.	Starts the emulator.
	2.	Waits for the emulator to boot up.
	3.	Installs the APK.
	4.	Starts the Appium server.
	5.	Runs the automation script.
	6.	Stops the Appium server.
	7.	Closes the emulator.

a. Import Required Modules

import subprocess
import os
import time
import threading

b. Define Functions for Each Step

i. Start the Emulator

def start_emulator(avd_name):
    print("Starting the emulator...")
    emulator_path = os.path.expanduser("~/Android/Sdk/emulator/emulator")
    subprocess.Popen([emulator_path, "-avd", avd_name, "-no-snapshot-load"])
    # Wait for the emulator to boot up
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
            time.sleep(5)
    print("Emulator started.")

ii. Install the APK

def install_apk(apk_path):
    print("Installing the APK...")
    subprocess.run(["adb", "install", "-r", apk_path])
    print("APK installed.")

iii. Start Appium Server

def start_appium_server():
    print("Starting Appium server...")
    subprocess.Popen(["appium"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for Appium server to start
    time.sleep(5)
    print("Appium server started.")

iv. Run the Automation Script

Assuming your automation script is named automation_script.py.

def run_automation_script():
    print("Running automation script...")
    subprocess.run(["python", "automation_script.py"])
    print("Automation script completed.")

v. Stop Appium Server

def stop_appium_server():
    print("Stopping Appium server...")
    subprocess.run(["pkill", "-f", "appium"])
    print("Appium server stopped.")

vi. Close the Emulator

def close_emulator():
    print("Closing the emulator...")
    subprocess.run(["adb", "emu", "kill"])
    print("Emulator closed.")

c. Main Workflow Function

def main():
    avd_name = "my_avd"
    apk_path = "/path/to/your/application.apk"  # Replace with your APK path

    start_emulator(avd_name)
    install_apk(apk_path)
    start_appium_server()
    run_automation_script()
    stop_appium_server()
    close_emulator()

if __name__ == "__main__":
    main()

4. Full Python Script

Filename: automation_workflow.py

import subprocess
import os
import time

def start_emulator(avd_name):
    print("Starting the emulator...")
    emulator_path = os.path.expanduser("~/Android/Sdk/emulator/emulator")
    subprocess.Popen([emulator_path, "-avd", avd_name, "-no-snapshot-load"])
    # Wait for the emulator to boot up
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

def install_apk(apk_path):
    print("Installing the APK...")
    subprocess.run(["adb", "install", "-r", apk_path])
    print("APK installed.")

def start_appium_server():
    print("Starting Appium server...")
    subprocess.Popen(["appium"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for Appium server to start
    time.sleep(5)
    print("Appium server started.")

def run_automation_script():
    print("Running automation script...")
    subprocess.run(["python", "automation_script.py"])
    print("Automation script completed.")

def stop_appium_server():
    print("Stopping Appium server...")
    subprocess.run(["pkill", "-f", "appium"])
    print("Appium server stopped.")

def close_emulator():
    print("Closing the emulator...")
    subprocess.run(["adb", "emu", "kill"])
    print("Emulator closed.")

def main():
    avd_name = "my_avd"
    apk_path = "/path/to/your/application.apk"  # Replace with your APK path

    start_emulator(avd_name)
    install_apk(apk_path)
    start_appium_server()
    run_automation_script()
    stop_appium_server()
    close_emulator()

if __name__ == "__main__":
    main()

5. Running the Workflow

	•	Ensure all paths are correct in automation_workflow.py and automation_script.py.
	•	Set executable permissions (if on Unix-like OS):

chmod +x automation_workflow.py automation_script.py


	•	Run the workflow script:

python automation_workflow.py

Additional Considerations

1. Emulator Performance

	•	Hardware Acceleration: Ensure that your system supports hardware acceleration (Intel HAXM on Windows/macOS, KVM on Linux) for better emulator performance.
	•	Emulator Options: Adjust emulator launch options for better performance (e.g., -gpu host).

2. Handling Appium Server

	•	Appium Server Logs: You may want to capture and monitor Appium server logs for debugging.
	•	Appium Server Port: If using a different port, adjust the webdriver.Remote URL accordingly.

3. Waiting Mechanisms

	•	Wait for Emulator Boot: The script waits until sys.boot_completed property is set to 1.
	•	Wait for Appium Server: Adjust the sleep duration if needed.

4. Error Handling

	•	Add Try-Except Blocks: Enhance the script with exception handling to manage errors gracefully.
	•	Clean Up Resources: Ensure that the emulator and Appium server are closed even if errors occur.

5. Cross-Platform Compatibility

	•	Windows Considerations:
	•	Adjust paths and commands accordingly.
	•	Use emulator.exe and adb.exe from the Android SDK.
	•	Use of pkill:
	•	On Windows, use taskkill to stop processes.

def stop_appium_server():
    print("Stopping Appium server...")
    subprocess.run(["taskkill", "/F", "/IM", "node.exe"])
    print("Appium server stopped.")

Enhancements

1. Use Threading for Parallel Processes

	•	Start Appium Server in a Separate Thread: To capture logs and handle the process more robustly.

2. Use Python Libraries for ADB and Emulator Control

	•	pure-python-adb: A library to interact with ADB using Python.

3. Logging

	•	Implement Logging: Use the logging module to log events and errors.

Complete Workflow with Error Handling and Logging

Here’s an enhanced version of automation_workflow.py with logging and error handling:

import subprocess
import os
import time
import logging
import sys
import threading

# Configure logging
logging.basicConfig(
    filename='automation_workflow.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start_emulator(avd_name):
    try:
        logging.info("Starting the emulator...")
        emulator_path = os.path.expanduser("~/Android/Sdk/emulator/emulator")
        subprocess.Popen([emulator_path, "-avd", avd_name, "-no-snapshot-load"])
        # Wait for the emulator to boot up
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
                logging.info("Waiting for emulator to boot...")
                time.sleep(5)
        logging.info("Emulator started.")
    except Exception as e:
        logging.error(f"Failed to start emulator: {e}")
        sys.exit(1)

def install_apk(apk_path):
    try:
        logging.info("Installing the APK...")
        subprocess.run(["adb", "install", "-r", apk_path], check=True)
        logging.info("APK installed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install APK: {e}")
        sys.exit(1)

def start_appium_server():
    try:
        logging.info("Starting Appium server...")
        subprocess.Popen(["appium"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Wait for Appium server to start
        time.sleep(5)
        logging.info("Appium server started.")
    except Exception as e:
        logging.error(f"Failed to start Appium server: {e}")
        sys.exit(1)

def run_automation_script():
    try:
        logging.info("Running automation script...")
        subprocess.run(["python", "automation_script.py"], check=True)
        logging.info("Automation script completed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Automation script failed: {e}")
        sys.exit(1)

def stop_appium_server():
    try:
        logging.info("Stopping Appium server...")
        subprocess.run(["pkill", "-f", "appium"])
        logging.info("Appium server stopped.")
    except Exception as e:
        logging.error(f"Failed to stop Appium server: {e}")

def close_emulator():
    try:
        logging.info("Closing the emulator...")
        subprocess.run(["adb", "emu", "kill"])
        logging.info("Emulator closed.")
    except Exception as e:
        logging.error(f"Failed to close emulator: {e}")

def main():
    avd_name = "my_avd"
    apk_path = "/path/to/your/application.apk"  # Replace with your APK path

    start_emulator(avd_name)
    install_apk(apk_path)
    start_appium_server()
    run_automation_script()
    stop_appium_server()
    close_emulator()

if __name__ == "__main__":
    main()

Conclusion

By following these steps, you can automate the process of starting an Android emulator, installing an APK, running an automation script, and closing the emulator, all from a Python script using subprocess. This approach allows you to run your automation tests without the need for a physical device and automate the entire workflow.

Additional Resources

	•	Android SDK Command-Line Tools: Official Documentation
	•	Appium Documentation: Appium Docs
	•	Appium-Python-Client: GitHub Repository
	•	ADB Commands: ADB Shell Commands
	•	Python subprocess Module: Official Documentation

Feel Free to Ask

If you have any questions or need further assistance with:
	•	Adjusting the scripts for your specific environment.
	•	Handling specific errors or issues.
	•	Enhancing the automation scripts with more complex interactions.
	•	Integrating this workflow into a CI/CD pipeline.

I’m here to help you achieve your automation goals!

Disclaimer: Ensure you have the rights and permissions to automate the application you’re testing. Always comply with software licenses, terms of service, and applicable laws.
