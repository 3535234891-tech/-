# 字典是由key和value组成的键值对构成的，格式为：d = {key1 : value1, key2 : value2 } 在添加字典元素时
#字典名[key] = value1 若原字典中有key，将其对应的原value更新为value1，若没有key 会把key和value1同时添加到字典中
tinydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
tinydict['Name'] = 8
tinydict['highth'] = '170cm'
print(tinydict)

# Python pymysql库的基础操作
from pymysql import Connection
# 构建Mysql数据库的链接

coon = Connection(
    host='localhost',  #主机名（IP）
    port=3306,
    user='root',
    password = "123456"
)

print(coon.get_server_info())

# 执行非查询性质SQL

