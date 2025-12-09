# 模块是一个python文件，相当于一个工具包，包含了类、函数、变量等，在导入模块后可以使用其中包含的工具
#常用的导入的语法有如下：
import time
# import 模块名    通过import导入time模块使用sleep功能（函数）
import time
print("开始执行")
time.sleep(5) #通过.来确定层级关系
print("结束执行")

#from 模块名 import 功能名   代表直接导入模块中的某一功能
from time import sleep
print("开始执行")
sleep(5)
print("结束执行")

#利用*直接导入import全部功能，同时调用时直接利用该功能，不需要加模板名
from time import *
print("开始执行")
sleep(5)
print("结束执行")

#使用as给特定模块或模块中功能加上别名（原来可能名字复杂）
import time as t #给模块time别名t
print("开始执行")
t.sleep(5)
print("结束执行")

from time import sleep as t#给模块time中的sleep功能别名t
print("开始执行")
t(5)
print("结束执行")

#导入了多个模块后，在调用多个模块中的同名功能时，调用的是后面导入的模块的功能
#开发人员设计了模块后往往会留下一个测试代码，那么我们在导入模块时为了不运行测试代码，利用main变量

#如果一个模块中有_all_变量(是包含了如函数功能的一个列表)，当使用from xxx import *导入时，只能导入这个列表中的元素


#Python包是一个用来管理多个模块的文件夹，在该文件夹下包含了一个_init_py文件，该文件夹可用于包含多个模块文件，包的本质依然是模块
#调用包时仍和前面一样，只不过在层级前面加上包的名称即可
#常见语法有：
#方式一：import 包名.模块名
#包名.模块名.目标功能
#方式二：from 包名 import 模块名
#模块名.功能
#三：from 包名.模块名 import 功能名
#功能


#同理，通过__all__变量(直接写在包的_init_py文件中），控制import*，调包时就只能调__all__变量中包含的模块了