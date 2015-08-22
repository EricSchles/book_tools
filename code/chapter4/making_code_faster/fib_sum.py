import threading
from time import time

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=fib(i)

def summing():
    thread1 = SummingThread(0,16)
    thread2 = SummingThread(16,32)
    thread1.start() # This actually causes the thread to run
    thread2.start()
    thread1.join()  # This waits until the thread has completed
    thread2.join() 
    # At this point, both threads have completed
    return thread1.total + thread2.total

def regular_sum():
    summa = 0
    for i in range(32):
        summa += fib(i)
    return summa

summing_start = time()
summing()
print "Summing Total Time:", time()-summing_start

regular_sum_start = time()
regular_sum()
print "Regular Total Time:", time() - regular_sum_start
