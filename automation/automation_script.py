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

load_dotenv()

def parse_arguments() -> Namespace :
    parser = argparse.ArgumentParser(description='Automation script for the Android app.')
    parser.add_argument('--config-file', type=str, required=True, help='Path to the JSON configuration file')
    return parser.parse_args()

def load_config(file_path: str) -> List[dict]:
    with open(file_path, 'r') as file:
        return json.load(file)



def apply_userinput(actions: List[Dict[str, any]], 
                    user_input: Dict[int, Tuple[Dict[str, str], Dict[str, str]]]) -> List[Dict[str, any]]:
    """
    Modifies the 'actions' list of dictionaries based on the 'user_input' mappings.

    Args:
    - actions: List of action dictionaries where each dictionary represents an action.
    - user_input: A dictionary mapping indices of 'actions' to a tuple of two dictionaries.
                  The first dictionary in the tuple maps a target key to a value to be updated,
                  and the second dictionary optionally defines changes to a 'subaction' key within an action.

    Returns:
    - List[Dict[str, any]]: The modified list of actions with updates applied based on user input.
    """
    for index, updates in user_input.items():
        action = actions[index]
        # Update the main action
        if len(updates[0]) > 0:
            action_target, action_value = updates[0].get('target'), updates[0].get('value')
            if action_target and action_value:
                action[action_target] = action_value
        # Update the subaction, if any
        if len(updates[1]) > 0:
            subaction_target, subaction_value = updates[1].get('target'), updates[1].get('value')
            if subaction_target and subaction_value:
                action.setdefault('subaction', {})[subaction_target] = subaction_value

    return actions



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

    user_input = { 1 : ({ 'target' : 'text', 'value' : os.getenv('APP_NAME')},
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
