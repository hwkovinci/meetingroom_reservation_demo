from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
#from appium.webdriver.common.touch_action import TouchAction
from datetime import datetime, timedelta
from typing import Dict, Any
import time


class UIAction:
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver

    def confirm_ready(self, selector: str, selector_type: str ) -> bool:
        try:
            element = self.find_element( selector, selector_type)
            return element.is_displayed()
        except Exception as e:
            logging.error(f'Failed to find or validate the element {ui_element_id}: {str(e)}')
            return False

    def get_attribute( self, selector: str, selector_type: str, attribute_name : str ) -> str :
        element = self.find_element(se)
        return element.get_attribute( attribute_name )


    def perform_action(self, action : Dict[str, Any]) -> None:
        action_type = action.get('type')
        if action_type == 'click':
            self.click_element(action.get('selector'), action.get('selector_type'))
        elif action_type == 'type':
            self.type_text(action.get('selector'), action.get('text'), action.get('selector_type'))
#        elif action_type == 'swipe':
#            self.swipe(action['start_x'], action['start_y'], action['end_x'], action['end_y'])
#        elif action_type == 'date_swipe':
#            self.check_date_and_swipe(action.get('selector'), datetime.strptime(action.get('target_date'), "%Y-%m-%d"))


    def action_wrapper( self, action : Dict[str, Any] ) -> None :
        pass_next = False
        for i in range(0, int( action.get('max_retry') )) :
            pass_next = self.confirm_ready( action.get('selector'), action.get('selector_type') )
            if pass_next : break
            if i == (int( action.get('max_retry') ) -1 ) : 
                if not bool( action.get('ignore') ) :
                    raise TimeoutError( f'Action Failed after given amount of retry ; {action.get('max_retry')}' )
                else :
                    pass
        if len( action.get['subaction'].keys() ) > 0 :
            self.iterate_action( action.get('subaction') , action )
        else  : self.perform_action( action )        


    def click_element(self, selector: str, selector_type: str) -> None:
        element = self.find_element( selector, selector_type )
        element.click()

    def type_text(self, selector: str, selector_type: str, text : str ) -> None:
        element = self.find_element( selector, selector_type )
        element.send_keys(text)


    def find_element( self, selector : str, selector_type: str ) -> Any:
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
        retry_count = 0
        for i in range(0, int( action.get('max_retry') )) :
            self.perform_action( main_action )
            time.sleep( 0.5 )
            if condition == 'get_attribute' :
                attribute_value = self.get_attribute( selector, selector_type, action.get( 'attribute_name' ))
                meet_condition =  attribute_value is action.get( 'text' )
            elif condition == 'confirm_ready' :
                meet_condition = self.confirm_ready( selector, selector_type)
            if meet_condition : break
            if i == (int( action.get('max_retry') ) -1 ) :
                raise TimeoutError( f'Action Failed after given amount of retry ; {action.get('max_retry')}' )

#    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int) -> None:
#       TouchAction(self.driver).press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

#    def check_date_and_swipe(self, selector: str, target_date: datetime) -> None:
#        # Sample implementation; adapt based on actual app behavior
#        current_date = datetime.now()
#        while current_date < target_date:
#            # Assume swiping left brings future dates
#            self.swipe(100, 500, 500, 500)  # Modify coordinates as needed
#            current_date += timedelta(days=1)

