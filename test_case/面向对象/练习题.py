'''
需求：
-----------------------------------------------------------
1.房子有户型，总面积和家具名称列表，新房子没有任何的家具

2.家具有名字和占地面积，其中
          床： 占4平米
        衣柜： 占2平米
        餐桌： 占1.5平米

3.将以上三件家具添加到房子中

4.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
-------------------------------------------------------------
分析：
-------------------------------------------------------------
# 1.由于要将家具放入房子中,所以需要先创建家具类

# 2.家具类:
#   (1)属性:名字(name),占地面积(area)
#   (2)对象:床(bed),衣柜(closet),餐桌(table)

# 3.房子类:
#   (1)属性:户型(house_style),总面积(zarea),
#      家具名称列表(namelist) (新房子没有任何的家具,即初始家具名称列表为空列表)
#      剩余面积(farea) (由于打印房子时,要求输出'剩余面积',所以剩余面积为房子的隐含属性)
#   (2)方法:添加家具(add_item)
----------------------------------------------------------------------------
'''


# 1.定义家具类
class Furniture():
    # 初始化; name,area:类的属性(家具名称 占地面积)
    def __init__(self, name, area):
        self.name = name
        self.area = area

    # str方法:规范化(输出信息)
    def __str__(self):
        return '{}占地{}平房米'.format(self.name, self.area)


# 1).创建家具对象
bed = Furniture('床', 4)
print(bed)
closet = Furniture('衣柜', 2)
print(closet)
table = Furniture('餐桌', 1.5)
print(table)


class House():
    def __init__(self,house_style,zarea):
        self.house_style = house_style
        self.zarea = zarea
        # namelist: 类的属性(家具名称列表)
        self.namelist = []
        # farea: 类的属性(剩余面积)
        self.farea = zarea

    def __str__(self):
        return '户型:%s 总面积:%.2f 剩余面积:%.2f 家具:%s' % (self.house_style, self.zarea, self.farea, self.namelist)

    def add_item(self,func):
        if self.farea >= func.area:
            print('可以放置家具')
            self.namelist.append(func.name)
            self.farea = self.farea-func.area
            print('您已经将{}放置到房子里面了，房子的剩余面积为{}'.format(func.name,self.farea))
        else:
            print('地方不够，无法放置')

h = House('三居室',120)
h.add_item(bed)
h.add_item(closet)
print(h)




