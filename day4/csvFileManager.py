#1.要想读取csv文件，首先要导入csv代码库
#如果要读取excel，需要下载相应的代码库：xlrd
#怎么下载：1.通过命令下载：在dos窗口中输入pip install -U xlrd   -U是升级到最新版的意思   pip是代码库管理工具，是python语言最常用的项目管理工具，和java中的maven类似
#如果同时安装了python2和python3，那么需要把pip改成pip3
#第2中方式，点击file-settings-project下面的interpreter--+搜索需要的代码库，点击安装
import csv
#指定要读取的文件的路径
path = r"C:\Users\51Testing\PycharmProjects\selenium\data\testdata.csv"
#因为字符串中包含反斜线\t等,怎么办？
#1.在每个反斜线前加一个反斜线
#2.把每个反斜线都改成正斜线
#相比第二种方法更好一点，因为java，python都是跨平台的语言
#在字符串中两个反斜线会自动根据转义字符的规则转成一个反斜线
#在windows操作系统中，用反斜线表示目录结构
#但是在linux操作系统中，只有正斜线才能表示目录
#如果双反斜线，那么代码就失去了跨平台能力，在linux里用不了反斜线
#如果用正斜线，代码可以同时在windows和linux中执行
#3在字符串外面加上一个字母r，会认为中间所有的代码都不存在转义字符
print(path)
#3.打开路径所对应的文件
file = open(path,'r')
#4.读取文件的内容，通过csv代码库来读取文件内容
#reader方法是专门用来读取文件的
data_table=csv.reader(file)

#打印data_table中的每一样数据   循环for-each语句
#for是循环的关键字，item代表一行，每循环一次，item就代表最新的一行数据，data_table表示整个文件中的所有数据

for item in data_table:
    print(item)
#很多的测试用例可能都需要从excel中读取数据，所以我们应该对这些代码做一个简单的封装
#建一个文件csvFileManager2,把以上的代码封装到一个方法中
#并且再建一个文件来读取封装方法
