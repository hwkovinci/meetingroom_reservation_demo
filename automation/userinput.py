from typing import Dict, List, Tuple
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def get_work_batch_list() -> List[Tuple[str, List[int]]]  :
    lmd_split = lambda x: [int(i) for i in x.split(',')]
    work_batch_list = [(os.getenv(f'WORK_BATCH_{i}_DESCRIPTION'), lmd_split(os.getenv(f'WORK_BATCH_{i}'))) for i in range(0, 100) if os.getenv(f'WORK_BATCH_{i}') is not None]
    return work_batch_list

def datetime_compare( compare_time : datetime ) -> int :

    if datetime.now().strftime('%p') == compare_time.strftime('%p') : return 0
    elif datetime.now().hour - compare_time.hour > 0 : return 1
    else : return -1
 
def get_swap_value( compare_time : datetime ) -> str :
    swap_value = ''
    val = datetime_compare(  compare_time )
    if val == 0 :
        swap_value = str( os.getenv( 'XY_AMPM_NONE' ) )
    elif val == 1 :
        swap_value = str( os.getenv( 'XY_AMPM_DOWN' ) )
    elif val == -1 :
        swap_value = str( os.getenv( 'XY_AMPM_UP' )  )
    return swap_value

def load_variables() -> Dict[int, Tuple[Dict[str, any], Dict[str, any]]] :
    start_time = datetime.strptime( os.getenv('START_TIME') , '%Y.%m.%d %H:%M:%S'  )
    end_time = datetime.strptime( os.getenv('END_TIME') , '%Y.%m.%d %H:%M:%S'  ) 

    swap_value_start =  get_swap_value( start_time )

    swap_value_end = get_swap_value( end_time )

    
    user_input = { 
        1 : ({ 'target' : 'text', 'value' : [os.getenv('APP_NAME') ]}, {}),
        2 : ({ 'target' : 'selector', 'value' : [ os.getenv('APP_NAME') ] }, {}),
        5 : ({ 'target' : 'text', 'value' : [ os.getenv('USER_ID') ] }, {}),
        6 : ({ 'target' : 'text', 'value' : [ os.getenv('USER_PW') ] }, {}),
        9 : ({}, {'target' : 'text' , 'value' : [start_time.strftime("%Y.%m.%d(%a)")] }),
        10 : ({'target' : 'selector' , 'value' : [start_time.strftime("%Y.%m.%d(%a)"), start_time.strftime("%H:%M" ), end_time.strftime("%H:%M") ] }, {}),
        12: ({}, {'target' : 'text' , 'value' : [os.getenv('ROOM_NUM')]}),
        15 : ({'target' : 'selector', 'value' : [start_time.strftime('%d %B %Y')] }, {}),
        17 : ({'target' : 'selector', 'value' : [start_time.strftime('%d %B %Y')] }, {}),          
        20 : ({ 'target' : 'xy_xy', 'value' : [ swap_value_start ] }, {}),
        21 : ({'target' : 'xy_xy', 'value' : [str(os.getenv('XY_H_UP'))]  },{'target' : 'selector', 'value' : [start_time.strftime('%I')] }),
        22 : ({'target' : 'xy_xy', 'value' : [str(os.getenv('XY_M_UP'))] },{'target' : 'selector', 'value' : [start_time.strftime('%M')] }),
        25 : ({ 'target' : 'xy_xy', 'value' : [ swap_value_end ]  }, {}),
        26 : ({'target' : 'xy_xy', 'value' : [str(os.getenv('XY_H_UP'))] },{'target' : 'selector', 'value' : [end_time.strftime('%I')] }),
        27 : ({'target' : 'xy_xy', 'value' : [str(os.getenv('XY_M_UP'))] },{'target' : 'selector', 'value' : [end_time.strftime('%M')] }),
        30 : ({'target' : 'text', 'value' : [os.getenv('MEETING_TITLE')] },{}),
        31 : ({'target' : 'text', 'value' : [os.getenv('MEETING_MESSAGE')] },{})
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


  
