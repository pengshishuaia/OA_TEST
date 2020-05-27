"""
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，
装饰器的返回值也是一个函数对象。
它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。
装饰器;要有闭包的特点
被装饰函数带有参数？万能装饰器：def wrapper(*args, **kwargs):
                                     func(*args, **kwargs)
装饰器带有参数：带参数的装饰器是三层的，最外层的函数负责接收装饰器参数
被装饰的函数是否可以有多个装饰器？可以有多个装饰器，最先执行与被装饰函数近的装饰器
"""


# 定义一个装饰器


# def decorate(func):
#     print('wrapper外层打印测试')
#
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         print('------刷漆')
#         print('------铺地板')
#         print('------装门')
#
#     print('wrapper加载完成测试...')
#     return wrapper
#
#
# # 使用装饰器
#
# @decorate
# def house():
#     print("这是一个毛坯房")


# 定义一个带有参数的装饰器

def outer(a):
    def decorate(func):
        print('wrapper外层打印测试')

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print('------刷漆')
            print('------铺地板{}快'.format(a))
            print('------装门')
            #
            print('wrapper加载完成测试...')

        return wrapper

    return decorate


@outer(10)
def house():
    print("这是一个毛坯房")


house()
