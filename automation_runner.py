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
