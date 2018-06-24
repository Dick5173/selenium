import csv
#每个测试用例对应着不同的csv文件
#每条测试用例都会打开一个csv文件，所以每次也应该关闭该文件
class csvFileManager3:
    @classmethod
    def read(self):
        path=r"C:\Users\51Testing\PycharmProjects\selenium\data\testdata.csv"
        file=open(path)
        #通过csv代码库读取打开的csv文件，获取到文件中的数据集
        try:  #try尝试执行一下代码
            data_table=csv.reader(file)
            a= [2,3,4,5]
            a[6]  #发生数据下标越界
            for item in data_table:
                print(item)
        #方法最后应该添加close方法
        #如何保证不论程序执行过程中是否报错，都能正常关闭打开的文件
        finally:  #finally最终，无论过程是否报错，都会执行一下代码
            print("file.close()方法被执行")
            file.close()

#如果想测试一下这个方法：
if __name__ == '__main__':
    # csv2=csvFileManager2()
    # csv2.read()
    #如果在方法上面加上classmethod，表示这个方法可以直接调用
    csvFileManager3.read()