'''
私有化
封装：1,私有化属性 2，定义中有set和get方法
__属性：将属性私有化 例如：__name，访问范围仅限于类总
好处：
1，隐藏属性不被外界随意的修改
2，也可以修改：通过函数 setXXX
    def setAge(self,age):
        筛选赋值的内容
        if xxx是否符合条件
            赋值
        else
            不赋值
3,如果想获取具有的某一属性
  使用get函数
    def getAge():
        return self.__xxx

'''


class Students():
    __age = 18  # 类属性

    def __init__(self, name, age):
        self.__name = name  # 长度必须6位
        self.__age = age
        self.__score = 59

    # 定义公有set和get方法
    # set是为了赋值
    def setAge(self, age):
        if age > 60:
            self.__age = age
        else:
            print('您的年龄不符合条件！')

    # get是为了获取
    def getAge(self):
        return self.__age

    def __str__(self):
        return '姓名:{}，年龄:{}，分数:{}'.format(self.__name, self.__age, self.__score)


s = Students('于新宇', 18)
print(s)  # 姓名:于新宇，年龄:18，分数:59
# s.age=19
# #print(s.__score)
# s.__score = 69
# print(s)
# s.setAge(61)
# print(s)
print(s.getAge())
print(dir(Students))
print(dir(s))

