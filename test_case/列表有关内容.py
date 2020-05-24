'''
1，列表元素的获取
2，列表元素的更新和删除
3，列表的切片操作
4，列表的新增
5，列表的排序
'''
# append()，extend()， insert()都是列表操作中常用的插入函数。其中前两个均接收一个参数，并插入到列表尾部。
# 最后一个接收两个参数，将参数2插入到参数1之前。
girls = ['劳拉', '泰勒', '安吉丽娜', '林夕如']
# append() 末尾追进
# while True:
#     name = input("请输入明星的名字：")
#     if name == 'quite':
#         break
#     girls.append(name)
# print(girls)

# extend(),类似列表的合并
# names = ['泰勒', '安吉丽娜', '林夕如']
# name = input("请输入明星的名字：")
# girls.extend(names)

# insert()指定位置增加
# name = input("请输入明星的名字：")
# girls.insert(1,name)
# print(girls)


'''
产生十个随机数，将其存到列表中
1，如何产生随机数
2，10个数字产生
3，将产生的随机数存放到列表中
4，打印保存
'''
import random

random_list = []
# for i in range(10): #产生十个随机数
#     ram = random.randint(1,100)
#     print(ram , end=' ')
#     #保存到列表中
#     random_list.append(ram)
# print(random_list)

# 需求2：产生十个不同的随机数，保存到列表中
i = 0
while i < 10:
    ram = random.randint(1, 100)
    if ram not in random_list:
        random_list.append(ram)
        i += 1
print(random_list)
# 需求3：求随机数列表中的最大值和最小值
# 方法一：求列表最大值函数max()和最小值函数min()
print('列表中的最大值为：', max(random_list))
print('列表中的最小值为：', min(random_list))
# 方法二
print('-------------------自定义求最大值和最小值-------------------------------')
max_value = random_list[0]
min_value = random_list[0]
for value in random_list:
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value
print('列表中的最大值为：', max_value)
print('列表中的最小值为：', min_value)

# 需求4：列表求和
#  方法一,内置函数sum()直接求和
print('列表的和为：', sum(random_list))
#  方法二
sum_1 = 0
for value in random_list:
    sum_1 += value
print('列表的和为：', sum_1)

# 需求5：列表的排序，用sorted进行排序,默认是升序
new_List1 = sorted(random_list)  # 升序
new_List2 = sorted(random_list,reverse=True)  # 降序
print(random_list)
print(new_List1)
print(new_List2)


'''
队列的特点：先进先出
栈的特点：先进后出
列表中的删除函数
del list[index]
remove（e） 删除列表中第一次出现的元素e，返回值为none
            如果没有找到要删除的元素，则抛出异常
pop（）     弹栈，默认删除列表中的最后一个元素，返回值是删除的元素
            也可以指定index删除元素
clear（）   清除列表（里面的所有元素全部删除） 

翻转：resver（）列表倒序排序，改变了原列表的位置结构
排序：list.sort()
      sorted(list) 
次数：count（）
'''