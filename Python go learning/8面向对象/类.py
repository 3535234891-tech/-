#类：用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例
# 类是程序中的"设计图纸",对象是基于图纸生产的具体实体 面向对象编程就是使用基于类创建的对象来完成具体工作
# 方法：类中定义的函数。若函数体为pass则称为抽象方法
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
#在方法内部如果访问类的其他成员变量时，需要在成员变量之前加上self,但是在调用方法时不需要传入self这个参数 类格式为：
# class 类名称:
#     变量（成员属性）
#
#     def 成员方法(self,参数列表):
#         成员方法体
#
# 对象 = 类名称()

#定义一个带成员方法的类
class Student:
    name = None

    def say_hi(self):
        print(f"大家好啊，我是{self.name}")

    def say_hi1(self,mx):
        print(f"大家好啊，我是{self.name},{mx}")

#构建一个类对象 就可以使用前面的成员属性和方法了

stu = Student()
stu.name = '李超凡'
stu.say_hi()

stu2 = Student()
stu2.name = '欧0'
stu2.say_hi1('过年了')

#在给成员变量赋值时可以用构造方法来简化代码，即用_init_方法（特殊方法）实现：主要是创建类对象时会自动执行该方法，传入参数自动传递给_init_方法使用

class Student2:
     def __init__(self,name,age):
         self.name = name  #在构造方法中定义成员变量，依旧需要self关键字
         self.age = age
         print('Student类创建类一个对象')

stu = Student2('周杰伦',18)
print(stu.name)
print(stu.age)

class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)

# 创建一个类的实例
obj = MyClass(42) #(__init__方法自动执行)

# 调用实例的方法
obj.display_value() # 输出 42


#传统for循环
# for i in range(10):
#      print(f'当前录入第{i}位学生信息，共录入10位学生信息')
#      name = input('请输入学生姓名：')
#      age = input('请输入学生年龄：')
#      print(f'第{i}位学生信息录入完成，信息为姓名：{name}，年龄：{age}')

#利用类来做
class Student3:
    def __init__(self,name,age):
         self.name = name
         self.age = age
for i in range(10):
    print(f'当前录入第{i+1}位学生信息，共录入10位学生信息')
    stu= Student3(name = input('请输入学生姓名：'),age = input('请输入学生年龄：'))
    print(f'第{i+1}位学生信息录入完成，信息为姓名：{stu.name}，年龄：{stu.age}')

#类方法（不需要创建对象）和实例方法（需要创建对象）的区别
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        """实例方法 - 需要具体的对象"""
        return f"我叫{self.name}"


# 必须创建对象才能调用
student = Student("张三")
print(student.introduce())  # 我叫张三


class Student:
    school_name = "清华大学"  # 类属性

    def __init__(self, name):
        self.name = name  # 实例属性

    @classmethod
    def get_school_info(cls):
        """类方法 - 第一个参数是cls，代表类本身"""
        return f"学校名称: {cls.school_name}"

    @classmethod
    def change_school(cls, new_school):
        """类方法可以修改类属性"""
        cls.school_name = new_school
        return f"学校已改为: {cls.school_name}"
