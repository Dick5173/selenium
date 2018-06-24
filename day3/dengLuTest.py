#selenium执行javascript中的两个关键字:return(返回值)和argument(参数)
from itertools import product

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("http://localhost")
#点击登录链接
#用javascript的方法找登录链接的代码：
#document.getElementByClassName("site-nav-right fr")[0].childNodes[1]
#用selenium的方法找登录链接的代码：
#driver.find_element_by_link_text("登录")
#某些元素，用selenium的方法比javascript更容易
#虽然selenium不支持removeAttribute的方法
#但是selenium找的登录链接和javascript找到的是同一个元素
#我们可以用selenium找到元素后，转换为javascript的元素
login_link=driver.find_element_by_link_text("登录")
#把原来的javascript看成是一个无参无返的方法，现在直接从外面传入一个页面元素，就变成一个有参无返的方法、
#arguments参数的复数形式，[0]表示第一个参数，指的就是js后面的ligin_link
#所以下面这句代码相当于把driver.find_element_by_link_text("登录")带入到javascript语句中
#变成了driver.find_element_by_link_text("登录").removeAttribute('target')
#arguments是参数数组，指的是js字符串后面的所有参数
#一般情况下我们只会用到arguments[0]，即js后面的第一个字符串
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("fangyong")
driver.find_element_by_id("password").send_keys("123456")
ActionChains(driver).send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text("返回商城首页").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#因为img没有target属性，所以我们复制css的时候要找它的父节点a标签
#复制出的css往往比较长，我们可以适当的缩写长度
#我们定位元素的目标节点是最后一个节点，最后一个节点是不能被删除的
#大于号的前面是父节点，后面是子节点
#每个节点的第一个单词是标签名，比如a，div，body
#小数点后面表示class属性
#：nth-child（2），nth表示第几个4th，5th表示第n个，child表示子节点
#所以：nth-child(2)表示当前标签是它的父节点的第二个子节点
product_link_css="body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > div.shop_01-imgbox > a"
iphone = driver.find_element_by_css_selector(product_link_css)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_css_selector("body > div.shop_last.w1100 > div.other_shopl.fl > div.shopCar_T > span.shopCar_T_span3").click()
#点击结算按钮
#在每个class前面都加一个小数点，并且去掉中间的空格，我们就可以同时用两个class属性定位一个元素
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
#点击添加新地址
driver.find_element_by_css_selector(".add-address").click()
#输入收货人等信息
driver.find_element_by_name("address[address_name]").send_keys("fangyong")
driver.find_element_by_name("address[mobile]").send_keys("15612341234")
dropdown1=driver.find_element_by_id("add-new-area-select")
#下拉框是一种特殊的网页元素，对下拉框的操作和普通网页元素不太一样
#selenium为这种特殊的元素专门创建了一个类Select
#dropdown1的类型是一个普通的网页元素，下面这句代码的意思是
#把一个普通的网页元素，转换成一个下拉框的特殊网页元素
print(type(dropdown1)) #dropdown1是Web_Element类型
#WebElement这个类中，只有click和send_key这样的方法，没有选择下拉框的方法
select1 =Select(dropdown1)
print(type(select1)) #select1是select类型
select1.select_by_value("320000")#这时我们选项的值来定位
time.sleep(2)
select1.select_by_visible_text("辽宁省")#也可以通过选项的文本信息来定位
#因为是动态id，所以不能通过id定位
#因为class重复，我们也不能直接用class定位，但是我们可以用find_elements的方法，先找到页面所有class=add-new-area-select的元素，然后再通过下标的方式选择第n个页面元素
dropdown2=driver.find_elements_by_class_name("add-new-area-select")[1]
select2=Select(dropdown2)
select2.select_by_value("210100")
dropdown3=driver.find_elements_by_class_name("add-new-area-select")[2]
select3=Select(dropdown3)
select3.select_by_value("210106")
driver.find_element_by_class_name("add-new-name-span-2").send_keys("铁西市政府")
driver.find_element_by_class_name("add-new-name-span-3").send_keys("123456")
#保存收货人信息
driver.find_element_by_class_name("aui_state_highlight").click()