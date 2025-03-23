import subprocess
from selenium.common.exceptions import NoSuchElementException
import time
from appium.webdriver.common.touch_action import TouchAction
import re
from PIL import Image
from io import BytesIO

class common:

    def __init__(self, driver):
        self.driver = driver

    def shortcut(driver,picture):
        # 裁剪截图，仅保留 ImageView 区域
        if picture is not None:
            # 获取控件的位置和大小
            location = picture.location
            size = picture.size

            # 获取屏幕截图
            screenshot = driver.get_screenshot_as_png()

            # 裁剪截图，仅保留 ImageView 区域
            image = Image.open(BytesIO(screenshot))
            left = location['x']
            top = location['y']
            right = left + size['width']
            bottom = top + size['height']
            image_view_screenshot = image.crop((left, top, right, bottom))

            # 保存截图为文件
            image_view_screenshot.save(f"picturedemo.png")
        else:
            print("Failed to get picture element.")

    def check_element_and_swipe(driver,element_locator, swipe_direction='down', max_swipe_attempts=3):
        swipe_attempts = 0

        while swipe_attempts < max_swipe_attempts:
            try:
                # 查找元素
                driver.find_element(*element_locator)
                print("Element found!")
                return True
            except NoSuchElementException:
                print("Element not found. Performing swipe...")
                swipe_attempts += 1

                if swipe_direction == 'down':
                    # 执行向下滑动操作
                    common.swipe_down(driver)
                else:
                    print("Invalid swipe direction. Please provide a valid direction.") 

            time.sleep(1)  # 等待页面加载新内容的时间，可以根据需要进行调整

        print("Element not found after maximum swipe attempts.")
        return False
    
    def check_element(driver,element_locator):
        try:
            # 查找元素
            driver.find_element(*element_locator)
            print("Element found!")
            return True
        except NoSuchElementException :
            print("Element not found")
        return False

    def swipe_down(self):
        # 获取屏幕尺寸
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = screen_size['height'] * 0.8
        end_y = screen_size['height'] * 0.3

        # 创建 TouchAction 对象并执行滑动操作
        action = TouchAction(self.driver)
        action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

        # 等待一段时间，以便页面加载新内容
        time.sleep(1)  # 可根据需要进行调整

    # 执行向下滑动操作
    def swipe_down_detail(driver):
    # 获取屏幕尺寸
        screen_size = driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = screen_size['height'] * 0.8
        end_y = screen_size['height'] * 0.5

        # 创建 TouchAction 对象并执行滑动操作
        action = TouchAction(driver)
        action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

        # 等待一段时间，以便页面加载新内容
        time.sleep(1)  # 可根据需要进行调整

    def is_all_letters_except_hyphen(s):
        pattern = r'^[a-zA-Z-]+$'
        return bool(re.match(pattern, s))

    # 执行向下滑动操作
    def swipe_down_detail_up(driver):
    # 获取屏幕尺寸
        screen_size = driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = screen_size['height'] * 0.5
        end_y = screen_size['height'] * 0.8

        # 创建 TouchAction 对象并执行滑动操作
        action = TouchAction(driver)
        action.press(x=start_x, y=start_y).move_to(x=start_x, y=end_y).release().perform()

        # 等待一段时间，以便页面加载新内容
        time.sleep(1)  # 可根据需要进行调整    

    def swipe_down_rongzi(driver):
        # 获取屏幕尺寸
        screen_size = driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = screen_size['height'] * 0.8
        end_y = screen_size['height'] * 0.75

        # 执行滑动操作
        driver.swipe(start_x,start_y,start_x,end_y,duration=1000) 

    def swipe_up(self):
        # 获取屏幕尺寸
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] / 2
        start_y = screen_size['height'] * 0.8
        end_y = screen_size['height'] * 0.4

        # 执行滑动操作
        self.driver.swipe(start_x,start_y,start_x,end_y,duration=1000)
    @classmethod
    def adb_push(cls,photo):
       
        subprocess.run(["adb", "push", f"{photo}", f"/sdcard/Pictures/{photo}"])

        # 广播照片
        subprocess.run(["adb", "shell", "am", "broadcast", "-a", "android.intent.action.MEDIA_SCANNER_SCAN_FILE", "-d", f"file:///sdcard/Pictures/{photo}"])  
    
          
    
common.adb_push("resume.png") 
       

   
    
    
