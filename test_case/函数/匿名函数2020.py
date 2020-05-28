'''
<<<<<<< HEAD
lambda
max(参数，key= )
map()
reduce()
filter()
sorted()
'''
'''
匿名函数定义：
格式：lambda 参数（可以有多个参数）：表达式

lambda匿名函数的应用：**max,min,sorted,map,reduce,filter**
'''
lambda x, y: x + y

# 如何调用匿名函数
f = lambda x, y: x + y
print(f(2, 3))


# 相当于
def add(x, y):
    return x + y


add(2, 4)

# 求工资最高的人：max
salaries = {
    'egon': 3000,
    'alex': 100000000,
    'wupeiqi': 10000,
    'yuanhao': 2000
}


def get(k):
    return salaries[k]


print(max(salaries, key=get))  # 'alex'
print(max(salaries, key=lambda x: salaries[x]))
info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]
max(info, key=lambda dic: int(dic['salary']))
max([11, 22, 33, 44, 55])

# 求工资最低的人：min

salaries = {
    'egon': 3000,
    'alex': 100000000,
    'wupeiqi': 10000,
    'yuanhao': 2000
}
print(min(salaries, key=lambda x: salaries[x]))  # 'yuanhao'
info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]
min(info, key=lambda dic: int(dic['salary']))

# 把薪资字典，按照薪资的高低排序sort

salaries = {
    'egon': 3000,
    'alex': 100000000,
    'wupeiqi': 10000,
    'yuanhao': 2000
}
alaries = sorted(salaries)  # 默认按照字典的键排序
print(salaries)
#salaries = sorted(salaries, key=lambda x: salaries[x])  # 默认是升序排
#alaries = sorted(salaries, key=lambda x: salaries[x], reverse=True)  # 降序
print(salaries)
info = [
    {'name': 'egon', 'age': '18', 'salary': '3000'},
    {'name': 'wxx', 'age': '28', 'salary': '1000'},
    {'name': 'lxx', 'age': '38', 'salary': '2000'}
]
l = sorted(info, key=lambda dic: int(dic['salary']))
print(l)

# map 映射, 循环让每个元素执行函数，将每个函数执行的结果保存到新的列表中
v1 = [11, 22, 33, 44]
result = map(lambda x: x + 100, v1)  # 第一个参数为执行的函数,第二个参数为可迭代元素.
print(list(result))  # [111,122,133,144]
names = ['alex', 'wupeiqi', 'yuanhao', 'egon']
res = map(lambda x: x + '_NB' if x == 'egon' else x + '_SB', names)
print(list(res))

# reduce , 对参数序列中元素进行累积.
# 在Python2.x版本中recude是直接 import就可以的, Python3.x版本中需要从functools这个包中导入

import functools

v1 = ['wo', 'hao', 'e']


def func(x, y):
    return x + y


result = functools.reduce(func, v1)
print(result)  # wohaoe

result = functools.reduce(lambda x, y: x + y, v1)
print(result)  # wohaoe

from functools import reduce

l = ['my', 'name', 'is', 'alex', 'alex', 'is', 'sb']
res = reduce(lambda x, y: x + ' ' + y + ' ', l)
print(res)
# my name  is  alex  alex  is  sb

# filter , 按条件筛选

result = filter(lambda x: x > 2, [1, 2, 3, 4])
print(list(result))
v1 = [11, 22, 33, 'asd', 44, 'xf']


# 一般做法
def func(x):
    if type(x) == int:
        return True
    return False


result = filter(func, v1)
print(list(result))  # [11,22,33,44]

# 简化做法
result = filter(lambda x: True if type(x) == int else False, v1)
print(list(result))

# 极简做法
result = filter(lambda x: type(x) == int, v1)
print(list(result))
names = ['alex_sb', 'wxx_sb', 'yxx_sb', 'egon']
res = filter(lambda x: True if x.endswith('sb') else False, names)
res = filter(lambda x: x.endswith('sb'), names)
print(list(res))  # ['alex_sb', 'wxx_sb', 'yxx_sb']
ages = [18, 19, 10, 23, 99, 30]
res = filter(lambda n: n >= 30, ages)
print(list(res))  # [99, 30]
salaries = {
    'egon': 3000,
    'alex': 100000000,
    'wupeiqi': 10000,
    'yuanhao': 2000
}
res = filter(lambda k: salaries[k] >= 10000, salaries)
print(list(res))  # ['alex', 'wupeiqi']

