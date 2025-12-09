"""
本代码演示了
"""
print(10)#整数、浮点数、变量都可以直接输出，只有字符串要加引号“”
print("Hello world")
# 写一个整数字面量
print(type(666))
tel = 18536202455
str_tel = str(tel)
print("我的电话号码是："+str_tel)
# 通过占位的方式，完成字符串的拼接
name = "黑马程序员"
message = "学IT来:%s" %(name)
print(message)
class_num = 57
avg_salary = 20000
print("北京%s，工资%s" %(class_num, avg_salary))
name = "传智播客"
setup_year = 2006
stock_price = 19.99
message = "%s成立于%d，今日股价为%f"%(name, setup_year, stock_price)
print(message)

# 快速字符串格式化
name = "鸡"
stock_price = 19.99
stock_code = 101
stock_price_daily_growth_factor = 1.2
growth_days = 5
stock_price_2 = stock_price * stock_price_daily_growth_factor**growth_days
print(f"公司名称：{name}，股票代码：{stock_code}，当前股价{stock_price}")
print("每日增长系数为：%.2f,经过 %d天增长后，股价达到了%.2f"%(stock_price_daily_growth_factor, growth_days, stock_price_2))
user_name = input("请告诉我用户名称")
user_type = input("用户类型")
print(f"{user_name},您是尊贵的{user_type} 欢迎光临")
