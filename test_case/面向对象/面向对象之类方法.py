'''
类方法
特点：
1，定义需要依赖装饰器 @classmethod
2，类方法中的参数不是一个对象，而是类
3，类方法只可以属于类属性
4，类方法中是否可以使用普通方法？不可以
作用：
因为只能访问类属性和类方法，所以在对象创建之前，如果需要完成一些动作（功能）
'''
class Dog():
    name = '阿黄'
    def __init__(self,name):
        self.name = name

    def run(self):  #self 对象
        print('{}正在院子里欢乐的奔跑'.format(self.name))

    @classmethod
    def test(cls):  #cls  class
        print(cls)
        print(cls.name)

d = Dog('狗杂种')
d.run()
d.test()

