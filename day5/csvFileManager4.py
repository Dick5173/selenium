#1.导包
import csv

import os


class CsvFileManager4:
    def read(self,filename):
        list = [] #声明一个空列表
        #2.指定csv文件的路径
        #path = r"C:\Users\51Testing\PycharmProjects\selenium\data\"
        #这样生成的path路径有一个缺点，可移植性比较差
        #项目换了不同的路径，那么我们每次都要修改代码
        #更好的方法是：
        #os.path.dirname(__file__)这是一个固定写法，用来获取当前文件的目录结构
        #os操作系统，path路径，dirname目录名，__file__是python内置的变量，表示当前文件
        base_path = os.path.dirname(__file__)
        print(base_path)
        #用base_path的好处：不管项目放到任何路径下面，都可以找到该文件的绝对路径
        #我们真正想要的是csv文件的路径，不是代码文件的路径
        #可以通过basepath计算出csv文件的路径
        path = base_path.replace('day5','data/'+filename)
        print(path)
        #3.打开指定文件
        # file = open(path,'r')
        #每次打开文件，最后用完之后要记得关闭该文件，释放系统资源
        #上节课用的是try...finally的方法
        #更常用的方法是 with...as的语法结构
        with open(path,'r') as file:
            data_table = csv.reader(file)
            #4.循环遍历数据表中的每一行
            for row in data_table:
                print(row)
            #我们的测试用例需要调用这些数据，所以要给这个方法设一个返回值，把数据提取出来
                #5.声明一个二维列表，保存data_table中的所有数据
                list.append(row)
        #6.在read方法的末尾返回这个列表
        return list
    #这个方法写完之后，是不是所有的测试用例都应该从这个方法读取csv数据
    #我们不可能为每一个测试用例都单独写一个方法
    #但是这个路径已经写死了，只能读testdata.csv这个文件
    #一个csv文件只适合保存一组测试用例数据
    #所以不同测试用例，应该对应不同的cav文件
    #7.把csv文件名作为参数传进来

if __name__ == '__main__':
    list = CsvFileManager4().read('testdata.csv')
    print(list[1][0])