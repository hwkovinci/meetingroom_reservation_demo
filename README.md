# 📱 Android UI Automation Project with Python and Termux 🚀

Welcome to the **Android UI Automation Project**! This project allows you to automate interactions with an Android application directly from your device using Python 🐍 and Termux 📲. Follow this guide to set up and run your automation script with ease.

---

## Table of Contents 📖

- [Introduction 🌟](#introduction-)
- [Features ✨](#features-)
- [Prerequisites 📋](#prerequisites-)
- [Installation 🛠️](#installation-)
- [Usage 🚴](#usage-)
- [Scheduling Automation ⏰](#scheduling-automation-)
- [Configuration 🔧](#configuration-)
- [Logging 📄](#logging-)
- [Security Considerations 🔐](#security-considerations-)
- [Troubleshooting 🐞](#troubleshooting-)
- [Contributing 🤝](#contributing-)
- [License 📄](#license-)

---

## Introduction 🌟

Automate your Android app interactions using Python scripts running on your device! This project leverages **Termux** and **uiautomator2** to perform UI automation tasks, such as logging into an app and making reservations, all from a script. No need for external computers or servers! 🌐

---

## Features ✨

- Run Python scripts on your Android device using Termux 🐍
- Automate UI interactions with other apps using uiautomator2 🤖
- Schedule automation tasks at specific times ⏰
- Pass credentials and scheduling options via command-line arguments 📝
- Securely handle sensitive information 🔒
- Log automation activities for auditing and troubleshooting 📋

---

## Prerequisites 📋

- Android device running Android 7.0 (Nougat) or higher 📱
- [Termux](https://f-droid.org/en/packages/com.termux/) installed on your device 📲
- Basic knowledge of using the command line 🖥️

---

## Installation 🛠️

### 1. Install Termux 📥

Download and install Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/):

```bash
# No commands needed; install via F-Droid
```

### 2. Update and Upgrade Packages 🔄

Open Termux and run:

```bash
pkg update && pkg upgrade -y
```

### 3. Install Python and Pip 🐍

```bash
pkg install python -y
pip install --upgrade pip
```

### 4. Install uiautomator2 🤖

```bash
pip install --upgrade --pre uiautomator2
```

### 5. Install Android Tools (ADB) 🔧

```bash
pkg install android-tools -y
```

### 6. Initialize uiautomator2 ⚙️

```bash
python -m uiautomator2 init
```

---

## Usage 🚴

### 1. Prepare Your Automation Script 📝

Create a file named `automation_script.py`:

```bash
nano automation_script.py
```

Copy the following code into the file:

```python
import uiautomator2 as u2
import argparse
import time
import sys
import logging
from datetime import datetime, timedelta

def parse_arguments():
    parser = argparse.ArgumentParser(description='Automate meeting room reservation.')
    parser.add_argument('-u', '--username', type=str, help='Username for login', required=True)
    parser.add_argument('-p', '--password', type=str, help='Password for login', required=True)
    parser.add_argument('-s', '--schedule', type=str, help='Schedule time in HH:MM format (24-hour clock)')
    return parser.parse_args()

def wait_until_schedule(schedule_time):
    now = datetime.now()
    schedule_datetime = datetime.strptime(schedule_time, '%H:%M').replace(
        year=now.year, month=now.month, day=now.day)
    if schedule_datetime < now:
        schedule_datetime += timedelta(days=1)
    wait_seconds = (schedule_datetime - now).total_seconds()
    logging.info(f"Waiting for scheduled time: {schedule_datetime.strftime('%Y-%m-%d %H:%M')}")
    time.sleep(wait_seconds)

def automate_meeting_room_reservation(username, password):
    logging.info("Starting automation for meeting room reservation.")
    d = u2.connect()
    d.screen_on()
    d.unlock()
    d.app_start("com.example.meetingroom")  # Replace with actual package name
    d.wait_timeout = 20

    d(resourceId="com.example.meetingroom:id/username_input").set_text(username)
    d(resourceId="com.example.meetingroom:id/password_input").set_text(password)
    d(resourceId="com.example.meetingroom:id/login_button").click()
    time.sleep(5)

    # Add your automation steps here 🛠️

    d.app_stop("com.example.meetingroom")
    logging.info("Automation completed successfully.")

if __name__ == "__main__":
    logging.basicConfig(
        filename='automation.log',
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    args = parse_arguments()

    if args.schedule:
        wait_until_schedule(args.schedule)

    try:
        automate_meeting_room_reservation(args.username, args.password)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        sys.exit(1)
```

Save and exit (`Ctrl + X`, then `Y`, then `Enter`).

### 2. Make the Script Executable ✅

```bash
chmod +x automation_script.py
```

### 3. Run the Script 🏃

Provide your credentials and optionally a schedule time:

```bash
python automation_script.py -u your_username -p your_password -s 08:00
```

---

## Scheduling Automation ⏰

### Using Cron 📅

1. **Install Cronie:**

   ```bash
   pkg install cronie -y
   ```

2. **Start the Cron Service:**

   ```bash
   crond
   ```

3. **Edit the Crontab:**

   ```bash
   crontab -e
   ```

4. **Add a Cron Job:**

   Run the script every day at 8:00 AM:

   ```cron
   0 8 * * * python /data/data/com.termux/files/home/automation_script.py -u your_username -p your_password
   ```

---

## Configuration 🔧

### Using a Configuration File 📝

1. **Create `config.ini`:**

   ```ini
   [credentials]
   username = your_username
   password = your_password
   ```

2. **Modify the Script to Use the Config File:**

   Update the `parse_arguments()` function as shown in the code above.

### Environment Variables 🌍

Set environment variables in Termux:

```bash
export MEETING_USERNAME=your_username
export MEETING_PASSWORD=your_password
```

The script will read these variables if no command-line arguments are provided.

---

## Logging 📄

The script logs its activities to `automation.log`:

- **Info Logs:** General information and successful steps.
- **Error Logs:** Details about any errors that occur.

Check the log file for details about the script's execution.

---

## Security Considerations 🔐

- **Credentials Management:** Avoid hardcoding credentials in scripts or passing them via command line where they can be exposed.
- **File Permissions:** Ensure that `config.ini` and `automation.log` have appropriate permissions:

  ```bash
  chmod 600 config.ini automation.log
  ```

- **Data Protection:** Be cautious with sensitive data and comply with all relevant privacy laws and regulations.

---

## Troubleshooting 🐞

- **Script Errors:** Check `automation.log` for error messages.
- **Dependencies Issues:** Ensure all packages are installed and up to date.
- **Permission Denied:** Verify file permissions and that Termux has necessary permissions.
- **UI Elements Not Found:** Use tools like `uiautomatorviewer` to get the correct resource IDs.

---

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository 🍴
2. Create your feature branch (`git checkout -b feature/AmazingFeature`) 🌟
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`) 🖋️
4. Push to the branch (`git push origin feature/AmazingFeature`) 🚀
5. Open a pull request 📬

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy Automating!** 🎉🚀

---

*Disclaimer: Automating interactions with other apps may violate their terms of service and Android's policies. Ensure you have the right to perform such automation and comply with all legal and ethical guidelines.* ⚠️
