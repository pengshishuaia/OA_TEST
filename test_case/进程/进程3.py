'''
阻塞式:添加一个任务，执行一个任务，如果一个任务不执行完成，下一个任务无法执行
非阻塞式：全部添加到队列，立刻返回，并没有等待其他进程执行完毕之后

进程池：
 pool = Pool(max) 创建进程池
 pool.apply_async 非阻塞
 pool.apply 阻塞的


'''
from multiprocessing import Pool
import time
import random
import os


# 非阻塞式
def task(task_name):
    print('开始做任务啦', task_name)
    start = time.time()
    # 使用sleep
    time.sleep(random.random() * 2)
    end = time.time()
    print('任务名称：', task_name, '用时时间：', (end - start), '当前进程ID:', os.getpid())


if __name__ == '__main__':
    pool = Pool(5)
    tasks = ['听音乐', '打游戏', '看电视剧', '吃饭', '做饭', '打王者']
    for task1 in tasks:
        pool.apply_async(task, args=(task1,))

    pool.close()
    pool.join()

    print('结束！')
