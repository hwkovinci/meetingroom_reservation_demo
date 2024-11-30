**Session**
```python
options = AppiumOptions()
options.load_capabilities({
	"appium:DeviceName": "Android",
	"platformName": "Android",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
```
**Swipe Gesture**
```python
from appium.webdriver.common.touch_action import TouchAction

# Create a TouchAction instance
action = TouchAction(driver)

# Perform swipe action
action.press(x=start_x, y=start_y) \
      .move_to(x=end_x, y=end_y) \
      .release() \
      .perform()
```


	
## Click (ID)
com.google.android.apps.nexuslauncher:id/search_container_hotseat

## Type (ID)
com.google.android.apps.nexuslauncher:id/input

## Click (XPATH)
//android.widget.TextView[@content-desc="회의실 예약"]

## Click (ID)
com.android.permissioncontroller:id/permission_deny_button

## Type (ID)
com.etnersplatform.booki:id/et_input_id

## Type (ID)
com.etnersplatform.booki:id/et_input_pwd

## Click (ID)
com.etnersplatform.booki:id/btn_login_confirm

## Click (ID)
com.etnersplatform.booki:id/bottom_nav_usage
# While 
### (ID) com.etnersplatform.booki:id/tvDateToday
  Get Attribute , Text
  #### =! 
  ```python
in_datetime_start.strftime("%Y.%m.%d(%a)")
```
  => Click (ID) com.etnersplatform.booki:id/right
## Element Exist (Xpath)
```python
f'//android.widget.TextView[@resource-id="com.etnersplatform.booki:id/tv_Time" and @text="{in_datetime_start.strftime("%Y.%m.%d(%a)} {in_datetime_start.strftime("%H:%M")} ~ {in_datetime_end.strftime("%H:%M")}"]'
```
## return bool


## Click (ID)
com.etnersplatform.booki:id/bottom_nav_info

## While 
### (ID) com.etnersplatform.booki:id/tvName 
  Get Attribute , Text 
  #### =! 302
  => Scroll Down

## Click (ID)
com.etnersplatform.booki:id/button


## Click (ID)
com.etnersplatform.booki:id/tvSelectDate

## While 
### (XPATH) 
```python
f'''//android.view.View[@content-desc="{in_datetime_start.strftime('%d %B %Y')}"]'''
```
  #### Element Exist =! false
=> Click (ID) android:id/next

## Click (ID)
com.etnersplatform.booki:id/tvStartTime

## Assign
```python
int_diff =  datetime.now().hour - in_datetime_start.hour
"up" if int_diff > 0 else "down"
```
## IF 
```python
in_datetime_start.strftime('%p') =! datetime.now().strftime('%p')
```
=> Scroll 
```python
f'("up" if int_diff > 0 else "down")' 
``` 

## While 
### (XPATH) 
```python
f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{in_datetime_start.strftime('%I')}"]'''
```
  #### Element Exist =! false
=> Scroll down


## While 
### (XPATH) 
```python
f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{in_datetime_start.strftime('%M')}"]'''
```
  #### Element Exist =! false
=> Scroll down


## Click (ID)
com.etnersplatform.booki:id/tvStartTime

## Assign
```python
int_diff =  datetime.now().hour - in_datetime_start.hour
```
## IF 
```python
in_datetime_start.strftime('%p') =! datetime.now().strftime('%p')
```
=> Scroll 
```python
f'("up" if int_diff > 0 else "down")' 
``` 

## While 
### (XPATH) 
```python
f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{in_datetime_start.strftime('%I')}"]'''
```
  #### Element Exist =! false
=> Scroll down


## While 
### (XPATH) 
```python
f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{in_datetime_start.strftime('%M')}"]'''
```
  #### Element Exist =! false
=> Scroll down

## Click (ID)
com.etnersplatform.booki:id/btn_ok



## Click (ID)
com.etnersplatform.booki:id/tvEndTime

## Assign
```python
int_diff =  datetime.now().hour - in_datetime_end.hour
```
## IF 
```python
in_datetime_end.strftime('%p') =! datetime.now().strftime('%p')
```
=> Scroll 
```python
f'("up" if int_diff > 0 else "down")' 
``` 

## While 
### (XPATH) 
```python
f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{in_datetime_end.strftime('%I')}"]'''
```
  #### Element Exist =! false
=> Scroll down


## While 
### (XPATH) 
```python
f'''//android.widget.EditText[@resource-id="android:id/numberpicker_input" and @text="{in_datetime_end.strftime('%M')}"]'''
```
  #### Element Exist =! false
=> Scroll down

## Click (ID)
com.etnersplatform.booki:id/btn_ok


## While 
### (ID) 	com.etnersplatform.booki:id/btnOk
  #### Element Exist =! false
=> Scroll down

## Type (ID) 
com.etnersplatform.booki:id/etTitle

## Type (ID) 
com.etnersplatform.booki:id/etMessage

### Click (ID) 	
com.etnersplatform.booki:id/btnOk


