# 多态指的是完成某个（函数）行为时，使用不同的对象得到不同的状态
# 常用在继承关系上，比如方法形参声明接受父类对象，实际传入了子类对象做具体工作，用以获得同一行为，不同状态

class Animal:
    def speak(self):
        pass

class Dog(Animal): #子类Dog
    def speak(self):
        print('汪汪汪')

class Cat(Animal):   #子类Cat
    def speak(self):
        print('喵喵喵')

def make_noise(animal:Animal):  # 需要传入Animal类建立的对象
    animal.speak()

#演示多态，使用2个子类对象来调用函数
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

#Animal的speak是空方法，是空实现 因为父类用来确定有哪些方法，具体的方法实现由子类决定，称这种写法为抽象类 好比定义一个抽象方法 子类必须实现

class AC:
    def cool_wind(self):
        """"制冷"""
        pass
class Midea_AC(AC):
    def cool_wind(self):
        print('美的核心制冷')

class GREE_AC(AC):
    def cool_wind(self):
        print('格力变频制冷')

def make_cool(ac:AC):
    ac.cool_wind()  #函数体是实现传入对象的cool_wind方法

midea_ac = Midea_AC() #构建子类Midea_ac的对象
gree_ac = GREE_AC()   #构建子类GREE_ac的对象

#利用多态，使用两个子类对象调用函数

make_cool(midea_ac ) #根据定义的函数即实现 midea_ac.cool_wind()
make_cool(gree_ac)

# 配合多态可以完成 抽象的父类设计（设计标准）和具体的子类实现（实现标准）


