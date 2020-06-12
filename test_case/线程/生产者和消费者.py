'''
生产者和消费者;两个线程之间的通信

数据共享：
进程：进程是每个进程都有一份
线程：共用一个数据
'''
import threading
import time
import queue

q = queue.Queue(10)  # 生产一个队列，用于放数据，数据最大量为10


# 生产者
def productor(q, name):
    for i in range(20):
        info = name + '生产的娃娃{}'.format(str(i))
        print(info)
        q.put(info)  # 把数据放入队列
    q.put(None)  # 生产者生产完数据以后，放入一个不再生产的标示None，消费者读取到None后，可以知道数据已经读取完


# 消费者
def consuner(q, name):
    while True:
        info = q.get()  # 从队列读取数据
        if info:  # 如果队列中存在数据，打印，不存在，直接结束循环
            print('{}拿走了{}'.format(name, info))
        else:
            break


if __name__ == '__main__':
    q = queue.Queue(10)  # 生产一个队列，用于放数据，数据最大量为10
    t1 = threading.Thread(target=productor, args=(q, '生产者'))
    t2 = threading.Thread(target=consuner, args=(q, '消费者'))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('---------------------')
