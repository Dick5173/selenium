#1.登录海盗商城
#因为大部分测试用例都会用到登录功能，那么我们可以把登录功能单独封装成一个方法，每次直接调用这个方法就可以了
#以后每次登录，就只需要一行代码就可以了
from selenium import webdriver
# import time

from day2.loginTest import Login
driver=webdriver.Chrome()
#implicitly_wait主要检测页面加载时间，检测什么时候页面加载完，什么时候执行后续的操作
driver.implicitly_wait(20)
#实例化对象会占用内存，pycharm会自动帮我们释放内存
#代码运行完检测到Login()这个对象不在被使用，系统会自动释放内存
#把driver浏览器传入到登录方法中
#让登录方法使用传进来的driver

Login().loginWithDefaultUser(driver)
# driver.get("http://localhost")
# driver.execute_script('document.getElementsByClassName("site-nav-right fr")[0].childNodes[1].removeAttribute("target")')
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_id("username").send_keys("fangyong")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_class_name("login_btn").click()
# time.sleep(5)
#2.点击“账号设置”
#本来要点“账号设置”，需要使用driver这个变量，但是现在文件中没有driver变量了。可以重新声明一个driver
driver.find_element_by_link_text("账号设置").click()
#3.点击“个人资料”
#partial_link_text可以对链接中的一部分进行元素定位
#文本过长是可以使用，只要在网页中唯一即可
#xpath的方法比较通用，可以用工具自动生成
#但是不推荐使用，作为一种没有办法是使用的办法
#因为xpath的可读性和可维护性较差
#driver.find_element_by_link_text("个人资料").click()
driver.find_element_by_partial_link_text("个人资料").click()
#4.修改真实姓名
#如果输入框中原本有内容，那么我们修改内容时，往往需要先清除原来的值，用clear()
#实际上，一个良好的编程习惯是在每次sendkeys前清除
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("方勇")
#5.修改性别
#想通过value属性定位有两种方法 xpath和css_selector
#通过cssselector定位元素，只需要在唯一的属性两边加一堆中括号即可
# driver.find_element_by_css_selector('[value="1"]').click()
#在xpath中//表示采用相对路径定位元素
#/ 表示绝对路径，一般都是从/html开始定位元素
#相对路径一般通过元素的特殊属性查找元素
#绝对路径一般对过元素的位置，层级关系查找元素
#绝对路径写起来比较长，涉及到的节点比较多，当开发人员修改页面布局是，受到影响的可能性比较大
#相对路径，查询速度比较慢，因为可能需要遍历更多的节点
#工作中推荐用css_selector
#css_selector的查询速度比xpath快一点，xpath在某些浏览器上支持不太好
#css_selector所有前端都会用，易于沟通交流
# *表示任意节点  [@]表示通过属性定位
# driver.find_element_by_xpath('//*[@value="1"]').click()
#javascript的getElementsByClassName()方法可以找到页面上符合条件的所有元素
#然后下标选取其中的第n个元素，也可以用于定位
#selenium
driver.find_elements_by_id("xb")[2].click()
#6.修改生日
#一下一下点年月日是可以实现的，但是稳定性比较差，很容易点错。并且很难修改日期
#因为readonly属性
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1993-03-05")
#7.修改QQ
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("12345678")
#8.点击确定，保存成功
driver.find_element_by_id("true_name").submit()

