'''
** selenium的任务就是发送命令给浏览器，用以执行某些操作或为信息发送请求

'''

from selenium import webdriver

# 使用驱动实例开启会话
from selenium.webdriver.common.by import By
def setup():
    # 在浏览器上执行操作
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    return driver

def teardown(driver):
    driver.quit()

def test_eight_cmponents():
    driver = setup()
    # 请求浏览器信息(窗口句柄，浏览器尺寸/位置，cookie，警报等)
    title = driver.title
    assert title == "Web from"

    # 建立等待策略
    '''
    将代码和浏览器当前的状态同步
    在尝试定位元素之前，确保该元素位于页面上，并且在尝试与该元素交互之前，该元素处于可交互状态
    隐式等待是selenium提供的一种机制，用于设置查找元素时的最大等待时间，如果在指定的时间内找不到元素，selenium会抛出异常，适合简单场景
    显示等待允许指定等待某个条件成立的最长时间
    '''
    driver.implicitly_wait(0.5)

    # 发送命令查找元素
    '''大多数selenium会话中的主要命令都与元素相关，如果找不到元素，就无法与之交互'''
    text_box = driver.find_element(by=By.NAME, value="my-text")
    sumbit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

    # 操作元素
    '''对于一个元素，只有少数几个操作可以执行，但是经常会被使用'''
    text_box.send_keys("Selenium")
    sumbit_button.click()

    # 获取元素信息
    message = driver.find_element(by=By.ID,value="message")
    text = message.text
    assert text == "received！"
    teardown(driver)




