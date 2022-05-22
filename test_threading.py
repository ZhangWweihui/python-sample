import multiprocessing
import threading
import time


class LoopThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        print('thread %s is running.' % threading.current_thread().name)
        n = 0
        while n < 5:
            n += 1
            print('thread %s >>> %d.' % (threading.current_thread().name, n))
            time.sleep(1)
        print('thread %s end.' % threading.current_thread().name)


class SumThread(threading.Thread):

    def __init__(self, name, startNum, endNum):
        threading.Thread.__init__(self, name=name)
        self.startNum = startNum
        self.endNum = endNum

    def run(self):
        _sum = 0
        while self.startNum <= self.endNum:
            _sum += self.startNum
            self.startNum += 1
        print("sum = %d" % _sum)


def timestamp():
    return int(round(time.time()*1000))


if __name__ == '__main__':
    start_time = timestamp()
    print('thread %s is running. start_time: %d' % (threading.current_thread().name, start_time))
    print('cpu count: %d' % multiprocessing.cpu_count())
    for i in range(1000_000):
        t = SumThread("SumThread" + str(i), 1, 100)
        t.start()
        t.join()
    end_time = timestamp()
    print('end time: %d' % end_time)
    print('thread %s end. cost time: %d' % (threading.current_thread().name, end_time-start_time))


