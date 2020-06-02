'''
定义个猫类
'''


class Cat():
    type = '猫'

    # 通过__init__初始化的特征
    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self, food):
        print('{}喜欢吃{}'.format(self.nickname, food))

    def catch_mouse(self, color, weight):
        print('{}抓了一个{}kg的，{}大老鼠'.format(self.nickname, weight, color))

    def sleep(self, hour):
        if hour < 5:
            print('继续睡觉！')
        else:
            print('赶紧起床去抓老鼠')

    def show(self):
        print('现在有一只名字为{}，年龄为{}岁的猫咪'.format(self.nickname, self.age))


# 创建对象
cat1 = Cat('花花', 2, '白色')

# 通过对象调用方法
cat1.catch_mouse('黑色', 10)
cat1.sleep(6)
cat1.eat('黄花鱼')
cat1.show()
