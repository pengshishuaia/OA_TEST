'''
阻塞式
非阻塞式
'''
from multiprocessing import Pool
import time
import random

#非阻塞式进程
def task1(task_nmae):
    print('开始做任务啦！',task_nmae)
    start = time.time()
    time.sleep(random()*2)
    end = time.time()
    print('完成任务用时',(end-start))

if __name__ == '__main__':
    p = Pool(5)
    task = ['听音乐','打游戏','看电影','吃饭']
    for i in range(8):
        p.apply_async(task1,args=('听音乐',))  #异步