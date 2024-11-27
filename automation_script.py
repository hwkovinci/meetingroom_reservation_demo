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
