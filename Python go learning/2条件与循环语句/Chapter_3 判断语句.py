# from random import random
#
# print("欢迎来到游乐园")
# high = int(input("请输入你的身高(cm)："))#input输入的所有内容都是字符串类型
# if high >= 120:
#     print("您身高超过120cm，游玩需补票10元")
# else:
#     print("您身高未超过120cm，可以免费游玩")
# print("祝您游玩愉快")
# num = 10
# guess_num = int(input("请输入第一次猜想的数字"))
# if num == guess_num:
#     print("猜对了")
# elif num == int(input("请输入第二次猜想的数字")):
#     print("猜对了")
# elif num == int(input("请输入第三次猜想的数字")):
#     print("猜对了")
# else:
#     print(f"都没猜对，我想的是%d" %num)
import random
num = random.randint(1,10)
# str_num = str(num)
# print(str(num))
# print(str_num)#print("str_num")是把变量str_num当作字符串输出了，而print(str_num)输出的是变量
guess_num = int(input("请输入第一次猜想的数字"))
if num == guess_num:
    print("猜对了")
else:
    if num > guess_num:
        print('猜小了')
    else:
        print('猜大了')
    guess_num = int(input("请输入第二次猜想的数字"))
    if num == guess_num:
        print('第二次猜对了')
    else:
        if num < guess_num:
            print('猜大了')
        else:
            print('猜小了')
        guess_num = int(input("请输入第三次猜想的数字"))
        if num == guess_num:
            print('第三次猜对了')
        else:
            if num < guess_num:
                print('猜大了')
            else:
                print('猜小了')
print(num)
i = 0;
sum = 0;
while i <= 100:
    sum += i
    i += 1
print(sum)
