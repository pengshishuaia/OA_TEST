'''
#在开发中看的一些私有化处理，装饰器
'''


class Students():
    __age = 18  # 类属性

    def __init__(self, name, age):
        self.name = name  # 长度必须6位
        self.__age = age
        self.__score = 59
    # 固定格式：
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print('您的年龄不符合条件！')

    # 定义公有set和get方法
    # set是为了赋值
    # def setAge(self, age):
    #     if age > 60 and age <100:
    #         self.__age = age
    #     else:
    #         print('您的年龄不符合条件！')

    # get是为了获取
    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return '姓名:{}，年龄:{}，分数:{}'.format(self.name, self.__age, self.__score)


p = Students('彭帅', 68)
p.age = 35
print(p.age)
print(p.__dir__())
