# 안드로이드 어플리케이션 자동화 

## Table of Contents 

- 1. [개발 개요 및 배경](#개발-개요-및-배경-)
- 2. [흐름 개요](#흐름-개요-)
- 3. [특이사항](#특이사항-)
- 4. [환경설정](#환경설정-)
- 5. [오류이력](#오류이력-)
- 6. [개발 및 수정이력](#개발-및-수정이력-)

## 1. 개발 개요 및 배경
### 적용 효과
- 데스크탑 버전이 지원이 되지 않는 모바일 어플리케이션내에서의 반복적인 업무를 자동화 할 수 있습니다. 

### 수혜 대상
- 데스크탑 버전이 지원이 되지 않는 모바일 어플리케이션을 자동화하고자 하는 경우
- 사용중인 스마트폰의 제조사가 더 이상 os 업데이트를 지원하지 않는 경우
- 사용하고자 하는 모바일 어플리케이션이 일정버전 이상의 os를 요하는 경우
  
### 제약 사항 : 
#### 운영체제별로 다음과 같은 하드웨어 요구조건이 발생할 수 있습니다. 
- Windows: Enable Intel HAXM during Android SDK installation.
- macOS: Hardware acceleration is enabled by default.
- Linux: Use KVM for hardware acceleration.

#### 생체정보를 통해서만 엑세스가 허용되는 어플리케이션의 경우 이용에 제한이 있을 수 있습니다.  

## 2. 흐름 개요
```shell
[Client Script]
    |        |
    |        |---[Initialize Driver]
    |                 | (Desired Capabilities)
    |        |---[Load Actions (JSON)]
    |
    |------------------> [Appium Server]
                            |          |
                            |          |---[Translate Commands]
                            |                    | (to Mobile Commands)
                            |          |---[Communicate with Device]
                            |
                            |------------------> [Mobile Device]
                                                 |       |
                                                 |       |---[Execute Actions on App]
                                                 |       |      | (UI Interactions)
                                                 |       |---[Send Response]
                                                 |
                                                 |<------------------|
                                                 |
                            |<------------------|
                            |          |
                            |          |---[Process Responses]
                            |
    |<------------------|
    |        |
    |        |---[Handle Results]
    |        |---[Adjustments/Reiterations]
    |
    |---[End/Quit Driver]

```
## 3. 특이사항

|index|주요문제|조치사항|
|---|---|---|
|0|libpulse.so.0:cannot open shared object file : cannot open shared object file :No such file or directory| PulseAudio package 설치 : (4. 환경설정-Linux (Ubuntu 22.04.5 LTS 기준)-[필요 패키지 설치](#필요-패키지-설치-)) 참조|
|1|This user doesn't have permissions to use KVM| 사용자 kvm 권한 부여 : (4. 환경설정-Linux (Ubuntu 22.04.5 LTS 기준)-[필요 패키지 설치](#필요-패키지-설치-)) 참조|
|2|윈도우 nodejs 에서 appium 설치 불가|4. 환경설정-Windows-4. [Appium Server GUI 설치](#Appium-Server-GUI-설치-) 참조|


## 4. 환경설정

### Windows
1. 구글 공식홈페이지에서 Android Sdk Studio 다운로드 (https://developer.android.com/studio)
2. Java jdk 설치
3. JAVA_HOME 사용자 환경 변수 설정
4. Appium Server GUI 설치 ( https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4 )
5. Appium Inspector 설치 (선택사항, https://github.com/appium/appium-inspector/releases)
6. Android Sdk Studio 에서 다음 안내에 따라 command-line-tool 설치

Note: The Android SDK Command-Line Tools package, located in cmdline-tools, replaces the SDK Tools package, located in tools. With the new package, you can select the version of the command line tools you want to install, and you can install multiple versions at a time. With the old package, you can only install the latest version of the tools. Thus, the new package lets you depend on specific versions of the command-line tools without having your code break when new versions are released. For information about the deprecated SDK Tools package, see the SDK Tools release notes.

Source : https://developer.android.com/tools

8. powershell 실행
```powershell
C:\Users\YOURDOMAIN\AppData\Local\Android\Sdk\cmdline-tools/version/bin/sdkmanager.exe "system-images;android-35;google_apis_playstore;x86_64"
C:\Users\YOURDOMAIN\AppData\Local\Android\Sdk\cmdline-tools/version/bin/avdmanager.exe create avd -n YOUR_AVD_NAME -k "system-images;android-35;google_apis_playstore;x86_64" --device "pixel"
```

### macOS
준비중

### Linux (Ubuntu 22.04.5 LTS 기준)

#### 필요 패키지 설치
```shell
sudo apt update
sudo apt install unzip
sudo apt install default-jdk
sudo apt install -y nodejs npm
npm install -g appium


echo 'export JAVA_HOME=/usr/lib/jvm/default-jdk'>>~/.bashrc
echo 'export PATH=$PATH:$JAVA_HOME/bin'>>~/.bashrc

echo 'export ANDROID_SDK_ROOT=~/Android/Sdk'>>~/.bashrc
echo 'export ANDROID_HOME=~Android'>>~/.bashrc 

source ~/.bashrc

curl -L "https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip" -o $ANDROID_SDK_ROOT/cmdl.zip
unzip $ANDROID_SDK_ROOT/cmdl.zip -d $ANDROID_SDK_ROOT


sdkmanager --sdk_root=$ANDROID_SDK_ROOT "platform-tools" "platforms;android-35" "system-images;android-35;google_apis_playstore;x86_64" "emulator"

mv $ANDROID_SDK_ROOT/platform-tools $ANDROID_HOME/platform-tools
mv $ANDROID_SDK_ROOT/platforms $ANDROID_HOME/platforms
mv $ANDROID_SDK_ROOT/system-images $ANDROID_HOME/system-images
mv $ANDROID_SDK_ROOT/emulator $ANDROID_HOME/emulator 

avdmanager create avd -n YOUR_AVD_NAME -k "system-images;android-35;google_apis_playstore;x86_64" --device "pixel"

sudo apt-get install pulseaudio

```

## 오류이력
|날짜|진행내용|담당자|비고|
|---|---|---|---|
|yyyy.MM.dd|undefined|undefined|undefined|



## 개발 및 수정이력
|날짜|진행내용|담당자|비고|
|---|---|---|---|
|yyyy.MM.dd|undefined|undefined|undefined|

