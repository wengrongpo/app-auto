import random
import string
import time
from appium import webdriver
import openpyxl
from openpyxl import Workbook
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from common import common
from selenium.common.exceptions import NoSuchElementException


# Appium 服务器的地址和端口
appium_server = 'http://localhost:4723/wd/hub'

# 定义 Appium 的配置
desired_capabilities = {
  "platformName": "android",
  "appium:platformVersion": "13",
  "appium:autoGrantPermissions": "true",
  "appium:dontStopAppOnReset": "true",
  "appium:noReset": "true",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.hpbr.bosszhipin",
  "appium:appActivity": "com.hpbr.bosszhipin.module.launcher.WelcomeActivity"
}

driver = webdriver.Remote(appium_server, desired_capabilities)

time.sleep(5)

# driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.hpbr.bosszhipin:id/img_icon"])[2]').click()
# time.sleep(1)
# driver.find_element(By.ID,'com.hpbr.bosszhipin:id/et_search').send_keys("测试实习生")
# time.sleep(1)
# driver.find_element(By.ID,'com.hpbr.bosszhipin:id/tv_search').click()
# time.sleep(1)

time.sleep(2)
method=common(driver)
num=1
common.adb_push("resume.png") 
while(True):
    
    for i in range(1,4):
        print(f'当前第{num}次沟通')
        driver.find_element(By.XPATH,f'//androidx.recyclerview.widget.RecyclerView[@resource-id="com.hpbr.bosszhipin:id/rv_list"]/android.widget.LinearLayout[{i}]').click()
        time.sleep(1)
        job_name=driver.find_element(By.ID,'com.hpbr.bosszhipin:id/tv_job_name')

        if "测试" in job_name.text or "测开" in job_name.text or "质量" in job_name.text :
            print("符合预期")
        else:
            driver.back()
            continue

        chat=driver.find_element(By.ID,'com.hpbr.bosszhipin:id/btn_chat')
        if(chat.text=='立即沟通'):
            chat.click()
            time.sleep(1)
            driver.find_element(By.ID,'com.hpbr.bosszhipin:id/mMoreIcon').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'(//android.widget.ImageView[@resource-id="com.hpbr.bosszhipin:id/imageResource"])[1]').click()
            time.sleep(1)
            driver.find_element(By.ID,'com.hpbr.bosszhipin:id/mGalleryTextView').click()
            time.sleep(1)
            driver.find_element(By.XPATH,'(//android.view.View[@resource-id="com.hpbr.bosszhipin:id/check_view"])[1]').click()
            time.sleep(1)
            driver.find_element(By.ID,'com.hpbr.bosszhipin:id/button_preview').click()
            time.sleep(1)
            driver.find_element(By.ID,'com.hpbr.bosszhipin:id/button_apply').click()
            time.sleep(1)
            driver.back()
            time.sleep(1)
        driver.back()
        num+=1
    method.swipe_up()    

# 关闭会话
driver.quit()






