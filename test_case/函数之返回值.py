# 函数返回值
"""
将函数的运算结果“扔”出来,如果函数有多个返回值，调用时，会将返回值存到元组中
简单介绍 print 和 return 的区别，print 仅仅是打印在控制台，
而 return 则是将 return 后面的部分作为返回值作为函数的输出，可以用变量接走，继续使用该返回值做其它事。

函数需要先定义后调用，函数体中 return 语句的结果就是返回值。
如果一个函数没有 reutrn 语句，其实它有一个隐含的 return 语句，返回值是 None，类型也是 'NoneType'。
"""

#
# def sum(a, b):
#     sum = a + b
#     return sum,'aaa'
#
#
# print(sum(3, 4))

def outer():
    def inner():
        print("inner")

    print("outer")
    inner()

outer()

