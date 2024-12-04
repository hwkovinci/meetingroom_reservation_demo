#!/usr/bin/env python3
import argparse
import time
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from argparse import Namespace
from typing import Dict, List, Tuple
from dotenv import load_dotenv
import os
from uiaction import UIAction
import parseutil as pu 

load_dotenv()

def parse_arguments() -> Namespace :
    parser = argparse.ArgumentParser(description='Automation script for the Android app.')
    parser.add_argument('--config-file', type=str, required=True, help='Path to the JSON configuration file')
    return parser.parse_args()


def run_automation(args : Namespace) -> None:
    desired_caps = {
            "appium:DeviceName": "Android",
            "platformName": "Android",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True,
            "automationName": "UiAutomator2",
            "noRest" : True }  


#    desired_caps = dict( platformName='Android',
#                    automationName='uiautomator2',
#                    deviceName='Android',
#                    appPackage='com.android.settings',
#                    appActivity='.Settings',
#                    language='en',
#                    locale='US')

    user_input = { 1 : ({ 'target' : 'text', 'value' : [os.getenv('APP_NAME') ]},
                        {})}
    options = AppiumOptions()
    options.load_capabilities( desired_caps )
    url = f'http://{os.getenv("ADRESS")}:{os.getenv("PORT")}/wd/hub'
    driver = webdriver.Remote( url , options=options)
    time.sleep(5)  # Wait for the app to load


    ui_actions = UIAction(driver)
    actions = load_config(args.config_file)


    actions = apply_userinput( actions, user_input )


    # Iterate through each action in the JSON configuration
    for action in actions:
        ui_actions.action_wrapper(action)


    driver.quit()

if __name__ == "__main__":
    args = parse_arguments()
    run_automation(args)
