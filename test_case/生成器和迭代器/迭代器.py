'''
可迭代对象： 1：生成器2：集合，列表，元组，字典，字符串（通过iter（）函数，将可迭代的，转换成迭代器）
判断是否是可迭代对象： isinstance
迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束
迭代器只能往前不会后退
可以被next（）函数调用并不断返回下一个值的对象称为迭代器：Iterable
可迭代的，是不是肯定就是迭代器？
生成器既是可迭代的，也是迭代器
列表是可迭代的，但不是迭代器
'''
from collections import Iterable
list1 = [1,2,3,4,6,8,2]
f = isinstance(list1,Iterable)
print(f)

f = isinstance('abc',Iterable)
print(f)

f = isinstance(100,Iterable)
print(f)

g = (x for x in range(10))
f = isinstance(g,Iterable)
print(f)

list1 = iter(list1)  # 通过iter（）函数，将可迭代的列表，转换成迭代器
print(next(list1))