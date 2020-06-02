'''
魔术方法：
__init__初始化魔术方法
触发时机：初始化对象时触发
__new__()

__call__()
__del__()
1,对象赋值
    p = Person（）
    p1 = p
    p2 = p
    说明p p1 p2共同指向同一个地址
2，删除地址的引用
    del p1 删除p1对地址的引用
3，查看引用次数
    import sys
    sys.getrefcount(p)
4,当一块空间没有任何引用，默认执行__del__

__str__
'''

import sys
class Person():
    def __init__(self, name):
        print('---------init', self)  # 第二步：将创建的地址赋值给init<__main__.Person object at 0x021E7430>
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('---------new')
        position = object.__new__(cls)
        print(position)  # 第一步：创建内存地址 <__main__.Person object at 0x021E7430>
        return position
    def __call__(self, *args, **kwargs):
        print('---------call')
        print('执行对象的参数为{}'.format(*args))

    def __del__(self):
        print('------del------')


p = Person('jack')
print(p)  # 最后<__main__.Person object at 0x021E7430>
p('ps')   # 默认调用__call__函数，执行结果：执行对象的参数为ps
p1 = p
p2 = p
print(sys.getrefcount(p))
del p1
print(sys.getrefcount(p))
