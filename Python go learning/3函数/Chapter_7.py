def test_fuc(compute):
    result = compute(1,2)
    print(result)

def compute(x,y):
    return x+y

test_fuc(compute)
#
# 如果函数体内部没有print,那调用函数时虽然会运行到想要的结果但也不会输出任何值
# 同样return只是返回值给调用者，如果本身函数内部没有print，调用函数时也不会输出任何值，要用变量去接受返回值再打印或者直接打印调用的函数

#通过lambda匿名函数的形式你，将匿名函数作为参数传入。格式为：lambda 传入参数:函数体（一行代码）