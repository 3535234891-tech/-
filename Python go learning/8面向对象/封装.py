#封装表示将现实世界事物的属性、行为封装到类中，分别描述为成员变量和成员方法，从而完成程序对现实世界的描述
#私有成员变量（方法）定义时以__开头,不可被类对象所调用，但可以被公开的（正常的）成员变量和方法调用
class Phone:
    __current_voltage = 0.5

    def __keep_single_core(self):
         print('单核运行')

    def call_by_5g(self):
        if self.__current_voltage >=1:
            print('电量充足')
        else:
            self.__keep_single_core()
            print('电量不足，单核运行')

phone = Phone()
phone.call_by_5g()

class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable == True:
            print('5g开启')
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g1(self):
        self.__check_5g()
        print('正在通话中')
#建立类对象并调用公开方法
phone = Phone()
phone.call_by_5g1()

#继承是基于已有类(父类）得到新的类(子类),继承的意义在于有多个类时，继承了谁就有了谁的功能，可以把全部继承后只建立一个类对象而使用全部类的属性和方法
#单继承格式：class 子类（父类）
#             类内容体（仅包含新增加的属性和方法）
class Phone:
    IMEt = None
    producer ='HM'

    def call_by_4g(self):
        print('4g通话')
class Phone2022(Phone):
    face_id = '1001'
    def call_by_4g1(self):
        print('2022新功能：4g1')

phone = Phone2022()
print(phone.producer, phone.face_id)
phone.call_by_4g1()

#多继承 class 子类（父类1,....,父类n) 若多个父类中有同名的成员属性或方法，默认以继承顺序为优先级（即继承最左边的同名属性或方法）
#         类内容体


# 复写指的是子类继承父类的成员属性和成员方法后，如果对其不满意，那么可以进行复兴：即在子类中重新定义同名的属性或方法即可
class Phone:
    IMEt = None
    producer ='HM'

    def call_by_4g(self):
        print('父类的4g通话')

class Phone2022(Phone):
    producer = 'ITHEIMA'

    def call_by_4g1(self):
        print('子类的5g通话')

phone = Phone2022()
print(phone.IMEt, phone.producer)
phone.call_by_4g1()

#发现复写父类成员后，类对象调用成员的时候，就会调用复写后的新成员
#如果需要使用被复写的父类成员，需要特殊的调用方式：
#方式一:调用父类成员
#      使用成员变量：父类名.成员变量
#      使用成员方法：父类名.成员方法(self)
#方式二:使用super()调用父类成员
#      使用成员变量:super().成员变量
#      使用成员方法:super().成员方法