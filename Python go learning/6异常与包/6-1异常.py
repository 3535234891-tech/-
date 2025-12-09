# bug and debug
# try:
#     把可能出bug的代码提前用try去标记
# except：
#     真出bug时所执行的代码

try:
    f = open("D:/文本文档",'r',encoding='utf-8')
except:
    print('异常时因为文件不存在，以open模式，改为w模式去创建')
    f = open("D:/文本文档", 'w', encoding='utf-8')

# 捕获指定的异常
try:
    #print(name) 这里变量name没定义运行的话会出NameError的异常
    1/0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)
# 捕获多个异常
try:
    print(1/0)
except(NameError,AttributeError) as e:
    print("出现了    或   的异常")

#捕获所有异常
try:
    print(1/0)
except Exception as e:# or except:
    print("出现异常了")

try:
    print(1/0)
except Exception as e:
    print(e)
else:
    print()    #没有异常时执行的代码

try:
    print(1/0)
except Exception as e:
    print()
else:
    print()
finally:
    print()#无论有无异常都会执行的代码

#异常的传递性
def func1():
    print("func1 开始执行")
    num = 1/0
    print("func2 结束执行")

#定义一个无异常的方法，调用上面的方法
def func2():
    print("func2 开始执行")
    func1()
    print('func2 结束执行')

# 定义一个方法，调用上面的方法
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常了，异常的信息是:{e}")

main()