#!/usr/bin/env python3
import argparse
import subprocess
import sys
from typing import List, Dict, NoReturn


def run_automation_script(script_path : str, uiactions_path : str ) -> None :
    print(f"Running automation script '{script_path}'...")
    command = ["python3", script_path, "--config-file", uiactions_path ]
    
#python automation_script.py --username script_args[0] 
    result = subprocess.run(command)
    if result.returncode == 0:
        print("Automation script completed successfully.")
    else:
        print("Automation script failed.")
        sys.exit(result.returncode)

def main() -> NoReturn :
    parser = argparse.ArgumentParser(description="Run the automation script.")
    parser.add_argument('--script-path', required=True, help='Path to the automation script')
    parser.add_argument('--uiactions-path', required=True, help='Path to the automation script')

    args = parser.parse_args()


    run_automation_script(args.script_path, args.uiactions_path)

if __name__ == "__main__":
    main()
