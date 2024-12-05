from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#from appium.webdriver.common.touch_action import TouchAction
from datetime import datetime, timedelta
from typing import Dict, List, Any
import time
import logging

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='app.log',  # Log to a file
                    filemode='a')  # Append mode

class UIAction:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
        
    def make_decision(self, action : Dict[str, Any] ) -> Tuple[bool, int]:
        result = self.perform_decision(action.get('decision_type') , action.setdefault('destination', ''), action.get('selector'), action.get('selector_type') )
        
        if result == 'stop':
            return (True, 0)  # Stop the entire batches
        elif result.isdigit():
            return ( False, int(result))  # Move to specific batch index
        return (False, None)  # Continue with the next batch

    def perform_decision( decision_type : str, destination : str, selector : str, selector_type : str ) -> :
        if decision_type == 'stop_if_ready':
            state_ready = self.confirm_ready( selector, selector_type )
            return 'stop' if not state_ready else destination
        if decision_type == 'start_if_ready':
            state_ready = self.confirm_ready( selector, selector_type )
            return 'stop' if not state_ready else destination  
          
        else :
            raise ValueError( f'Unsupported decision type  : {decision_type}' )

    def confirm_ready(self, selector: str, selector_type: str ) -> bool:
        try:
            element = self.find_element( selector, selector_type)
            return element.is_displayed()
        except Exception as e:
            logging.warning(f'Failed to find or validate the element |---{selector}---|---{selector_type}---|---{str(e)}')
            return False

    def get_attribute( self, selector: str, selector_type: str, attribute_name : str ) -> str :
        element = self.find_element(se)
        return element.get_attribute( attribute_name )
        
    def get_xy(self, xy_value : str, direction : str ) ->List[int] :
        set_value = ''
        if not len(xy_value) > 0 :  
            set_value = os.getenv(f'XY_DEFAULT_{direction}')
        else : 
            set_value = xy_value
        return [ int(item) for item in set_value.split(',') ]

    def perform_action(self, action : Dict[str, Any]) -> None:
        action_type = action.get('type')
        if action_type == 'click':
            self.click_element(action.get('selector'), action.get('selector_type'))
        elif action_type == 'type':
            
            self.type_text(action.get('selector'), action.get('selector_type'), action.get('text'))
        elif action_type == 'swipe':
            list_nums = self.get_xy( action['xy_xy'], action['direction'] )
            self.driver.swipe(*list_nums, duration = 500 )


    def action_wrapper( self, action : Dict[str, Any] ) -> None :
        pass_next = False
        if len(action.get('selector')) > 0 :
            for i in range(0, int( action.get('max_retry') )) :
                time.sleep(1)
                pass_next = self.confirm_ready( action.get('selector'), action.get('selector_type') )
                if pass_next : break
                if i == (int( action.get('max_retry') ) -1 ) : 
                    if not bool( action.get('ignore') ) :
                        raise TimeoutError( f'Action Failed after given amount of retry ; {action.get('max_retry')}' )
                    else :
                        pass
        if not bool( action.get('ignore') ) or pass_next :
            time.sleep(1)
            if len( action.setdefault('subaction', {}).keys() ) > 0 :
                self.iterate_action( action.get('subaction') , action )
            else  : self.perform_action( action )       
        


    def click_element(self, selector: str, selector_type: str) -> None:
        element = self.find_element( selector, selector_type )
        element.click()

    def type_text(self, selector: str, selector_type: str, text : str ) -> None:
        element = self.find_element( selector, selector_type )
        element.send_keys(text)


    def find_element( self, selector : str, selector_type : str ) -> Any:
        if selector_type == 'id':
            return self.driver.find_element( AppiumBy.ID, selector)
        elif selector_type == 'xpath' :
            return self.driver.find_element( AppiumBy.XPATH, selector)
        else :
            raise ValueError( f'Unsupported selector type  : {selector_type}' )

    def iterate_action( self , action : Dict[ str, Any], main_action : Dict[ str, Any ] ) -> None :
        meet_condition = False
        selector = action.get['selector']
        selector_type = action.get('selector_type')
        condition = action.get('condition')
        for i in range(0, int( action.get('max_retry') )) :
            self.perform_action( main_action )
            time.sleep( 1 )
            if condition == 'get_attribute' :
                attribute_value = self.get_attribute( selector, selector_type, action.get( 'attribute_name' ))
                meet_condition =  attribute_value is action.get( 'text' )
            elif condition == 'confirm_ready' :
                meet_condition = self.confirm_ready( selector, selector_type)
            if meet_condition : break
            if i == (int( action.get('max_retry') ) -1 ) :
                raise TimeoutError( f'Action Failed after given amount of retry ; {action.get('max_retry')}' )


