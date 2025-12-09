# x = float(input("请输入您的数字"))
# def check(x):
#     print("开始检测")
#     if x < 37:
#         print("通过")
#     else:
#         print("不通过")
# check(x)
#
# def add(a,n):
#     result = a+n
#     return result #通过return返回值，将结果返回给调用者
#     print("anything") #函数体在遇到return后后面的内容都不会再运行了
# r = add(1,2)#函数返回值可以通过变量去接受
# print(r)

# 定义全局变量
money = 500000
# 要求客户输入姓名
name = input("请输入您的姓名：")
# 定义查询函数
def query(x):
    if x == 1:
       print("-----------查询余额-----------")
    print(f"{name},您好，您的余额剩余{money}元")

# 定义存款函数
def saving(num):
     global money
     money += num
     print("------------存款------------")
     print(f"{name},您好，您存款{name}元成功")

     # 调用query函数查询余额
     query(0)

#定义取款函数
def get_money(num):
     global money
     money -= num
     # 调用query函数查询余额
     query(0)

# 定义主菜单函数
def main():
    print("----------主菜单--------")
    print(f"{name},您好，欢迎来到银行，请选择操作")
    print('查询余额\t[输入1]')
    print('存款\t\t[输入2]')
    print('取款\t\t[输入3]')
    print('退出\t\t[输入4]')
    return input('请输入您的选择')

#设置无限循环
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(1)
        continue
    elif keyboard_input == "2":
        num = int(input('您想要存入多少钱？请输入：'))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input('您想要取出多少钱？请输入：'))
        get_money(num)
        continue
    else:
        print('已退出')
        break
