from typing import Dict, List, Tuple
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def get_work_batch_list() -> List[Tuple[str, List[int]]]  :
    lmd_split = lambda x: [int(i) for i in x.split(',')]
    work_batch_list = [(os.getenv(f'WORK_BATCH_{i}_DESCRIPTION'), lmd_split(os.getenv(f'WORK_BATCH_{i}'))) for i in range(0, 100) if os.getenv(f'WORK_BATCH_{i}') is not None]
    return work_batch_list

def load_variables() -> Dict[int, Tuple[Dict[str, any], Dict[str, any]]] :
    start_time = datetime.strptime( os.getenv('START_TIME') , '%Y.%m.%d %H:%M:%S'  )
    end_time = datetime.strptime( os.getenv('END_TIME') , '%Y.%m.%d %H:%M:%S'  )
    time_diff_start =  datetime.now().hour - start_time.hour
    time_diff_end =  datetime.now().hour - end_time.hour
    
    user_input = { 
        1 : ({ 'target' : 'text', 'value' : [os.getenv('APP_NAME') ]}, {}),
        2 : ({ 'target' : 'selector', 'value' : [ os.getenv('APP_NAME') ] }, {}),
        4 : ({ 'target' : 'selector', 'value' : [ os.getenv('USER_ID') ] }, {}),
        5 : ({ 'target' : 'selector', 'value' : [ os.getenv('USER_PW') ] }, {}),
        8 : ({}, {'target' : 'text' , 'value' : [start_time.strftime("%Y.%m.%d(%a)")] }),
        9 : ({'target' : 'selector' , 'value' : [start_time.strftime("%Y.%m.%d(%a)"), start_time.strftime("%H:%M" ), end_time.strftime("%H:%M") ] }, {}),
        11: ({}, {'target' : 'text' , 'value' : [os.getenv('ROOM_NUM')]}),
        14 : ({}, {'target' : 'selector', 'value' : [start_time.strftime('%d %B %Y')] }),
        16 : ({ 'target' : 'xy_xy', 'value' : str(os.getenv('XY_AMPM_DOWN')) if time_diff_start > 0 else str(os.getenv('XY_AMPM_UP')) }, {}),
        17 : ({'target' : 'xy_xy', 'value' : str(os.getenv('XY_H_DOWN')) },{'target' : 'selector', 'value' : start_time.strftime('%I') }),
        18 : ({'target' : 'xy_xy', 'value' : str(os.getenv('XY_M_DOWN')) },{'target' : 'selector', 'value' : start_time.strftime('%M') }),
        21 : ({ 'target' : 'xy_xy', 'value' : str(os.getenv('XY_AMPM_DOWN')) if time_diff_end > 0 else str(os.getenv('XY_AMPM_UP')) }, {}),
        22 : ({'target' : 'xy_xy', 'value' : str(os.getenv('XY_H_DOWN')) },{'target' : 'selector', 'value' : end_time.strftime('%I') }),
        23 : ({'target' : 'xy_xy', 'value' : str(os.getenv('XY_M_DOWN')) },{'target' : 'selector', 'value' : end_time.strftime('%M') }),
        26 : ({'target' : 'text', 'value' : os.getenv('MEETING_TITLE') },{}),
        27 : ({'target' : 'text', 'value' : os.getenv('MEETING_MESSAGE') },{})
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


  
