# 阻塞式

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
        pool.apply(task, args=(task1,))

    pool.close()
    pool.join()

    print('结束！')