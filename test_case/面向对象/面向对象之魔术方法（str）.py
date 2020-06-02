'''
淡出打印对象名，打印出的是一个地址
__str__
触发时机：打印对象名，自动触发去调用__str__里面的内容
注意：一点要在__str__添加return，return后面的内容就是打印对象看到的内容
    p = Person('JACK', 19)
    print(p)  # 姓名是JACK年龄19

总结：魔术方法
重点：__init__(构造方法;创建完空间之后第一个调用) __str__()
了解;__new__()  开辟空间
     __del__()   没有引用的时候回调用，99%都不需要重新
     __call__()    想不到把对象当成函数调用
'''


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '姓名是' + self.name + '年龄' + str(self.age)


p = Person('JACK', 19)
print(p)
