import os
import random
import time
from multiprocessing import Process, Queue
from multiprocessing.pool import Pool
from time import sleep


def do_something():
    print('do something start.')
    sleep(3)
    print('do something end.')


def create_child_process():
    print('Process (%s) start...' % os.getpid())
    # only works on unix/linux/mac
    # fork()调用一次，返回两次，子进程永远返回0，而父进程返回子进程的ID
    pid = os.fork()
    if pid == 0:
        # 这段是在子进程中执行的代码
        print('I am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid()))
        do_something()
    else:
        # 这段是在父进程中执行的代码
        print('I (%s) just create a child process (%s).' % (os.getpid(), pid))
    print('Process (%s) end...' % os.getpid())


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def test_process():
    """ 用Process表示子进程 """
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def test_pool():
    """ 进程池 """
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


def communicate_between_process():
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()


if __name__ == '__main__':
    # create_child_process()
    # test_process()
    # test_pool()
    communicate_between_process()
