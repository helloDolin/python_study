'''
object是所有类的基类
python支持多继承
python的构造函数是分为两个部分的，先__new__ 再去初始化__init__
既支持面向过程编程又支持面向对象编程
对象：类对象、实例对象
类属性，对象属性；类方法，对象方法
类属性,所有实例对象共享类属性
__del__,当引用计数为0的时候调用此方法，同 OC 的dealloc
'''
import sys


class Car(object):

    level = 'B'  # 公有类属性
    __level = 'B'  # 私有类属性

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.color = 'white'  # 公有对象属性
        self.__price = 1000000  # 私有对象属性

    def __str__(self):
        return('自定义打印对象信息')

    def __del__(self):
        pass

    def drive(self):
        self.__drive()

    def __drive(self):
        print('私有方法')

    # 类方法 第一个参数需要传类的引用

    @classmethod
    def testClsMethod(cls):
        print('testClsMethod')

    # 静态方法 可以不传任何参数
    @staticmethod
    def testStaticMethod():
        print('testStaticMethod')


class Volvo(Car):
    def drive(self):
        print('Volvo drive')


class Jili(Car):
    def drive(self):
        print('Jili drive')

# 领克同时继承沃尔沃和吉利


class Lynk(Volvo, Jili):
    pass


lynk = Lynk()
lynk.drive()
Lynk.testClsMethod()
Lynk.testStaticMethod()

# 获取引用计数的个数
print(sys.getrefcount(lynk))
