#!/usr/bin/env python3
import argparse
import time
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from argparse import Namespace
from uiaction import UIAction
from parseutil import load_config, apply_userinput 
from userinput import load_variables, load_connection


def parse_arguments() -> Namespace :
    parser = argparse.ArgumentParser(description='Automation script for the Android app.')
    parser.add_argument('--config-file', type=str, required=True, help='Path to the JSON configuration file')
    return parser.parse_args()


def run_automation(args : Namespace) -> None:
    actions = load_config(args.config_file)
    actions = apply_userinput( actions, load_variables() )
    url, desired_caps = load_connection()
    options = AppiumOptions()
    options.load_capabilities( desired_caps )
    driver = webdriver.Remote( url , options=options)
    
    time.sleep(5) 
    ui_actions = UIAction(driver)
 
    # Iterate through each action in the JSON configuration
    for action in actions:
        ui_actions.action_wrapper(action)


    driver.quit()

if __name__ == "__main__":
    args = parse_arguments()
    run_automation(args)
