"""
对象----现实中的实物
对象：一切实物都是对象
类：具有相同特征的一类事物(人、狗、老虎)
属性：对象的特征
方法：对象的功能（动作） 普通方法，，类方法，静态方法，魔术方法
手机：类
属性：颜色，大小，品牌，内存....
方法：打电话，发短信，看视频，微信聊天....
"""


class Phone():
    size = '512G'
    brand = '华为'
    color = '蓝色'


New_Phone = Phone()
print(New_Phone.brand)
New_Phone.brand = '苹果'
print(New_Phone.brand)
