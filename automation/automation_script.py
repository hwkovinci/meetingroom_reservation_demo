#!/usr/bin/env python3

import argparse
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from argparse import Namespace
from Typing import Tuple, List
from dotenv import load_dotenv
from uiactions import UIAction

load_dotenv()

def parse_arguments() -> Namespace :
    parser = argparse.ArgumentParser(description='Automation script for the Android app.')
    parser.add_argument('--config-file', type=str, required=True, help='Path to the JSON configuration file')
    return parser.parse_args()

def load_config(file_path: str) -> List[Dict]:
    with open(file_path, 'r') as file:
        return json.load(file)

def apply_userinput( actions : List[Dict],
                    user_input : Dict[int , Tuple[Dict[str, str],Dict[str, str] ] ) -> List[Dict] :
    for index in user_input.keys() :
        for sub_index in range(0, 2) :
            if len  user_input[index][sub_index].keys() :
                actions[index][ user_input[index][sub_index]["target"]] = user_input[index][sub_index]['value']





def run_automation(args : Namespace) -> None:


    desired_caps = {
        "platformName": "Android",
        "platformVersion": args.platform_version,
        "deviceName": "Android",
        "appPackage": args.app_package,
        "appActivity": args.app_activity,
        "app" : args.app_path,
        "automationName": "UiAutomator2",
        "noReset": True
    }

    user_input = {
            1 : ({
                'target' : 'text',
                'value' : os.getnv('user_id')
                },
                 {})
            3 : ({},{})




            }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
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
