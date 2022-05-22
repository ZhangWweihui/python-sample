import time
from _datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler


def my_clock():
    print('Hello! The time is:%s' % datetime.now())


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_clock, 'cron', hour=18, minute=1)
    scheduler.start()
    print('after scheduler.')

    while True:
        print('main 1s')
        time.sleep(1)
