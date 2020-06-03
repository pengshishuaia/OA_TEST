'''
is a base class 基础类，父类

继承：
    Student，Doctor  --->都属于Person类
    相同的代码--->代码冗余，可读性不高
    将相同的代码提取---->Person类
    Student，Doctor继承Person类

特点：
1，如果类中不定义__init__，调用父类的_init_
2，如果类继承父类也需要自己定义__init__，就需要在当前的类中调用父类init
3，如何调用父类__init__
    super().__init__(name)
    super(Doctor, self).__init__(name)
4，如果父类有eat，子类也定义eat，默认搜索原则，先找当前类，再去找父类
    假如父类提供的方法，不满足子类的方法，就需要在子类中定义个同名的方法
'''


class Person:
    def __init__(self, name):
        self.name = name
        self.age = 18
    def eat(self):
        print('{}正在吃饭'.format(self.name))

    def run(self):
        print('{}正在跑步'.format(self.name))


class Student(Person):
    def __init__(self,name,clazz):
        print('-----Student的init')
        # 如何调用父类的__init__
        super().__init__(name)  #super()调用父类的对象
        self.clazz = clazz
    def study(self,course):
        print('{}岁的{}正在学习{}课程'.format(self.age,self.name,course))

    def eat(self,food):
        # super().eat()  如何还依赖父类修改，需要调用
        print(self.name+'正在吃饭，并吃的是{}'.format(food))


class Doctor(Person):
    def __init__(self,name,patient):
        # 如何调用父类的__init__
        super(Doctor, self).__init__(name)  # super()调用父类的对象
        self.patient = patient



stu = Student('彭帅','3年8班')
stu.run()
stu.study('数学')
#stu.eat('红烧肉')
# list1 = ['张三','李四','王五']
# doc = Doctor('钟南山',list1)
