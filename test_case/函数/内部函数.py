"""
内部函数修改全局的不可变变量时，需要在函数内部声明global
内部函数修改外部函数的不可变变量时，需要在函数内部声明nonlocal
locals() 函数会以字典类型返回当前位置的全部局部变量。
globals() 函数会以字典类型返回当前位置的全部全局变量。
"""


def fun():
    n = 100
    list1 = [2, 3, 9, 5, 4]

    def fun1():
        nonlocal n
        for index, values in enumerate(list1):
            print(index, values)
            list1[index] = values + 10
        print(list1)
        list1.sort()
        print(list1)
        n = n + 100
        print(n)

    fun1()


a = 100


def fun2():
    b = 200

    def fun3():
        nonlocal b
        global a
        c = 300
        c += 1
        b += 2
        a += 3
        print(a, b, c)

    fun3()
    print(locals())
print(globals())


fun2()
