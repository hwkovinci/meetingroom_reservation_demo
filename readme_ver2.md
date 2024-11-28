📱 Android UI Automation Project with Python and Appium 🚀

Welcome to the Android UI Automation Project! This project allows you to automate interactions with an Android application using Python 🐍 and Appium 🤖. You’ll run your automation scripts on a desktop environment using an Android Virtual Device (AVD) emulator.

Table of Contents 📖

	•	Introduction 🌟
	•	Features ✨
	•	Prerequisites 📋
	•	System Setup Guidelines 🛠️
	•	1. Install Java Development Kit (JDK) ☕
	•	2. Install Android SDK 📲
	•	3. Create an Android Virtual Device (AVD) 📱
	•	4. Install Appium and Dependencies 🤖
	•	Project Structure 📂
	•	Usage 🚴
	•	Additional Information ℹ️
	•	Contributing 🤝
	•	License 📄

Introduction 🌟

This project automates Android application interactions by:
	•	Running automation scripts on a desktop using an Android emulator.
	•	Installing the target APK into the emulator.
	•	Executing automation scripts using Appium.
	•	Automating the entire workflow with shell scripts and Python scripts.

Features ✨

	•	Cross-Platform Support: Works on Windows, macOS, and Linux 🖥️
	•	Modular Design: Clean separation between components for maintainability 🛠️
	•	Automation with Appium: Utilize Appium for robust UI automation 🤖
	•	Scripted Workflow: Shell and Python scripts orchestrate the entire process 📜

Prerequisites 📋

	•	Python 3.x installed on your desktop 🐍
	•	Node.js installed (for Appium server) 📦
	•	Git installed (optional, for cloning the repository) 🌐

System Setup Guidelines 🛠️

1. Install Java Development Kit (JDK) ☕

For Windows:
	1.	Download JDK:
	•	Visit Oracle JDK Downloads or OpenJDK.
	2.	Install JDK:
	•	Run the installer and follow the instructions.
	•	By default, JDK is installed in C:\Program Files\Java\jdk-<version>.
	3.	Set JAVA_HOME Environment Variable:
	•	Go to Control Panel > System > Advanced system settings.
	•	Click Environment Variables.
	•	Under System Variables, click New.
	•	Variable name: JAVA_HOME
	•	Variable value: C:\Program Files\Java\jdk-<version>
	•	Click OK.
	4.	Update PATH Variable:
	•	In System Variables, select Path and click Edit.
	•	Add %JAVA_HOME%\bin to the list.
	•	Click OK.

For macOS:
	1.	Download and Install JDK:
	•	Visit Oracle JDK Downloads.
	•	Download the macOS installer and run it.
	2.	Set JAVA_HOME Environment Variable:
	•	Open Terminal.
	•	Run:
```shell
echo 'export JAVA_HOME=$(/usr/libexec/java_home)' >> ~/.bash_profile
source ~/.bash_profile
```


For Linux:
	1.	Install OpenJDK:
	•	Ubuntu/Debian:
```shell
sudo apt update
sudo apt install -y openjdk-11-jdk
```

	•	CentOS/Fedora:
```shell
sudo yum install -y java-11-openjdk-devel
```

	2.	Set JAVA_HOME Environment Variable:
	•	Add to ~/.bashrc or ~/.bash_profile:
```shell
export JAVA_HOME=$(dirname $(dirname $(readlink -f $(which javac))))
export PATH=$PATH:$JAVA_HOME/bin
```

	•	Reload the profile:
```
source ~/.bashrc
```


2. Install Android SDK 📲

Note: We’ll install the Command Line Tools instead of the full Android Studio.

For All Platforms:
	1.	Download Command Line Tools:
	•	Visit Android Studio Downloads.
	•	Scroll down to Command line tools only.
	•	Download the appropriate package for your OS.
	2.	Install SDK Command Line Tools:
	•	Extract the Zip File:
	•	Windows: Use an unzip tool to extract to C:\Android\cmdline-tools.
	•	macOS/Linux:
```shell
mkdir -p ~/Android/Sdk/cmdline-tools
unzip commandlinetools-*.zip -d ~/Android/Sdk/cmdline-tools
```

	3.	Set ANDROID_SDK_ROOT Environment Variable:
	•	Windows:
 		Variable name: ANDROID_SDK_ROOT
   		Variable value: C:\Android
	•	macOS/Linux:
```shell
echo 'export ANDROID_SDK_ROOT=~/Android/Sdk' >> ~/.bash_profile
echo 'export PATH=$PATH:$ANDROID_SDK_ROOT/cmdline-tools/bin' >> ~/.bash_profile
echo 'export PATH=$PATH:$ANDROID_SDK_ROOT/platform-tools' >> ~/.bash_profile
source ~/.bash_profile
```

	4.	Install Required SDK Packages:
	•	Accept Licenses:
```shell
sdkmanager --sdk_root=$ANDROID_SDK_ROOT --licenses
```

	•	Install Packages:
```shell
sdkmanager --sdk_root=$ANDROID_SDK_ROOT "platform-tools" "platforms;android-30" "system-images;android-30;google_apis;x86_64" "emulator"
```


3. Create an Android Virtual Device (AVD) 📱

For All Platforms:
	1.	List Available System Images:
```shell
sdkmanager --list | grep "system-images"
```

	2.	Create an AVD:
```shell
avdmanager create avd -n my_avd -k "system-images;android-30;google_apis;x86_64" --device "pixel"
```
	•	-n my_avd: Names the AVD as “my_avd”.
	•	-k: Specifies the system image to use.
	•	--device "pixel": Uses a predefined device configuration.

4. Install Appium and Dependencies 🤖

For All Platforms:
	1.	Install Node.js:
	•	Windows:
	•	Download the Windows Installer from Node.js Downloads.
	•	Run the installer.
	•	macOS:
```shell
brew install node
```

	•	Linux:
```shell
sudo apt update
sudo apt install -y nodejs npm
```

	2.	Install Appium Server:
```shell
npm install -g appium
```

	3.	Install Appium Python Client:
```shell
pip install Appium-Python-Client
```
Project Structure 📂

automation_project/
├── scripts/
│   ├── __init__.py
│   ├── emulator.py
│   ├── apk_installer.py
│   ├── appium_server.py
│   └── automation_runner.py
├── automation/
│   └── automation_script.py
├── workflow.sh
├── requirements.txt
└── README.md

	•	scripts/: Contains Python modules for each task.
	•	automation/: Contains the main automation script.
	•	workflow.sh: Shell script to orchestrate the workflow.
	•	requirements.txt: Python dependencies.
	•	README.md: Project documentation (this file).

Usage 🚴

1. Clone the Repository
```shell
git clone https://github.com/yourusername/automation_project.git
cd automation_project
```
2. Install Python Dependencies
```shell
pip install -r requirements.txt
```
3. Configure the Project

	•	Update workflow.sh with the correct paths and configurations.
	•	Modify automation/automation_script.py to suit your automation needs.

4. Make Scripts Executable
```shell
chmod +x scripts/*.py
chmod +x automation/automation_script.py
chmod +x workflow.sh
```
5. Run the Workflow
```shell
./workflow.sh --username your_username --password your_password --app-package com.example.app --app-activity .MainActivity
```
Additional Information ℹ️

	•	Emulator Performance:
	•	For better performance, ensure your system supports hardware acceleration:
	•	Windows: Enable Intel HAXM during Android SDK installation.
	•	macOS: Hardware acceleration is enabled by default.
	•	Linux: Use KVM for hardware acceleration.
	•	Appium Server Logs:
	•	Logs are stored in appium.log.
	•	Adjust logging configurations in scripts/appium_server.py if needed.
	•	Automation Script:
	•	The automation script uses argparse for command-line arguments.
	•	Customize automation/automation_script.py with your automation steps.

Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests.
	1.	Fork the repository 🍴
	2.	Create your feature branch (git checkout -b feature/AmazingFeature) 🌟
	3.	Commit your changes (git commit -m 'Add some AmazingFeature') 🖋️
	4.	Push to the branch (git push origin feature/AmazingFeature) 🚀
	5.	Open a pull request 📬

License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

Happy Automating! 🎉🚀

Disclaimer: Ensure you have the rights and permissions to automate the application you’re testing. Always comply with software licenses, terms of service, and applicable laws. ⚠️
