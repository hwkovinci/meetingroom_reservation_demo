#!/usr/bin/env python3
import argparse
import time
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from argparse import Namespace
from uiaction import UIAction
from parseutil import load_config, apply_userinput, execution_log 
from userinput import load_variables, load_connection, get_work_batch_list
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='app.log',  # Log to a file
                    filemode='a')  # Append mode

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
        execution_log( description, enum, len( work_batch_list ) )

        description, batch = item
        print(description)
        for action_index, i in enumerate(batch):
            logging.info(f"  - Action {action_index + 1} of {len(batch)}: {actions[i].setdefault('description', 'no comment')} executed")
            ui_actions.action_wrapper(actions[i])
        decision_index = batch[-1] + 1
        stop, next_batch_index = ui_actions.make_decision(decision_index, actions)
        if not stop :
            if next_batch_index is not None:
                # Jump to specific batch index
                state_changed = True
                move_to = next_batch_index
                logging.info(f"↳ Jumping to Batch {next_batch_index}")
                continue
            else:
                # Skip the next batch
                state_changed = False
                logging.info("↳ Moving to next batch")
                continue
        else :
            logging.info("Batch execution stopped")
            break

    driver.quit()

if __name__ == "__main__":
    args = parse_arguments()
    run_automation(args)
