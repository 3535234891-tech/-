#列表
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list_2 = []
# index = 0
# while index < len(my_list):
#     if my_list[index] % 2 == 0:
#         element = my_list[index]
#         my_list_2.append(element)
#     index += 1
# print(my_list_2)


# for i in my_list:
#     if i % 2 == 0:
#         my_list_2.append(i)
#     i += 1
# print(my_list_2)
#

#元组
# cell = ('周杰伦',11,['football','music'])
# print(cell.index(11))
# cell.index('周杰伦')
# print(cell[cell.index('周杰伦')])
# cell[2][0] = 'coding'
#
# print(cell)

#字符串
my_str = "111，马黑，jj"
#先倒序，再切片
result1 = my_str[::-1][3:5]
print(f"方式1结果：{result1}")
#先切片，再倒序
result2 = my_str[4:6][::-1]
print(f"方式2结果：{result2}")

#split分割“，” replace替换“来”为空，倒序字符串
result3 = my_str.split("，")[1].replace("来","")[::-1]
print(f"方案3结果：{result3}")

#集合
my_list = [1,2,3,4,5,3,5,6,7,8,9,10,8,9]
my_set = set()
for item in my_list:
    print(f"列表中元素有：{item}")
    my_set.add(item)
print(f"for循环后集合变为：{my_set}")

#字典
info_dict = {
    '王':{
        "部门" : "科技部",
        "工资" : 3000,
        '级别' : 1
    },
    '李':{
        "部门": "市场部",
        "工资": 5000,
        '级别': 2
    },
    '张':{
        "部门": "市场部",
        "工资": 7000,
        '级别': 3
    },
    '周':{
        "部门": "科技部",
        "工资": 3000,
        '级别': 1
    },
}

for name in info_dict:
    if info_dict[name]['级别'] == 1:
       info_dict[name]['级别'] = 2
       info_dict[name]['工资'] += 1000
print(f"升职加薪后的结果是{info_dict}")