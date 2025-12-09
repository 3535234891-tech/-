#设计一个类，完成数据封装
class Record:
     def __init__(self,data,order_id,money,province):
         self.data = data          #日期
         self.order_id = order_id  #订单ID
         self.money = money        #订单金额
         self.province = province  #销售省份

#设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能

class Filereader:
    #相关功能为：读取文件数据，读到的每一条都转换为Record对象，将他们封装到list内即可
    def read_data(self) -> list[Record]:
        pass
class TextFilereader:
    def __init__(self,path):
        self.path = path

# 复写子类（实现抽象方法）父类的方法：
def read_data(self) -> list[Record]:
    f = open(self.path,'r',encoding='utf-8')
    record_list = []
    for line in f.readlines():
        line = line.strip()  #消除读取到的每一行数据的\n
        data_list = line.split(',') #将每一行按逗号分割
        record_list.append(Record(data_list,data_list[0],data_list[1],int(data_list[2])),data_list[3])#将处理后的数据转换为Record对象并封装成列表

    f.close()
    return record_list

# 用main方法测试
if __name__ == '__main__':
      text_file_reader = TextFilereader('文件路径')
      text_file_reader.read_data()

