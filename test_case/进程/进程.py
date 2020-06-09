'''
进程包含线程，线程包含协程

Process(target=函数,name=进程的名字,args=(给函数传递的参数))
对象调用方法：
Process.start() 启动进程并执行任务
Process.run()   启动任务但没有启动进程
terminate()   终止
'''
# 进程创建
from multiprocessing import Process
from time import sleep
import os

def task1(s,name):
    while True:
        m += 1
        sleep(s)
        print('正在执行任务一.........子进程ID:',os.getpid(),'----父进程ID:',os.getppid(),name,)


def task2(s):
    while True:
        sleep(s)
        m += 1
        print('正在执行任务二.........子进程ID:',os.getpid(),'----父进程ID:',os.getppid())

number = 1
if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p = Process(target=task1,name='任务1',args=(1,'aa'))
    p.start()
    print(p.name)
    p1 = Process(target=task2,args=(2,))
    p1.start()

    while True:
        number += 1
        sleep(0.2)
        if number ==100:
            p.terminate()
            p1.terminate()
            break

    print('----------------------------------------------')
    print('**********************************************')