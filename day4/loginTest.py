#用unittest写一个后台登录的测试用例
#1.导包
import unittest
#2建类，并继承unittest.TestCase
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class loginTest(unittest.TestCase):
    #3.重写setup和teardown方法
    @classmethod
    def setUpClass(self):
        #做web自动化测试，所有的测试用例都要先打开浏览器
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
    #窗口最大化代码，要求驱动版本必须和浏览器精准匹配
        self.driver.maximize_window()
    #4个空格在pycharm中可以用TAB键代替
    #对于初学者或者找工作的来讲，格式是最重要的
    #算法是程序的灵魂，格式是程序的外表
    @classmethod
    def tearDownClass(self):
        time.sleep(30)
        #每次执行完测试用例，应该把打开的浏览器关闭，释放内存，清除cookie和缓存，为下次执行测试用例做准备
        #这里调用的driver是声明在setup方法中的一个局部变量，局部变量是不允许被其他方法访问的，所以我们应该把setup方法中声明的driver改成一个全局变量。因为self表示类本身，所以我们只要把变量前加上self.  就表示这个变量属于类的
        self.driver.quit()
    def test_login(self):
        #因为每次使用driver变量是都需要在前面加一个self，为了简化代码，可以吧成员变量的属性self.driver改写赋值给局部变量driver
        driver=self.driver
        driver.get("http://localhost/index.php?m=admin&c=public&a=login")
        driver.find_element_by_name("username").send_keys("admin")
        #有些常用的键也可以用转义字符代替，其中\t表示TAB键，\N表示ENTER键
        ActionChains(driver).send_keys("\tpassword").send_keys("\t1234").send_keys("\n").perform()

        #添加商品的代码
        #如果第二个方法重新打开一个浏览器，登录就无效了
    def test_product_adding(self):
        driver=self.driver
        driver.find_element_by_link_text("商品管理").click()
        driver.find_element_by_link_text("添加商品").click()
        #除了用name属性切换frame，也可以通过8中元素定位方法定位元素然后切换
        iframe=driver.find_element_by_id("mainFrame")
        driver.switch_to_frame(iframe)
        driver.find_element_by_name("name").send_keys("PS4")
        #如果ID是纯数字，用#的方式不能定位，可以用[]的方式定位
        driver.find_element_by_css_selector('[id="1"]').click()
        driver.find_element_by_id("2").click()
        driver.find_element_by_id("6").click()
        ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
        select=Select(driver.find_element_by_name("brand_id"))
        select.select_by_value("1")
        driver.find_element_by_name("button_search").click()



if __name__ == '__main__':
    unittest.main()