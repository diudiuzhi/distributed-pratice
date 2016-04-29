#!/usr/bin/python
import Queue
import threading
import math
import time
import sys


class Threadpool:

    def __init__(self, thread_num=10, max_queue_len=1000):
        self.max_queue_len = max_queue_len
        self.task_queue = Queue.Queue(max_queue_len)
        self.threads = []
        self._create_pool(thread_num)

    def _create_pool(self, thread_num):
        for i in xrange(thread_num):
            thread = WorkerThread(self.task_queue)
            self.threads.append(thread)

    def wait_for_complete(self):
        while not self.task_queue.empty():
            time.sleep(1)
        while True:
            all_idle = True
            for th in self.threads:
                if not th.idle:
                    all_idle = False
                    break
                if all_idle:
                    break
                else:
                    time.sleep(1)

    def add_job(self, func, *args, **kwargs):
       self.task_queue.put((func, args, kwargs))


class WorkerThread(threading.Thread):

    def __init__(self, task_queue):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.task_queue = task_queue
        self.start()
        self.idle = True

    def run(self):
        sleep_time = 0.01
        multiply = 0
        while True:
            try:
                func, args, kwargs = self.task_queue.get()
                self.idle = False
                func(*args, **kwargs)
            except Queue.Empty:
                time.sleep(sleep_time * math.pow(2, multiply))
                self.idle = True
                multiply += 1
                continue
            except:
                print sys.exc_info()
                raise
