import csv
#把读取文件的代码封装成一个方法
class csvFileManager2:
    @classmethod
    def read(self):
        path=r"C:\Users\51Testing\PycharmProjects\selenium\data\testdata.csv"
        file=open(path)
        #通过csv代码库读取打开的csv文件，获取到文件中的数据集
        data_table=csv.reader(file)
        for item in data_table:
            print(item)

#如果想测试一下这个方法：
if __name__ == '__main__':
    # csv2=csvFileManager2()
    # csv2.read()
    #如果在方法上面加上classmethod，表示这个方法可以直接调用
    csvFileManager2.read()