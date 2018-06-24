
#这个文件用来实现一个登陆功能的自动化操作
#1.打开浏览器
import time
from selenium import webdriver
driver = webdriver.Ie()
#设置隐式等待：如果页面中的元素在20秒内等待，一旦找到页面元素，马上执行后面的语句
#如果超过20秒仍然找不到页面元素，那么程序将会报超时错误
driver.implicitly_wait(20)
#2.打开海盗商城网站
driver.get("http://localhost")
#3.打开登录按钮
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#4.输入用户名和密码
driver.find_element_by_id("username").send_keys("fangyong")
driver.find_element_by_name("password").send_keys("123456")
#5.点击登陆按钮
#所有调用方法
driver.find_element_by_class_name("login_btn").click()
#6检查登陆是否成功
#导包快捷键 ALT+Enter
#time.sleep提供了一种固定的时间等待，这里的意义是点击登录按钮后等5秒，再检查用户名是否正常显示，弊端是因为网络延迟，不知道等1秒合适还是等5秒合适
#结果办法是用只能等待代替固定等待
#time.sleep(5)

username_text=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/a[1]").text
print(username_text)
#我们可以通过if语句，判断页面显示的文本和预期的文本是否一致，来判断测试用例是否正常执行
if username_text =='您好 fangyong':
    print("测试执行通过")
else:
    print("测试执行失败")
#因为selenium主要做回归测试，所以测试脚本开始都是pass的，只有开发做了代码变更，我们的测试用例才有可能失败
#一般工作中不用if...else...进行判断，后面再详细讨论这个问题
#7点击进入商城购物按钮
#driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/dl[1]/dd/div/p/a").click()
#Xpath有一个缺点，定位元素的可读性比较差
driver.find_element_by_link_text("进入商城购物").click()

#8在商城主页输入搜索条件iphone
driver.find_element_by_name("keyword").send_keys("iphone")
#9点击搜索按钮
driver.find_element_by_class_name("btn1").click()
#10点击第一个商品的图片
driver.find_element_by_class_name("shop_01-imgbox").click()
#切换窗口
driver.close()#关闭selenium正在工作的窗口
driver.switch_to.window(driver.window_handles[-1])
#11点击加入购物车
driver.find_element_by_id("joinCarButton").click()
