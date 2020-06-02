'''
__init__()初始化
'''


class Phone():
    def __init__(self, name):
        self.brand = '华为'
        self.price = 4999
        self.size = '256G'
        self.name = name

    def Call_Phone(self):
        print('*' * 30)
        print('-----》{}开始用{}手机打电话了'.format(self.name,self.brand))
        print('-----》结束打电话')


p1 = Phone('彭帅')
p1.Call_Phone()

p2 = Phone('王欣欣')
p2.brand='苹果'
p2.Call_Phone()
