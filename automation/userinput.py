from typing import Dict, List, Tuple
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def load_variables() -> Dict[int, Tuple[Dict[str, any], Dict[str, any]]] :
    start_time = datetime.strptime( os.getenv('START_TIME') , '%Y.%m.%d %H:%M:%S'  )
    end_time = datetime.strptime( os.getenv('END_TIME') , '%Y.%m.%d %H:%M:%S'  )
    user_input = { 
        1 : ({ 'target' : 'text', 'value' : [os.getenv('APP_NAME') ]}, {}),
        2 : ({ 'target' : 'selector', 'value' : [ os.getenv('APP_NAME') ] }, {}),
        4 : ({ 'target' : 'selector', 'value' : [ os.getenv('USER_ID') ] }, {}),
        5 : ({ 'target' : 'selector', 'value' : [ os.getenv('USER_PW') ] }, {}),
        8 : ({}, {'target' : 'text' , 'value' : [start_time.strftime("%Y.%m.%d(%a)")] }),
        9 : ({'target' : 'selector' , 'value' : [start_time.strftime("%Y.%m.%d(%a)"), start_time.strftime("%H:%M" ), end_time.strftime("%H:%M") ] }, {})
    
                   }
    return user_input

def load_connection() ->  Tuple[str, Dict[str, str]] :
    url = f'http://{os.getenv("ADRESS")}:{os.getenv("PORT")}{os.getenv("BASEPATH")}'

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
    return url, desired_caps


  
