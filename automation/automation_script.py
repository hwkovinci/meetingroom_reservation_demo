#!/usr/bin/env python3
import argparse
import time
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from argparse import Namespace
from uiaction import UIAction
from parseutil import load_config, apply_userinput 
from userinput import load_variables, load_connection, get_work_batch_list


def parse_arguments() -> Namespace :
    parser = argparse.ArgumentParser(description='Automation script for the Android app.')
    parser.add_argument('--config-file', type=str, required=True, help='Path to the JSON configuration file')
    return parser.parse_args()


def run_automation(args : Namespace) -> None:
    work_batch_list = get_work_batch_list()
    actions = load_config(args.config_file)
    actions = apply_userinput( actions, load_variables() )
    url, desired_caps = load_connection()
    options = AppiumOptions()
    options.load_capabilities( desired_caps )
    driver = webdriver.Remote( url , options=options)
    
    time.sleep(5) 
    ui_actions = UIAction(driver)
    
    # Iterate through each action in the JSON configuration
    
    state_changed = False
    move_to = 0
    for enum, item in enumerate( work_batch_list ) :
        if state_changed :
            if move_to != enum :
                continue
        
        description, batch = item
        print(description)
        for i in batch:
            ui_actions.action_wrapper(actions[i])
        decision_index = batch[-1] + 1
        stop, next_batch_index = ui_actions.make_decision(decision_index, actions)
        if not stop :
            if next_batch_index is not None:
                # Jump to specific batch index
                state_changed = True
                move_to = next_batch_index
                continue
            else:
                # Skip the next batch
                state_changed = False
                continue
        else : break

    driver.quit()

if __name__ == "__main__":
    args = parse_arguments()
    run_automation(args)
