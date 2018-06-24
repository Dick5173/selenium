import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from day5.myTestCase import MytestCase
from day6.DBconnection import DBConnection


class RegisterTest(MytestCase):
    def test_register(self):
        #数据库验证 正常情况
        self.driver.get("http://localhost/index.php?m=user&c=public&a=reg")
        self.driver.find_element(By.NAME, "username").send_keys("fang201805")
        self.driver.find_element(By.NAME, "password").send_keys("123456")
        self.driver.find_element(By.NAME, "userpassword2").send_keys("123456")
        self.driver.find_element(By.NAME, "mobile_phone").send_keys("15612345679")
        self.driver.find_element(By.NAME, "email").send_keys("456@786.com")
        self.driver.find_element(By.CLASS_NAME, "reg_btn").click()
        time.sleep(2)
        new_record = DBConnection().execute_sql_command()
        self.assertEqual("fang201805",new_record[1])
        self.assertEqual("456@786", new_record[2])
        print(new_record)

if __name__ == '__main__':
    unittest.main()