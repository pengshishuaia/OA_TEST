"""
全局变量：1，定义在函数外的拥有全局作用域 2，局变量可以在整个程序内访问
局部变量：1，定义在函数内部的变量拥有一个局部作用域 2，局部变量只能在其被声明的函数内部访问
全局变量是不可变的，例如：s='abc',函数中要修改时候，需要在函数中声明为全局变量,global
全局变量是可变的，例如list = 【a,c,d,d】,在函数中要修改时，不需要声明为全局变量，可以直接修改
"""
name = '彭帅'  # 全局变量

list = ['a','b','c']

def fun1():
    s = 'abc'  # 局部变量
    print(name)


def fun2():
    global name  # 不修改全局变量，只是获取打印，可以直接调用，但是如果要修改全局变量，则需要在函数内部声明：global 变量名
    name += '帅小伙'
    list.append(name)
    print(name)
    print(list)


def fun3():
    name = '王欣欣'
    name += '美女'
    print(name)


fun2()
fun1()
#fun2()
fun3()
