# 继承 is a ， has a
import random


class Road():
    def __init__(self, name, length):
        self.name = name
        self.length = length


class Car():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):  # road = r（r = Road('京承高速',1200)），都指向同一个地址
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}上以{}速度行驶{}小时'.format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的，速度:{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('京承高速', 1200)
r.name = '青藏高速'
print(r.name)
audi = Car('奥迪', 120)
print(audi)
audi.get_time(r)  # 对象
