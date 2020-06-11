import threading
'''
线程可以共享全局变量
GIL 全局解释权锁
线程同步：数据安全，运行速度慢
进程：耗时操作，例如：下载，爬虫，IO（文件读写）
线程：计算密集型
'''
money = 1000
def task1():
    global money
    for i in range(100):
        money -= 1

def task2():
    global money
    for i in range(100):
        money -= 1

if __name__ == '__main__':
    t1 = threading.Thread(target=task1,name='线程一')
    t2 = threading.Thread(target=task2,name='线程2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('money:',money)

