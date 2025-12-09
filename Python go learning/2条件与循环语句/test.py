# import random
# num = random.randint(1,100)
# print(num)
# sum = 0
# i = int(input("请输入一个数字"))
# while i!=num:
#     if i>num:
#         print("猜大了")
#     else:
#         print("猜小了")
#     sum += 1
#     i = int(input("请再次输入一个数字"))
# print(f"猜对了，您一共猜了{sum}次")
# print("Hello\tworld")
# print("fucking\tworld")

sum = 0
name = "itaehmxeajnda"
for x in name: #与while循环不同，for无法定义循环条件，只能从被处理的数据集中，依次取出内容处理
    print(x)
    if x == "a":
        sum += 1
print(sum)

#判断偶数个数
import random
num = random.randint(1,100)
sum = 0
for x in range(1,num):
    if x%2 == 0:
       sum += 1
print(num)
print(sum)
