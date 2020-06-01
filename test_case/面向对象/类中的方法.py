# 类中的方法：动作
# 种类：普通方法 类方法 静态方法，魔术方法
'''
普通方法格式
def 方法名(self[参数一，参数二]):
'''


class Phone():
    brand = '小米'
    price = 3999
    type = 'mate 820'

    # Phone类里面的方法：call
    def call(self):
        print('--------',self)
        print('正在打电话中....')
        print('正在访问{}'.format(self.note))


phone1 = Phone()
phone1.note = 'phone1的记事本'
print(phone1)
print(phone1.brand)
phone1.call()

print('*'*30)

phone2 = Phone()
phone2.note = 'phone2的记事本'
print(phone2)
print(phone2.brand)
phone2.call()

