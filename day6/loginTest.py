from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from day5.myTestCase import MytestCase


driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element(By.NAME, "username").send_keys("fangyong")
driver.find_element(By.NAME, "password").send_keys("123456")
driver.find_element(By.CSS_SELECTOR,"form > ul > li:nth-child(5) > input").click()
WebDriverWait(driver,20,0.5).until(EC.visibility_of_any_elements_located(By.LINK_TEXT,"进入商场购物"))
#这句显式等待的代码相当于time.sleep(20)的优化版
driver.find_element_by_link_text("进入商城购物").click()