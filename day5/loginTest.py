import time
from selenium.webdriver.common.by import By
import unittest

from day5.myTestCase import MytestCase


class LoginTest(MytestCase):
    def test_login(self):
        driver = self.driver
        driver.get("http://localhost/index.php?m=user&c=public&a=login")
        driver.find_element(By.NAME,"username").send_keys("fangyong")
        driver.find_element(By.NAME,"password").send_keys("123456")
        old_title = driver.title
        driver.find_element(By.CSS_SELECTOR,"body > div.login_main.w1180.clearfix > div.login.fr > form > ul > li:nth-child(5) > input").click()
        time.sleep(5)
        new_title = driver.title
        #这时如果新标题和旧标题不相等，就说明页面发生了跳转，如果相等就说明没登陆成功，页面没跳转
        print("旧页面："+old_title)
        print("新页面："+new_title)
        self.assertNotEqual(old_title,new_title)

if __name__ == '__main__':
    unittest.main()