from multiprocessing import Process
from time import sleep
import os

m = 1  # 可变类型
list1 = []  # 不可变类型


def task1(s, name):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task1')
        print('正在执行任务一.........M的值为:', m)


def task2(s):
    global m
    while True:
        sleep(s)
        m += 1
        list1.append(str(m) + 'task2')
        print('正在执行任务二.........M的值为', m)


number = 1
if __name__ == '__main__':
    print(os.getpid())
    # 子进程
    p = Process(target=task1, name='任务1', args=(1, 'aa'))
    p.start()
    print(p.name)
    p1 = Process(target=task2, args=(2,))
    p1.start()

    while True:
        sleep(1)
        m += 1
        # list1.append(str(m) + 'main')
        print('---------M的值为:', m)

    print('----------------------------------------------')
    print('**********************************************')
