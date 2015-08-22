import threading
from time import time

class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0

     def run(self):
         for i in range(self.low,self.high):
             self.total+=i

def summing():
    thread1 = SummingThread(0,500000)
    thread2 = SummingThread(500000,1000000)
    thread1.start() # This actually causes the thread to run
    thread2.start()
    thread1.join()  # This waits until the thread has completed
    thread2.join()  
    # At this point, both threads have completed
    return thread1.total + thread2.total

def regular_sum():
    summa = 0
    for i in xrange(1000000):
        summa += i
    return summa

summing_start = time()
summing()
print "Summing Total Time:", time()-summing_start

regular_sum_start = time()
regular_sum()
print "Regular Total Time:", time() - regular_sum_start
