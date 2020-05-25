"""
闭包：
在函数中提出的概念
条件：
1，外部函数定义了一个内部函数
2，外部函数有返回值
3，返回值是内部函数的名字
4，内部函数引用外部函数的变量
格式：
def 外部函数（）：
    .....
    def 内部函数（）
    .....
    return 内部函数名
"""


def outer_func(a, b):
    c = 100

    def inner_func():
        sum = a + b + c
        print(sum)

    return inner_func


function1 = outer_func(3, 4)
function1()
