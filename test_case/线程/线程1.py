'''
线程概述:几乎所有的操作系统都支持同时运行多个任务，一个任务通常就是一个程序，每个运行中的程序就是一个进程。当一个程序运
行时，内部可能包含多个顺序执流，每个顺序执行流就是一个线程。
进程 Process
线程 threading
并发和并行是两个概念，并行指在同一时刻有多条指令在多个处理器上同时执行；并发指在同一时刻只能有一条指令执行，
但多个进程指令被快速轮换执行，使得宏观上具有多个进程同时执行的效果。对于CPU在某个时间上只能执行一个程序，
也就是运行一个进程，CPU不断地在这些进程之间轮换执行。但是相对于人的感觉CPU执行的速度太快了，
所以在CPU虽然在不断的切换，但是用户感觉到好像有多个进程在同时执行
线程状态：新建，就绪，运行，阻塞，结束
'''

import threading
from time import sleep

def download(n):
    images = ['girl.jpg', 'boy.jpg', 'man.jpg']
    for image in images:
        print('正在下载:{}'.format(image))
        #sleep(2)
        print('图片{}下载成功'.format(image))

def listenmusic():
    musics = ['大碗宽面','土耳其冰淇淋','烤面筋','烤馒头片']
    for music in musics:
        print('正在听：',music)

if __name__ == '__main__':
    # 创建线程对象
    t = threading.Thread(target=download,name='线程1',args=(1,))
    t.start()
    t1 = threading.Thread(target=listenmusic, name='线程2')
    t1.start()

    n = 1
    while True:
        print(n)
        sleep(1.5)
        n += 1
