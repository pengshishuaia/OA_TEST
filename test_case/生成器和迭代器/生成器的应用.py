'''
进程---》线程---》协程
生成器;generator
生成器一般应用在协程上面，意思就是生成器交替执行
定义生成器的方式：
1，通过列表推导式
    g = （x for x in range(6)）
2,函数+yield
def func（）：
    。。。
    yield   相当于return

g = func()

产生元素
1，next（generator） ---每次调用都会生产一个新的元素，如果元素产生完毕，再次调用的话就会产生异常
2，生成器自己的方法：
    g.__next__()
    g.send(value)
'''


def tarde1(i):
    for i in range(10):
        print('正在搬第{}快砖'.format(i))
        yield


def tarde2(x):
    for x in range(10):
        print('正在听第{}首歌'.format(x))
        yield


g1 = tarde1(5)
g2 = tarde2(5)
while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        break
