from appium import webdriver
import time
desired_caps = 	{

#系统版本
    "platformVersion": "5.1.1",
#系统名称
    "platformName": "Android",
#软件包名   adb shell pm list package -3
	"appPackage": "com.ss.android.ugc.aweme",
#软件的activity启动路径
	"appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
#adb设备名称   adb devices
	"deviceName": "127.0.0.1:62001"
	}
#获取手机驱动，需要俩个参数 一个是远程地址 一个是手机相关信息
#启动软件驱动
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

# 自己写刷抖音
def get_size(self):
	x = self.driver.get_window_size()['width']
	y = self.driver.get_window_size()['height']
	return(x,y)
def swipe_up(self,t):
	screen = self.get_size()
	self.driver.swipe(screen[341]*0.5,screen[908]*0.75,screen[341]*0.5,screen[341]*0.25,5000)
# time.sleep(10)
time.sleep(50)


#点击同意
driver.find_element_by_id("com.ss.android.ugc.aweme:id/a-8").click()
# 点击允许
time.sleep(3)
el2 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el2.click()
#点击允许
time.sleep(3)
el3 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
el3.click()

while True:
    time.sleep(10)
    start_x = 350
    start_y = 800
    distance = 500
    driver.swipe(start_x,start_y,start_x,start_y-distance)





#关闭app 回收资源
# driver.close_app()
#
# driver.quit()














