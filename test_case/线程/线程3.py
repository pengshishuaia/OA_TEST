'''
共享数据：
如果多个线程共同对某个数据进行修改，则有可能出现不可预期的结果，为了保证数据的正确性，需要对多个线程进行同步
一个一个完成，一个做完另一个才能进来
使用Thread对象的lock和rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法
对于那些需要每次值允许一个线程操作，可以将操作放到acquire方法和release方法之间
多线程的优势在于可以运行多个任务（至少感觉上来这样）
但当线程需要共享数据时，可能存在数据不同步的问题
为了避免这种情况的发生 ，引入了锁的概念

死锁：
'''
import threading
import random
import time
lock = threading.Lock()
list1 = [0] * 10

def task1():
    # 获取线程锁，如果已经上锁，则需要等待锁的释放
    lock.acquire() # 阻塞
    for i in range(len(list1)):
        list1[i] = 1
        time.sleep(0.5)
    lock.release() # 释放锁

def task2():
    # 获取线程锁，如果已经上锁，则需要等待锁的释放
    lock.acquire() # 阻塞
    for i in range(len(list1)):
        print('------',list1[i])
        time.sleep(0.5)
    lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()